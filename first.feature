Feature: Authentification on server

  Scenario: Active sender can successfully authentificats on server
     Given customer has an active sender
     And mail server
     When customer try to authentificate active sender on mail server
     Then active sender is successfully authentificated

