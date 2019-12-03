# SER415 Traffic Simulator - Team 6

### Team: Manolito Ramirez, Jessica Gilbert, Mike Wagner, Carlos Franco, Arthur Rivera, and Ryan Kirmis

<b>INSTRUCTIONS FOR RUNNING APPLICATION:</b>


<b>SOURCE FUNCTIONS<b>

    startSim(event) - Starts simulation when user clicks 'Run Simulation' button.

    cycleNS() - Cycles through North/South green state.
    
    cycleNSGrnArr() - Cycles through North/South green arrow state.

    cycleWE() - Cycles through West/East green state.
    
    cycleWEGrnArr() - Cycles through West/East green arrow state.
    
    inflowCars() - Inflow cars waiting at intersection based on user input.
    
    stopSim(event) - Stops the simulation if running.

    resetSim(event) - Resets the simulation if running.

    calculateCurrRate(t) - Returns the traffic flow rate at a specific time since GREEN light activated.
    
    scenarioChange(*args) - Updates flow rate/flow delay scalars based on scenario selection.
    
    dayChange(*args) - Updates flow rate/flow delay scalars based on day selection.
    
    timeChange(*args) - Updates flow rate/flow delay scalars based on time of day selection.
    
    disableEdits() - Disables all text boxes so that user cannot modify them.
    
    enableEdits() - Enables all text boxes so that users can modify them.
