-- Keep a log of any SQL queries you execute as you solve the mystery.

.schema
-- To get an overview of available information

SELECT * FROM people;
-- Get an overview of possible criminals

SELECT * FROM crime_scene_reports;
-- Get an overview of crime_scene_reports

SELECT * FROM crime_scene_reports WHERE description LIKE "%theft%";
-- Find all theft related crimes. The duck robbery took place at 10:15am at Chamberlin Stree courthouse on 2020-07-28

SELECT * FROM courthouse_security_logs;
-- Check security logs for theft details with given info

SELECT * FROM courthouse_security_logs WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute = 15;
-- Narrowing search. No results.

SELECT * FROM courthouse_security_logs WHERE year = 2020 AND month = 7 AND day = 28;
-- Widening search. Suspects: 5P2BI95 94KL13X 6P58WS2 4328GD8 G412CB7

SELECT * FROM interviews
-- Checking interviews for info

SELECT * FROM interviews WHERE year = 2020 AND month = 7 AND day = 28;
-- Narrowing search. Thief withdrew money from ATM of Fifer Street earlier. Thief was planning to take the earliest flight out of Fiftyville the day following the theft. He called accomplice and had a 1 minute phonecall and told his accomplice to purchase tickets.

SELECT * FROM atm_transactions;
-- Check if there's any info here.

SELECT * FROM atm_transactions WHERE year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street";
-- Narrowing results.

SELECT bank_accounts.* FROM bank_accounts JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number WHERE bank_accounts.account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street");
-- Check possible bank accounts

SELECT * FROM people WHERE id IN (SELECT bank_accounts.person_id FROM bank_accounts JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number WHERE bank_accounts.account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street"));
-- Checking suspects.

SELECT * FROM airports;
-- Check possible airports. Airport in Fiftyville is named "Fiftyville Regional Airport" with an id = 8 and abbreiviation = CSF.

SELECT * FROM flights WHERE origin_airport_id = 8 AND year = 2020 AND month = 7 AND day = 29;
-- Checking flights. Earliest flight was id = 18.

SELECT passport_number FROM passengers WHERE flight_id = 36;
-- Checking passports to identify people. Returned a couple passports.

SELECT * FROM people WHERE license_plate = "5P2BI95" OR license_plate = "94KL13X" OR license_plate = "6P58WS2" OR license_plate = "G412CB7" OR license_plate = "4328GD8";
-- Finding matches with bank accounts: Danielle (467400) and Ernest (686048)

SELECT * FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);
-- Find people on previously searched for flight. Danielle and Ernest again.

SELECT * FROM phone_calls
-- See how phone_calls work

SELECT * FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE id = 467400 OR id = 686048);
-- Check calls of suspects.

SELECT * FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE id = 467400 OR id = 686048) AND year = 2020 AND month = 7 AND day = 28;
-- Check calls of suspects on theft date. There's a 45 second call! Call id = 233

SELECT * FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE id = 467400 OR id = 686048) AND year = 2020 AND month = 7 AND day = 28);
-- Ernest (686048) is the thief. Next step is to find the receiver of the call.

SELECT * FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE id = 233 AND year = 2020 AND month = 7 AND day = 28);
-- Berthold (864400) is the accomplice.

SELECT * FROM airports WHERE id IN (SELECT destination_airport_id FROM flights WHERE id = 36);
-- Ernest (686048) escaped to LHR Heathrow Airport London (4)

