-- This script creates a stored procedure AddBonus that
-- adds a new correction for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER |
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
    DECLARE total FLOAT DEFAULT 0;
    DECLARE counted FLOAT DEFAULT 0;

    SELECT SUM(score) INTO total
        FROM corrections
        WHERE corrections.user_id = user_id;

    SELECT COUNT(*) INTO counted
        FROM corrections
        WHERE corrections.user_id = user_id;

    UPDATE users 
        SET users.average_score = IF(counted = 0, 0, total / counted)
        WHERE users.id = user_id;
END;
|