USE aa_dev_3;
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS killtracker_killmail;
DROP TABLE IF EXISTS killtracker_killmailattacker;
DROP TABLE IF EXISTS killtracker_killmailposition;
DROP TABLE IF EXISTS killtracker_killmailvictim;
DROP TABLE IF EXISTS killtracker_killmailzkb;
DROP TABLE IF EXISTS killtracker_trackedkillmail;
DROP TABLE IF EXISTS killtracker_trackedkillmail_attackers_ship_types;
DROP TABLE IF EXISTS killtracker_tracker;
DROP TABLE IF EXISTS killtracker_tracker_exclude_attacker_alliances;
DROP TABLE IF EXISTS killtracker_tracker_exclude_attacker_corporations;
DROP TABLE IF EXISTS killtracker_tracker_require_attacker_alliances;
DROP TABLE IF EXISTS killtracker_tracker_require_attacker_corporations;
DROP TABLE IF EXISTS killtracker_tracker_require_attackers_ship_groups;
DROP TABLE IF EXISTS killtracker_tracker_require_attackers_ship_types;
DROP TABLE IF EXISTS killtracker_tracker_require_constellations;
DROP TABLE IF EXISTS killtracker_tracker_require_regions;
DROP TABLE IF EXISTS killtracker_tracker_require_solar_systems;
DROP TABLE IF EXISTS killtracker_tracker_require_victim_alliances;
DROP TABLE IF EXISTS killtracker_tracker_require_victim_corporations;
DROP TABLE IF EXISTS killtracker_tracker_require_victim_ship_groups;
DROP TABLE IF EXISTS killtracker_webhook;
SET FOREIGN_KEY_CHECKS=1;