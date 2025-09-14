/*
  # Create users and predictions tables

  1. New Tables
    - `user_profiles`
      - `id` (uuid, primary key)
      - `email` (text, unique)
      - `name` (text)
      - `created_at` (timestamp)
    - `crop_predictions`
      - `id` (uuid, primary key)
      - `user_id` (uuid, foreign key)
      - `nitrogen` (numeric)
      - `phosphorus` (numeric)
      - `potassium` (numeric)
      - `temperature` (numeric)
      - `humidity` (numeric)
      - `ph` (numeric)
      - `rainfall` (numeric)
      - `predicted_crop` (text)
      - `confidence` (numeric)
      - `created_at` (timestamp)

  2. Security
    - Enable RLS on both tables
    - Add policies for authenticated users to manage their own data
*/

-- Create user_profiles table
CREATE TABLE IF NOT EXISTS user_profiles (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  email text UNIQUE NOT NULL,
  name text NOT NULL DEFAULT '',
  created_at timestamptz DEFAULT now()
);

-- Create crop_predictions table
CREATE TABLE IF NOT EXISTS crop_predictions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid REFERENCES user_profiles(id) ON DELETE CASCADE,
  nitrogen numeric NOT NULL,
  phosphorus numeric NOT NULL,
  potassium numeric NOT NULL,
  temperature numeric NOT NULL,
  humidity numeric NOT NULL,
  ph numeric NOT NULL,
  rainfall numeric NOT NULL,
  predicted_crop text NOT NULL,
  confidence numeric DEFAULT 0,
  created_at timestamptz DEFAULT now()
);

-- Enable Row Level Security
ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE crop_predictions ENABLE ROW LEVEL SECURITY;

-- Create policies for user_profiles
CREATE POLICY "Users can read own profile"
  ON user_profiles
  FOR SELECT
  TO authenticated
  USING (auth.uid() = id);

CREATE POLICY "Users can update own profile"
  ON user_profiles
  FOR UPDATE
  TO authenticated
  USING (auth.uid() = id);

CREATE POLICY "Users can insert own profile"
  ON user_profiles
  FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = id);

-- Create policies for crop_predictions
CREATE POLICY "Users can read own predictions"
  ON crop_predictions
  FOR SELECT
  TO authenticated
  USING (user_id = auth.uid());

CREATE POLICY "Users can insert own predictions"
  ON crop_predictions
  FOR INSERT
  TO authenticated
  WITH CHECK (user_id = auth.uid());

CREATE POLICY "Users can update own predictions"
  ON crop_predictions
  FOR UPDATE
  TO authenticated
  USING (user_id = auth.uid());

CREATE POLICY "Users can delete own predictions"
  ON crop_predictions
  FOR DELETE
  TO authenticated
  USING (user_id = auth.uid());