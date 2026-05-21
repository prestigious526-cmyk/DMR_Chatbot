# CHAPTER 3: FAULT DIAGNOSIS AND TROUBLESHOOTING

## 3.0 GENERAL OVERVIEW
The Radio set features a modular physical design. This allows faults to be easily traced and pin-pointed by isolating the faulty module whenever the set fails to operate. Repairing a faulty set effectively requires a solid background knowledge of the system's operational architecture. 

When the Receiver Transmitter develops a fault, follow the troubleshooting procedures outlined below. Many symptoms are discussed alongside their probable faulty modules or components. If a module is suspected, validate its performance before replacing it with a spare module to prevent the arbitrary replacement of functional hardware. For deeper hardware servicing, reference *Technical Mechanical Part III: Overhaul and Reconditioning Instructions*.

> ### ⚠️ CRITICAL SAFETY CAUTION
> **ENSURE THE RADIO SET IS COMPLETELY SWITCHED OFF WHILE REPLACING MODULES OR CONNECTORS DURING TROUBLESHOOTING OF THE RADIO UNDER TEST.**

---

## 3.1 SYSTEMATIC TROUBLESHOOTING MATRIX
The troubleshooting procedures are covered systematically by system layer and then card/module wise. Use the following sequential layout for fault diagnosis:
* **Procedure 1:** Dead Unit Troubleshooting Flowchart (Followed when the Radio Set is dead)
* **Procedure 2:** BITE Check Matrix (Used to check the failure of any module via internal diagnostics)
* **Procedure 3:** Display / Keypad Subsystem Troubleshooting (Locates faults related to display errors or keypad input)
* **Procedure 4:** Receiver Path (Rx) Troubleshooting (Followed whenever there is no reception in the Radio Set)
* **Procedure 5:** Transmitter Path (Tx) Troubleshooting (Followed whenever there is a transmission problem with the radio set)

---

### PROCEDURE 1: Dead Unit Troubleshooting Flowchart
*Follow this procedure if the handheld terminal fails to turn ON.*

1. **Battery Voltage Check:**
   * **Action:** Check the battery voltage to ensure it is properly charged.
   * **If Voltage is Low:** Charge the Battery.
   * **If Voltage is Sufficient (Yes):** Proceed to step 2.
2. **Main Power Interface Test:**
   * **Action:** Check the voltage baseline directly at test point **TP 34**.
   * **Target Metric:** It should measure `~7.4V` or match the nominal battery voltage.
   * **If Voltage is Absent/Incorrect:** * **Root Cause:** Battery connection issue.
   * **If Voltage is Correct (Yes):** Proceed to step 3.
3. **Core Regulator Rails Test:**
   * **Action:** Check the voltage lines at **TP 35** and **TP 36**.
   * **Target Metrics:** **TP 35** must measure `3.6V`; **TP 36** must measure `5V`.
   * **If Rails are Absent/Incorrect:**
     * **Root Cause:** **U24** Power component is Faulty.
   * **If Rails are Correct (Yes):** Proceed to step 4.
4. **Logic Supply Check:**
   * **Action:** Check the voltage baseline at resistor component **R55**.
   * **Target Metric:** It should measure `3.3V`.
   * **If 3.3V Line is Absent (No):** Proceed to evaluate downstream components.
   * **If 3.3V Line is Present (Yes):**
     * **Root Cause:** **U29** component is Faulty.
5. **Execution Verification:**
   * **Condition (Yes):** If the core power steps are valid but the screen remains unresponsive:
     * **Root Cause:** Display is Faulty.
     * **Action:** Check and validate the display assembly using a specialized test jig