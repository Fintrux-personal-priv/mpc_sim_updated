**Detailed Execution Flow** -

- *Contribution Submission*: Banks submit their individual contributions via the API.
- *Commitment Posting*: Banks compute and post cryptographic commitments to the bulletin board.
- *Share Distribution*: Contributions are split into shares, and each bank distributes its share to others.
- *ZKP Verification*: The protocol checks the validity of the commitments using ZKPs.
- *Round-Robin Communication*: Banks exchange shares in a round-robin fashion.
- *Aggregation*: The shares are aggregated, and the final result is computed.

```sh
 ✔ Container bank9                  Crea...                   0.1s 
 ✔ Container bank10                 Cre...                    0.0s 
 ✔ Container bank11                 Cre...                    0.0s 
 ✔ Container bank12                 Cre...                    0.0s 
 ✔ Container bank13                 Cre...                    0.0s 
 ✔ Container bank14                 Cre...                    0.0s 
 ✔ Container bank15                 Cre...                    0.0s 
 ✔ Container bank16                 Cre...                    0.0s 
 ✔ Container bank17                 Cre...                    0.0s 
 ✔ Container bank18                 Cre...                    0.0s 
 ✔ Container bank19                 Cre...                    0.0s 
Attaching to bank1, bank10, bank11, bank12, bank13, bank14, bank15, bank16, bank17, bank18, bank19, bank2, bank3, bank4, bank5, bank6, bank7, bank8, bank9
bank1   | LOG: Bank 1: Starting Process
bank1   | LOG: Bank 1: Running API server...
bank1   |  * Serving Flask app 'mpc'
bank1   |  * Debug mode: off
bank1   | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank1   |  * Running on all addresses (0.0.0.0)
bank1   |  * Running on http://127.0.0.1:8001
bank1   |  * Running on http://172.18.0.2:8001
bank1   | Press CTRL+C to quit
bank2   | LOG: Bank 2: Starting Process
bank2   | LOG: Bank 2: Starting MPC Protocol Execution
bank2   | LOG: Bank 2: Waiting for contribution submission via API...
bank2   | LOG: Bank 2: Waiting for contribution submission via API...
bank2   | LOG: Bank 2: Waiting for contribution submission via API...
bank2   | LOG: Bank 2: Waiting for contribution submission via API...
bank2   | LOG: Bank 2: Waiting for contribution submission via API...
bank2   | LOG: Bank 2: No API contribution received. Using default contribution: 102
bank2   | LOG: Bank 2: Sending value 5.37 to 1 on port 6001
bank2   | LOG: Bank 2: Sending value 5.37 to 2 on port 6002
bank2   | LOG: Bank 2: Sending value 5.37 to 3 on port 6003
bank2   | LOG: Bank 2: Sending value 5.37 to 4 on port 6004
bank2   | LOG: Bank 2: Sending value 5.37 to 5 on port 6005
bank2   | LOG: Bank 2: Sending value 5.37 to 6 on port 6006
bank2   | LOG: Bank 2: Sending value 5.37 to 7 on port 6007
bank2   | LOG: Bank 2: Sending value 5.37 to 8 on port 6008
bank2   | LOG: Bank 2: Sending value 5.37 to 9 on port 6009
bank2   | LOG: Bank 2: Sending value 5.37 to 10 on port 6010
bank2   | LOG: Bank 2: Sending value 5.37 to 11 on port 6011
bank2   | LOG: Bank 2: Sending value 5.37 to 12 on port 6012
bank2   | LOG: Bank 2: Sending value 5.37 to 13 on port 6013
bank2   | LOG: Bank 2: Sending value 5.37 to 14 on port 6014
bank2   | LOG: Bank 2: Sending value 5.37 to 15 on port 6015
bank2   | LOG: Bank 2: Sending value 5.37 to 16 on port 6016
bank2   | LOG: Bank 2: Sending value 5.37 to 17 on port 6017
bank2   | LOG: Bank 2: Sending value 5.37 to 18 on port 6018
bank2   | LOG: Bank 2: Sending value 5.37 to 19 on port 6019
bank2   | LOG: Bank 2: Sending value -0.03 to 20 on port 6020
bank2   | LOG: Bank 2: Aggregated total: 95.0
bank2   | LOG: Bank 2: Final aggregated sum: 95.0
bank3   | LOG: Bank 3: Starting Process
bank3   | LOG: Bank 3: Starting MPC Protocol Execution
bank3   | LOG: Bank 3: Waiting for contribution submission via API...
bank3   | LOG: Bank 3: Waiting for contribution submission via API...
bank3   | LOG: Bank 3: Waiting for contribution submission via API...
bank3   | LOG: Bank 3: Waiting for contribution submission via API...
bank3   | LOG: Bank 3: Waiting for contribution submission via API...
bank3   | LOG: Bank 3: No API contribution received. Using default contribution: 103
bank3   | LOG: Bank 3: Sending value 5.42 to 1 on port 6001
bank3   | LOG: Bank 3: Sending value 5.42 to 2 on port 6002
bank3   | LOG: Bank 3: Sending value 5.42 to 3 on port 6003
bank3   | LOG: Bank 3: Sending value 5.42 to 4 on port 6004
bank3   | LOG: Bank 3: Sending value 5.42 to 5 on port 6005
bank3   | LOG: Bank 3: Sending value 5.42 to 6 on port 6006
bank3   | LOG: Bank 3: Sending value 5.42 to 7 on port 6007
bank3   | LOG: Bank 3: Sending value 5.42 to 8 on port 6008
bank3   | LOG: Bank 3: Sending value 5.42 to 9 on port 6009
bank3   | LOG: Bank 3: Sending value 5.42 to 10 on port 6010
bank3   | LOG: Bank 3: Sending value 5.42 to 11 on port 6011
bank3   | LOG: Bank 3: Sending value 5.42 to 12 on port 6012
bank3   | LOG: Bank 3: Sending value 5.42 to 13 on port 6013
bank3   | LOG: Bank 3: Sending value 5.42 to 14 on port 6014
bank3   | LOG: Bank 3: Sending value 5.42 to 15 on port 6015
bank3   | LOG: Bank 3: Sending value 5.42 to 16 on port 6016
bank3   | LOG: Bank 3: Sending value 5.42 to 17 on port 6017
bank3   | LOG: Bank 3: Sending value 5.42 to 18 on port 6018
bank3   | LOG: Bank 3: Sending value 5.42 to 19 on port 6019
bank3   | LOG: Bank 3: Sending value 0.02 to 20 on port 6020
bank3   | LOG: Bank 3: Aggregated total: 95.0
bank3   | LOG: Bank 3: Final aggregated sum: 95.0
bank4   | LOG: Bank 4: Starting Process
bank4   | LOG: Bank 4: Starting MPC Protocol Execution
bank4   | LOG: Bank 4: Waiting for contribution submission via API...
bank4   | LOG: Bank 4: Waiting for contribution submission via API...
bank4   | LOG: Bank 4: Waiting for contribution submission via API...
bank4   | LOG: Bank 4: Waiting for contribution submission via API...
bank4   | LOG: Bank 4: Waiting for contribution submission via API...
bank4   | LOG: Bank 4: No API contribution received. Using default contribution: 104
bank4   | LOG: Bank 4: Sending value 5.47 to 1 on port 6001
bank4   | LOG: Bank 4: Sending value 5.47 to 2 on port 6002
bank4   | LOG: Bank 4: Sending value 5.47 to 3 on port 6003
bank4   | LOG: Bank 4: Sending value 5.47 to 4 on port 6004
bank4   | LOG: Bank 4: Sending value 5.47 to 5 on port 6005
bank4   | LOG: Bank 4: Sending value 5.47 to 6 on port 6006
bank4   | LOG: Bank 4: Sending value 5.47 to 7 on port 6007
bank4   | LOG: Bank 4: Sending value 5.47 to 8 on port 6008
bank4   | LOG: Bank 4: Sending value 5.47 to 9 on port 6009
bank4   | LOG: Bank 4: Sending value 5.47 to 10 on port 6010
bank4   | LOG: Bank 4: Sending value 5.47 to 11 on port 6011
bank4   | LOG: Bank 4: Sending value 5.47 to 12 on port 6012
bank4   | LOG: Bank 4: Sending value 5.47 to 13 on port 6013
bank4   | LOG: Bank 4: Sending value 5.47 to 14 on port 6014
bank4   | LOG: Bank 4: Sending value 5.47 to 15 on port 6015
bank4   | LOG: Bank 4: Sending value 5.47 to 16 on port 6016
bank4   | LOG: Bank 4: Sending value 5.47 to 17 on port 6017
bank4   | LOG: Bank 4: Sending value 5.47 to 18 on port 6018
bank4   | LOG: Bank 4: Sending value 5.47 to 19 on port 6019
bank4   | LOG: Bank 4: Sending value 0.07 to 20 on port 6020
bank4   | LOG: Bank 4: Aggregated total: 95.0
bank4   | LOG: Bank 4: Final aggregated sum: 95.0
bank2 exited with code 0
bank3 exited with code 0
bank5   | LOG: Bank 5: Starting Process
bank5   | LOG: Bank 5: Starting MPC Protocol Execution
bank5   | LOG: Bank 5: Waiting for contribution submission via API...
bank5   | LOG: Bank 5: Waiting for contribution submission via API...
bank5   | LOG: Bank 5: Waiting for contribution submission via API...
bank5   | LOG: Bank 5: Waiting for contribution submission via API...
bank5   | LOG: Bank 5: Waiting for contribution submission via API...
bank5   | LOG: Bank 5: No API contribution received. Using default contribution: 105
bank5   | LOG: Bank 5: Sending value 5.53 to 1 on port 6001
bank5   | LOG: Bank 5: Sending value 5.53 to 2 on port 6002
bank5   | LOG: Bank 5: Sending value 5.53 to 3 on port 6003
bank5   | LOG: Bank 5: Sending value 5.53 to 4 on port 6004
bank5   | LOG: Bank 5: Sending value 5.53 to 5 on port 6005
bank5   | LOG: Bank 5: Sending value 5.53 to 6 on port 6006
bank5   | LOG: Bank 5: Sending value 5.53 to 7 on port 6007
bank5   | LOG: Bank 5: Sending value 5.53 to 8 on port 6008
bank5   | LOG: Bank 5: Sending value 5.53 to 9 on port 6009
bank5   | LOG: Bank 5: Sending value 5.53 to 10 on port 6010
bank5   | LOG: Bank 5: Sending value 5.53 to 11 on port 6011
bank5   | LOG: Bank 5: Sending value 5.53 to 12 on port 6012
bank5   | LOG: Bank 5: Sending value 5.53 to 13 on port 6013
bank5   | LOG: Bank 5: Sending value 5.53 to 14 on port 6014
bank5   | LOG: Bank 5: Sending value 5.53 to 15 on port 6015
bank5   | LOG: Bank 5: Sending value 5.53 to 16 on port 6016
bank5   | LOG: Bank 5: Sending value 5.53 to 17 on port 6017
bank5   | LOG: Bank 5: Sending value 5.53 to 18 on port 6018
bank5   | LOG: Bank 5: Sending value 5.53 to 19 on port 6019
bank5   | LOG: Bank 5: Sending value -0.07 to 20 on port 6020
bank5   | LOG: Bank 5: Aggregated total: 95.0
bank5   | LOG: Bank 5: Final aggregated sum: 95.0
bank4 exited with code 0
bank6   | LOG: Bank 6: Starting Process
bank6   | LOG: Bank 6: Starting MPC Protocol Execution
bank6   | LOG: Bank 6: Waiting for contribution submission via API...
bank6   | LOG: Bank 6: Waiting for contribution submission via API...
bank6   | LOG: Bank 6: Waiting for contribution submission via API...
bank6   | LOG: Bank 6: Waiting for contribution submission via API...
bank6   | LOG: Bank 6: Waiting for contribution submission via API...
bank6   | LOG: Bank 6: No API contribution received. Using default contribution: 106
bank6   | LOG: Bank 6: Sending value 5.58 to 1 on port 6001
bank6   | LOG: Bank 6: Sending value 5.58 to 2 on port 6002
bank6   | LOG: Bank 6: Sending value 5.58 to 3 on port 6003
bank6   | LOG: Bank 6: Sending value 5.58 to 4 on port 6004
bank6   | LOG: Bank 6: Sending value 5.58 to 5 on port 6005
bank6   | LOG: Bank 6: Sending value 5.58 to 6 on port 6006
bank6   | LOG: Bank 6: Sending value 5.58 to 7 on port 6007
bank6   | LOG: Bank 6: Sending value 5.58 to 8 on port 6008
bank6   | LOG: Bank 6: Sending value 5.58 to 9 on port 6009
bank6   | LOG: Bank 6: Sending value 5.58 to 10 on port 6010
bank6   | LOG: Bank 6: Sending value 5.58 to 11 on port 6011
bank6   | LOG: Bank 6: Sending value 5.58 to 12 on port 6012
bank6   | LOG: Bank 6: Sending value 5.58 to 13 on port 6013
bank6   | LOG: Bank 6: Sending value 5.58 to 14 on port 6014
bank6   | LOG: Bank 6: Sending value 5.58 to 15 on port 6015
bank6   | LOG: Bank 6: Sending value 5.58 to 16 on port 6016
bank6   | LOG: Bank 6: Sending value 5.58 to 17 on port 6017
bank6   | LOG: Bank 6: Sending value 5.58 to 18 on port 6018
bank6   | LOG: Bank 6: Sending value 5.58 to 19 on port 6019
bank6   | LOG: Bank 6: Sending value -0.02 to 20 on port 6020
bank6   | LOG: Bank 6: Aggregated total: 95.0
bank6   | LOG: Bank 6: Final aggregated sum: 95.0
bank5 exited with code 0
bank7   | LOG: Bank 7: Starting Process
bank7   | LOG: Bank 7: Starting MPC Protocol Execution
bank7   | LOG: Bank 7: Waiting for contribution submission via API...
bank7   | LOG: Bank 7: Waiting for contribution submission via API...
bank7   | LOG: Bank 7: Waiting for contribution submission via API...
bank7   | LOG: Bank 7: Waiting for contribution submission via API...
bank7   | LOG: Bank 7: Waiting for contribution submission via API...
bank7   | LOG: Bank 7: No API contribution received. Using default contribution: 107
bank7   | LOG: Bank 7: Sending value 5.63 to 1 on port 6001
bank7   | LOG: Bank 7: Sending value 5.63 to 2 on port 6002
bank7   | LOG: Bank 7: Sending value 5.63 to 3 on port 6003
bank7   | LOG: Bank 7: Sending value 5.63 to 4 on port 6004
bank7   | LOG: Bank 7: Sending value 5.63 to 5 on port 6005
bank7   | LOG: Bank 7: Sending value 5.63 to 6 on port 6006
bank7   | LOG: Bank 7: Sending value 5.63 to 7 on port 6007
bank7   | LOG: Bank 7: Sending value 5.63 to 8 on port 6008
bank7   | LOG: Bank 7: Sending value 5.63 to 9 on port 6009
bank7   | LOG: Bank 7: Sending value 5.63 to 10 on port 6010
bank7   | LOG: Bank 7: Sending value 5.63 to 11 on port 6011
bank7   | LOG: Bank 7: Sending value 5.63 to 12 on port 6012
bank7   | LOG: Bank 7: Sending value 5.63 to 13 on port 6013
bank7   | LOG: Bank 7: Sending value 5.63 to 14 on port 6014
bank7   | LOG: Bank 7: Sending value 5.63 to 15 on port 6015
bank7   | LOG: Bank 7: Sending value 5.63 to 16 on port 6016
bank7   | LOG: Bank 7: Sending value 5.63 to 17 on port 6017
bank7   | LOG: Bank 7: Sending value 5.63 to 18 on port 6018
bank7   | LOG: Bank 7: Sending value 5.63 to 19 on port 6019
bank7   | LOG: Bank 7: Sending value 0.03 to 20 on port 6020
bank7   | LOG: Bank 7: Aggregated total: 95.0
bank7   | LOG: Bank 7: Final aggregated sum: 95.0
bank6 exited with code 0
bank8   | LOG: Bank 8: Starting Process
bank8   | LOG: Bank 8: Starting MPC Protocol Execution
bank8   | LOG: Bank 8: Waiting for contribution submission via API...
bank8   | LOG: Bank 8: Waiting for contribution submission via API...
bank8   | LOG: Bank 8: Waiting for contribution submission via API...
bank8   | LOG: Bank 8: Waiting for contribution submission via API...
bank8   | LOG: Bank 8: Waiting for contribution submission via API...
bank8   | LOG: Bank 8: No API contribution received. Using default contribution: 108
bank8   | LOG: Bank 8: Sending value 5.68 to 1 on port 6001
bank8   | LOG: Bank 8: Sending value 5.68 to 2 on port 6002
bank8   | LOG: Bank 8: Sending value 5.68 to 3 on port 6003
bank8   | LOG: Bank 8: Sending value 5.68 to 4 on port 6004
bank8   | LOG: Bank 8: Sending value 5.68 to 5 on port 6005
bank8   | LOG: Bank 8: Sending value 5.68 to 6 on port 6006
bank8   | LOG: Bank 8: Sending value 5.68 to 7 on port 6007
bank8   | LOG: Bank 8: Sending value 5.68 to 8 on port 6008
bank8   | LOG: Bank 8: Sending value 5.68 to 9 on port 6009
bank8   | LOG: Bank 8: Sending value 5.68 to 10 on port 6010
bank8   | LOG: Bank 8: Sending value 5.68 to 11 on port 6011
bank8   | LOG: Bank 8: Sending value 5.68 to 12 on port 6012
bank8   | LOG: Bank 8: Sending value 5.68 to 13 on port 6013
bank8   | LOG: Bank 8: Sending value 5.68 to 14 on port 6014
bank8   | LOG: Bank 8: Sending value 5.68 to 15 on port 6015
bank8   | LOG: Bank 8: Sending value 5.68 to 16 on port 6016
bank8   | LOG: Bank 8: Sending value 5.68 to 17 on port 6017
bank8   | LOG: Bank 8: Sending value 5.68 to 18 on port 6018
bank8   | LOG: Bank 8: Sending value 5.68 to 19 on port 6019
bank8   | LOG: Bank 8: Sending value 0.08 to 20 on port 6020
bank8   | LOG: Bank 8: Aggregated total: 95.0
bank8   | LOG: Bank 8: Final aggregated sum: 95.0
bank7 exited with code 0
bank9   | LOG: Bank 9: Starting Process
bank9   | LOG: Bank 9: Starting MPC Protocol Execution
bank9   | LOG: Bank 9: Waiting for contribution submission via API...
bank9   | LOG: Bank 9: Waiting for contribution submission via API...
bank9   | LOG: Bank 9: Waiting for contribution submission via API...
bank9   | LOG: Bank 9: Waiting for contribution submission via API...
bank9   | LOG: Bank 9: Waiting for contribution submission via API...
bank9   | LOG: Bank 9: No API contribution received. Using default contribution: 109
bank9   | LOG: Bank 9: Sending value 5.74 to 1 on port 6001
bank9   | LOG: Bank 9: Sending value 5.74 to 2 on port 6002
bank9   | LOG: Bank 9: Sending value 5.74 to 3 on port 6003
bank9   | LOG: Bank 9: Sending value 5.74 to 4 on port 6004
bank9   | LOG: Bank 9: Sending value 5.74 to 5 on port 6005
bank9   | LOG: Bank 9: Sending value 5.74 to 6 on port 6006
bank9   | LOG: Bank 9: Sending value 5.74 to 7 on port 6007
bank9   | LOG: Bank 9: Sending value 5.74 to 8 on port 6008
bank9   | LOG: Bank 9: Sending value 5.74 to 9 on port 6009
bank9   | LOG: Bank 9: Sending value 5.74 to 10 on port 6010
bank9   | LOG: Bank 9: Sending value 5.74 to 11 on port 6011
bank9   | LOG: Bank 9: Sending value 5.74 to 12 on port 6012
bank9   | LOG: Bank 9: Sending value 5.74 to 13 on port 6013
bank9   | LOG: Bank 9: Sending value 5.74 to 14 on port 6014
bank9   | LOG: Bank 9: Sending value 5.74 to 15 on port 6015
bank9   | LOG: Bank 9: Sending value 5.74 to 16 on port 6016
bank9   | LOG: Bank 9: Sending value 5.74 to 17 on port 6017
bank9   | LOG: Bank 9: Sending value 5.74 to 18 on port 6018
bank9   | LOG: Bank 9: Sending value 5.74 to 19 on port 6019
bank9   | LOG: Bank 9: Sending value -0.06 to 20 on port 6020
bank9   | LOG: Bank 9: Aggregated total: 95.0
bank9   | LOG: Bank 9: Final aggregated sum: 95.0
bank8 exited with code 0
bank10  | LOG: Bank 10: Starting Process
bank10  | LOG: Bank 10: Starting MPC Protocol Execution
bank10  | LOG: Bank 10: Waiting for contribution submission via API...
bank10  | LOG: Bank 10: Waiting for contribution submission via API...
bank10  | LOG: Bank 10: Waiting for contribution submission via API...
bank10  | LOG: Bank 10: Waiting for contribution submission via API...
bank10  | LOG: Bank 10: Waiting for contribution submission via API...
bank10  | LOG: Bank 10: No API contribution received. Using default contribution: 110
bank10  | LOG: Bank 10: Sending value 5.79 to 1 on port 6001
bank10  | LOG: Bank 10: Sending value 5.79 to 2 on port 6002
bank10  | LOG: Bank 10: Sending value 5.79 to 3 on port 6003
bank10  | LOG: Bank 10: Sending value 5.79 to 4 on port 6004
bank10  | LOG: Bank 10: Sending value 5.79 to 5 on port 6005
bank10  | LOG: Bank 10: Sending value 5.79 to 6 on port 6006
bank10  | LOG: Bank 10: Sending value 5.79 to 7 on port 6007
bank10  | LOG: Bank 10: Sending value 5.79 to 8 on port 6008
bank10  | LOG: Bank 10: Sending value 5.79 to 9 on port 6009
bank10  | LOG: Bank 10: Sending value 5.79 to 10 on port 6010
bank10  | LOG: Bank 10: Sending value 5.79 to 11 on port 6011
bank10  | LOG: Bank 10: Sending value 5.79 to 12 on port 6012
bank10  | LOG: Bank 10: Sending value 5.79 to 13 on port 6013
bank10  | LOG: Bank 10: Sending value 5.79 to 14 on port 6014
bank10  | LOG: Bank 10: Sending value 5.79 to 15 on port 6015
bank10  | LOG: Bank 10: Sending value 5.79 to 16 on port 6016
bank10  | LOG: Bank 10: Sending value 5.79 to 17 on port 6017
bank10  | LOG: Bank 10: Sending value 5.79 to 18 on port 6018
bank10  | LOG: Bank 10: Sending value 5.79 to 19 on port 6019
bank10  | LOG: Bank 10: Sending value -0.01 to 20 on port 6020
bank10  | LOG: Bank 10: Aggregated total: 95.0
bank10  | LOG: Bank 10: Final aggregated sum: 95.0
bank9 exited with code 0
bank11  | LOG: Bank 11: Starting Process
bank11  | LOG: Bank 11: Starting MPC Protocol Execution
bank11  | LOG: Bank 11: Waiting for contribution submission via API...
bank11  | LOG: Bank 11: Waiting for contribution submission via API...
bank11  | LOG: Bank 11: Waiting for contribution submission via API...
bank11  | LOG: Bank 11: Waiting for contribution submission via API...
bank11  | LOG: Bank 11: Waiting for contribution submission via API...
bank11  | LOG: Bank 11: No API contribution received. Using default contribution: 111
bank11  | LOG: Bank 11: Sending value 5.84 to 1 on port 6001
bank11  | LOG: Bank 11: Sending value 5.84 to 2 on port 6002
bank11  | LOG: Bank 11: Sending value 5.84 to 3 on port 6003
bank11  | LOG: Bank 11: Sending value 5.84 to 4 on port 6004
bank11  | LOG: Bank 11: Sending value 5.84 to 5 on port 6005
bank11  | LOG: Bank 11: Sending value 5.84 to 6 on port 6006
bank11  | LOG: Bank 11: Sending value 5.84 to 7 on port 6007
bank11  | LOG: Bank 11: Sending value 5.84 to 8 on port 6008
bank11  | LOG: Bank 11: Sending value 5.84 to 9 on port 6009
bank11  | LOG: Bank 11: Sending value 5.84 to 10 on port 6010
bank11  | LOG: Bank 11: Sending value 5.84 to 11 on port 6011
bank11  | LOG: Bank 11: Sending value 5.84 to 12 on port 6012
bank11  | LOG: Bank 11: Sending value 5.84 to 13 on port 6013
bank11  | LOG: Bank 11: Sending value 5.84 to 14 on port 6014
bank11  | LOG: Bank 11: Sending value 5.84 to 15 on port 6015
bank11  | LOG: Bank 11: Sending value 5.84 to 16 on port 6016
bank11  | LOG: Bank 11: Sending value 5.84 to 17 on port 6017
bank11  | LOG: Bank 11: Sending value 5.84 to 18 on port 6018
bank11  | LOG: Bank 11: Sending value 5.84 to 19 on port 6019
bank11  | LOG: Bank 11: Sending value 0.04 to 20 on port 6020
bank11  | LOG: Bank 11: Aggregated total: 95.0
bank11  | LOG: Bank 11: Final aggregated sum: 95.0
bank12  | LOG: Bank 12: Starting Process
bank12  | LOG: Bank 12: Starting MPC Protocol Execution
bank12  | LOG: Bank 12: Waiting for contribution submission via API...
bank12  | LOG: Bank 12: Waiting for contribution submission via API...
bank12  | LOG: Bank 12: Waiting for contribution submission via API...
bank12  | LOG: Bank 12: Waiting for contribution submission via API...
bank12  | LOG: Bank 12: Waiting for contribution submission via API...
bank12  | LOG: Bank 12: No API contribution received. Using default contribution: 112
bank12  | LOG: Bank 12: Sending value 5.89 to 1 on port 6001
bank12  | LOG: Bank 12: Sending value 5.89 to 2 on port 6002
bank12  | LOG: Bank 12: Sending value 5.89 to 3 on port 6003
bank12  | LOG: Bank 12: Sending value 5.89 to 4 on port 6004
bank12  | LOG: Bank 12: Sending value 5.89 to 5 on port 6005
bank12  | LOG: Bank 12: Sending value 5.89 to 6 on port 6006
bank12  | LOG: Bank 12: Sending value 5.89 to 7 on port 6007
bank12  | LOG: Bank 12: Sending value 5.89 to 8 on port 6008
bank12  | LOG: Bank 12: Sending value 5.89 to 9 on port 6009
bank12  | LOG: Bank 12: Sending value 5.89 to 10 on port 6010
bank12  | LOG: Bank 12: Sending value 5.89 to 11 on port 6011
bank12  | LOG: Bank 12: Sending value 5.89 to 12 on port 6012
bank12  | LOG: Bank 12: Sending value 5.89 to 13 on port 6013
bank12  | LOG: Bank 12: Sending value 5.89 to 14 on port 6014
bank12  | LOG: Bank 12: Sending value 5.89 to 15 on port 6015
bank12  | LOG: Bank 12: Sending value 5.89 to 16 on port 6016
bank12  | LOG: Bank 12: Sending value 5.89 to 17 on port 6017
bank12  | LOG: Bank 12: Sending value 5.89 to 18 on port 6018
bank12  | LOG: Bank 12: Sending value 5.89 to 19 on port 6019
bank12  | LOG: Bank 12: Sending value 0.09 to 20 on port 6020
bank12  | LOG: Bank 12: Aggregated total: 95.0
bank12  | LOG: Bank 12: Final aggregated sum: 95.0
bank10 exited with code 0
bank11 exited with code 0
bank13  | LOG: Bank 13: Starting Process
bank13  | LOG: Bank 13: Starting MPC Protocol Execution
bank13  | LOG: Bank 13: Waiting for contribution submission via API...
bank13  | LOG: Bank 13: Waiting for contribution submission via API...
bank13  | LOG: Bank 13: Waiting for contribution submission via API...
bank13  | LOG: Bank 13: Waiting for contribution submission via API...
bank13  | LOG: Bank 13: Waiting for contribution submission via API...
bank13  | LOG: Bank 13: No API contribution received. Using default contribution: 113
bank13  | LOG: Bank 13: Sending value 5.95 to 1 on port 6001
bank13  | LOG: Bank 13: Sending value 5.95 to 2 on port 6002
bank13  | LOG: Bank 13: Sending value 5.95 to 3 on port 6003
bank13  | LOG: Bank 13: Sending value 5.95 to 4 on port 6004
bank13  | LOG: Bank 13: Sending value 5.95 to 5 on port 6005
bank13  | LOG: Bank 13: Sending value 5.95 to 6 on port 6006
bank13  | LOG: Bank 13: Sending value 5.95 to 7 on port 6007
bank13  | LOG: Bank 13: Sending value 5.95 to 8 on port 6008
bank13  | LOG: Bank 13: Sending value 5.95 to 9 on port 6009
bank13  | LOG: Bank 13: Sending value 5.95 to 10 on port 6010
bank13  | LOG: Bank 13: Sending value 5.95 to 11 on port 6011
bank13  | LOG: Bank 13: Sending value 5.95 to 12 on port 6012
bank13  | LOG: Bank 13: Sending value 5.95 to 13 on port 6013
bank13  | LOG: Bank 13: Sending value 5.95 to 14 on port 6014
bank13  | LOG: Bank 13: Sending value 5.95 to 15 on port 6015
bank13  | LOG: Bank 13: Sending value 5.95 to 16 on port 6016
bank13  | LOG: Bank 13: Sending value 5.95 to 17 on port 6017
bank13  | LOG: Bank 13: Sending value 5.95 to 18 on port 6018
bank13  | LOG: Bank 13: Sending value 5.95 to 19 on port 6019
bank13  | LOG: Bank 13: Sending value -0.05 to 20 on port 6020
bank13  | LOG: Bank 13: Aggregated total: 95.0
bank13  | LOG: Bank 13: Final aggregated sum: 95.0
bank12 exited with code 0
bank13 exited with code 0
bank14  | LOG: Bank 14: Starting Process
bank14  | LOG: Bank 14: Starting MPC Protocol Execution
bank14  | LOG: Bank 14: Waiting for contribution submission via API...
bank14  | LOG: Bank 14: Waiting for contribution submission via API...
bank14  | LOG: Bank 14: Waiting for contribution submission via API...
bank14  | LOG: Bank 14: Waiting for contribution submission via API...
bank14  | LOG: Bank 14: Waiting for contribution submission via API...
bank14  | LOG: Bank 14: No API contribution received. Using default contribution: 114
bank14  | LOG: Bank 14: Sending value 6.0 to 1 on port 6001
bank14  | LOG: Bank 14: Sending value 6.0 to 2 on port 6002
bank14  | LOG: Bank 14: Sending value 6.0 to 3 on port 6003
bank14  | LOG: Bank 14: Sending value 6.0 to 4 on port 6004
bank14  | LOG: Bank 14: Sending value 6.0 to 5 on port 6005
bank14  | LOG: Bank 14: Sending value 6.0 to 6 on port 6006
bank14  | LOG: Bank 14: Sending value 6.0 to 7 on port 6007
bank14  | LOG: Bank 14: Sending value 6.0 to 8 on port 6008
bank14  | LOG: Bank 14: Sending value 6.0 to 9 on port 6009
bank14  | LOG: Bank 14: Sending value 6.0 to 10 on port 6010
bank14  | LOG: Bank 14: Sending value 6.0 to 11 on port 6011
bank14  | LOG: Bank 14: Sending value 6.0 to 12 on port 6012
bank14  | LOG: Bank 14: Sending value 6.0 to 13 on port 6013
bank14  | LOG: Bank 14: Sending value 6.0 to 14 on port 6014
bank14  | LOG: Bank 14: Sending value 6.0 to 15 on port 6015
bank14  | LOG: Bank 14: Sending value 6.0 to 16 on port 6016
bank14  | LOG: Bank 14: Sending value 6.0 to 17 on port 6017
bank14  | LOG: Bank 14: Sending value 6.0 to 18 on port 6018
bank14  | LOG: Bank 14: Sending value 6.0 to 19 on port 6019
bank14  | LOG: Bank 14: Sending value 0.0 to 20 on port 6020
bank14  | LOG: Bank 14: Aggregated total: 95.0
bank14  | LOG: Bank 14: Final aggregated sum: 95.0
bank14 exited with code 0
bank15  | LOG: Bank 15: Starting Process
bank15  | LOG: Bank 15: Starting MPC Protocol Execution
bank15  | LOG: Bank 15: Waiting for contribution submission via API...
bank15  | LOG: Bank 15: Waiting for contribution submission via API...
bank15  | LOG: Bank 15: Waiting for contribution submission via API...
bank15  | LOG: Bank 15: Waiting for contribution submission via API...
bank15  | LOG: Bank 15: Waiting for contribution submission via API...
bank15  | LOG: Bank 15: No API contribution received. Using default contribution: 115
bank15  | LOG: Bank 15: Sending value 6.05 to 1 on port 6001
bank15  | LOG: Bank 15: Sending value 6.05 to 2 on port 6002
bank15  | LOG: Bank 15: Sending value 6.05 to 3 on port 6003
bank15  | LOG: Bank 15: Sending value 6.05 to 4 on port 6004
bank15  | LOG: Bank 15: Sending value 6.05 to 5 on port 6005
bank15  | LOG: Bank 15: Sending value 6.05 to 6 on port 6006
bank15  | LOG: Bank 15: Sending value 6.05 to 7 on port 6007
bank15  | LOG: Bank 15: Sending value 6.05 to 8 on port 6008
bank15  | LOG: Bank 15: Sending value 6.05 to 9 on port 6009
bank15  | LOG: Bank 15: Sending value 6.05 to 10 on port 6010
bank15  | LOG: Bank 15: Sending value 6.05 to 11 on port 6011
bank15  | LOG: Bank 15: Sending value 6.05 to 12 on port 6012
bank15  | LOG: Bank 15: Sending value 6.05 to 13 on port 6013
bank15  | LOG: Bank 15: Sending value 6.05 to 14 on port 6014
bank15  | LOG: Bank 15: Sending value 6.05 to 15 on port 6015
bank15  | LOG: Bank 15: Sending value 6.05 to 16 on port 6016
bank15  | LOG: Bank 15: Sending value 6.05 to 17 on port 6017
bank15  | LOG: Bank 15: Sending value 6.05 to 18 on port 6018
bank15  | LOG: Bank 15: Sending value 6.05 to 19 on port 6019
bank15  | LOG: Bank 15: Sending value 0.05 to 20 on port 6020
bank15  | LOG: Bank 15: Aggregated total: 95.0
bank15  | LOG: Bank 15: Final aggregated sum: 95.0
bank16  | LOG: Bank 16: Starting Process
bank16  | LOG: Bank 16: Starting MPC Protocol Execution
bank16  | LOG: Bank 16: Waiting for contribution submission via API...
bank16  | LOG: Bank 16: Waiting for contribution submission via API...
bank16  | LOG: Bank 16: Waiting for contribution submission via API...
bank16  | LOG: Bank 16: Waiting for contribution submission via API...
bank16  | LOG: Bank 16: Waiting for contribution submission via API...
bank16  | LOG: Bank 16: No API contribution received. Using default contribution: 116
bank16  | LOG: Bank 16: Sending value 6.11 to 1 on port 6001
bank16  | LOG: Bank 16: Sending value 6.11 to 2 on port 6002
bank16  | LOG: Bank 16: Sending value 6.11 to 3 on port 6003
bank16  | LOG: Bank 16: Sending value 6.11 to 4 on port 6004
bank16  | LOG: Bank 16: Sending value 6.11 to 5 on port 6005
bank16  | LOG: Bank 16: Sending value 6.11 to 6 on port 6006
bank16  | LOG: Bank 16: Sending value 6.11 to 7 on port 6007
bank16  | LOG: Bank 16: Sending value 6.11 to 8 on port 6008
bank16  | LOG: Bank 16: Sending value 6.11 to 9 on port 6009
bank16  | LOG: Bank 16: Sending value 6.11 to 10 on port 6010
bank16  | LOG: Bank 16: Sending value 6.11 to 11 on port 6011
bank16  | LOG: Bank 16: Sending value 6.11 to 12 on port 6012
bank16  | LOG: Bank 16: Sending value 6.11 to 13 on port 6013
bank16  | LOG: Bank 16: Sending value 6.11 to 14 on port 6014
bank16  | LOG: Bank 16: Sending value 6.11 to 15 on port 6015
bank16  | LOG: Bank 16: Sending value 6.11 to 16 on port 6016
bank16  | LOG: Bank 16: Sending value 6.11 to 17 on port 6017
bank16  | LOG: Bank 16: Sending value 6.11 to 18 on port 6018
bank16  | LOG: Bank 16: Sending value 6.11 to 19 on port 6019
bank16  | LOG: Bank 16: Sending value -0.09 to 20 on port 6020
bank16  | LOG: Bank 16: Aggregated total: 95.0
bank16  | LOG: Bank 16: Final aggregated sum: 95.0
bank15 exited with code 0
bank17  | LOG: Bank 17: Starting Process
bank17  | LOG: Bank 17: Starting MPC Protocol Execution
bank17  | LOG: Bank 17: Waiting for contribution submission via API...
bank17  | LOG: Bank 17: Waiting for contribution submission via API...
bank17  | LOG: Bank 17: Waiting for contribution submission via API...
bank17  | LOG: Bank 17: Waiting for contribution submission via API...
bank17  | LOG: Bank 17: Waiting for contribution submission via API...
bank17  | LOG: Bank 17: No API contribution received. Using default contribution: 117
bank17  | LOG: Bank 17: Sending value 6.16 to 1 on port 6001
bank17  | LOG: Bank 17: Sending value 6.16 to 2 on port 6002
bank17  | LOG: Bank 17: Sending value 6.16 to 3 on port 6003
bank17  | LOG: Bank 17: Sending value 6.16 to 4 on port 6004
bank17  | LOG: Bank 17: Sending value 6.16 to 5 on port 6005
bank17  | LOG: Bank 17: Sending value 6.16 to 6 on port 6006
bank17  | LOG: Bank 17: Sending value 6.16 to 7 on port 6007
bank17  | LOG: Bank 17: Sending value 6.16 to 8 on port 6008
bank17  | LOG: Bank 17: Sending value 6.16 to 9 on port 6009
bank17  | LOG: Bank 17: Sending value 6.16 to 10 on port 6010
bank17  | LOG: Bank 17: Sending value 6.16 to 11 on port 6011
bank17  | LOG: Bank 17: Sending value 6.16 to 12 on port 6012
bank17  | LOG: Bank 17: Sending value 6.16 to 13 on port 6013
bank17  | LOG: Bank 17: Sending value 6.16 to 14 on port 6014
bank17  | LOG: Bank 17: Sending value 6.16 to 15 on port 6015
bank17  | LOG: Bank 17: Sending value 6.16 to 16 on port 6016
bank17  | LOG: Bank 17: Sending value 6.16 to 17 on port 6017
bank17  | LOG: Bank 17: Sending value 6.16 to 18 on port 6018
bank17  | LOG: Bank 17: Sending value 6.16 to 19 on port 6019
bank17  | LOG: Bank 17: Sending value -0.04 to 20 on port 6020
bank17  | LOG: Bank 17: Aggregated total: 95.0
bank17  | LOG: Bank 17: Final aggregated sum: 95.0
bank16 exited with code 0
bank17 exited with code 0
bank18  | LOG: Bank 18: Starting Process
bank18  | LOG: Bank 18: Starting MPC Protocol Execution
bank18  | LOG: Bank 18: Waiting for contribution submission via API...
bank18  | LOG: Bank 18: Waiting for contribution submission via API...
bank18  | LOG: Bank 18: Waiting for contribution submission via API...
bank18  | LOG: Bank 18: Waiting for contribution submission via API...
bank18  | LOG: Bank 18: Waiting for contribution submission via API...
bank18  | LOG: Bank 18: No API contribution received. Using default contribution: 118
bank18  | LOG: Bank 18: Sending value 6.21 to 1 on port 6001
bank18  | LOG: Bank 18: Sending value 6.21 to 2 on port 6002
bank18  | LOG: Bank 18: Sending value 6.21 to 3 on port 6003
bank18  | LOG: Bank 18: Sending value 6.21 to 4 on port 6004
bank18  | LOG: Bank 18: Sending value 6.21 to 5 on port 6005
bank18  | LOG: Bank 18: Sending value 6.21 to 6 on port 6006
bank18  | LOG: Bank 18: Sending value 6.21 to 7 on port 6007
bank18  | LOG: Bank 18: Sending value 6.21 to 8 on port 6008
bank18  | LOG: Bank 18: Sending value 6.21 to 9 on port 6009
bank18  | LOG: Bank 18: Sending value 6.21 to 10 on port 6010
bank18  | LOG: Bank 18: Sending value 6.21 to 11 on port 6011
bank18  | LOG: Bank 18: Sending value 6.21 to 12 on port 6012
bank18  | LOG: Bank 18: Sending value 6.21 to 13 on port 6013
bank18  | LOG: Bank 18: Sending value 6.21 to 14 on port 6014
bank18  | LOG: Bank 18: Sending value 6.21 to 15 on port 6015
bank18  | LOG: Bank 18: Sending value 6.21 to 16 on port 6016
bank18  | LOG: Bank 18: Sending value 6.21 to 17 on port 6017
bank18  | LOG: Bank 18: Sending value 6.21 to 18 on port 6018
bank18  | LOG: Bank 18: Sending value 6.21 to 19 on port 6019
bank18  | LOG: Bank 18: Sending value 0.01 to 20 on port 6020
bank18  | LOG: Bank 18: Aggregated total: 95.0
bank18  | LOG: Bank 18: Final aggregated sum: 95.0
bank19  | LOG: Bank 19: Starting Process
bank19  | LOG: Bank 19: Starting MPC Protocol Execution
bank19  | LOG: Bank 19: Waiting for contribution submission via API...
bank19  | LOG: Bank 19: Waiting for contribution submission via API...
bank19  | LOG: Bank 19: Waiting for contribution submission via API...
bank19  | LOG: Bank 19: Waiting for contribution submission via API...
bank19  | LOG: Bank 19: Waiting for contribution submission via API...
bank19  | LOG: Bank 19: No API contribution received. Using default contribution: 119
bank19  | LOG: Bank 19: Sending value 6.26 to 1 on port 6001
bank19  | LOG: Bank 19: Sending value 6.26 to 2 on port 6002
bank19  | LOG: Bank 19: Sending value 6.26 to 3 on port 6003
bank19  | LOG: Bank 19: Sending value 6.26 to 4 on port 6004
bank19  | LOG: Bank 19: Sending value 6.26 to 5 on port 6005
bank19  | LOG: Bank 19: Sending value 6.26 to 6 on port 6006
bank19  | LOG: Bank 19: Sending value 6.26 to 7 on port 6007
bank19  | LOG: Bank 19: Sending value 6.26 to 8 on port 6008
bank19  | LOG: Bank 19: Sending value 6.26 to 9 on port 6009
bank19  | LOG: Bank 19: Sending value 6.26 to 10 on port 6010
bank19  | LOG: Bank 19: Sending value 6.26 to 11 on port 6011
bank19  | LOG: Bank 19: Sending value 6.26 to 12 on port 6012
bank19  | LOG: Bank 19: Sending value 6.26 to 13 on port 6013
bank19  | LOG: Bank 19: Sending value 6.26 to 14 on port 6014
bank19  | LOG: Bank 19: Sending value 6.26 to 15 on port 6015
bank19  | LOG: Bank 19: Sending value 6.26 to 16 on port 6016
bank19  | LOG: Bank 19: Sending value 6.26 to 17 on port 6017
bank19  | LOG: Bank 19: Sending value 6.26 to 18 on port 6018
bank19  | LOG: Bank 19: Sending value 6.26 to 19 on port 6019
bank19  | LOG: Bank 19: Sending value 0.06 to 20 on port 6020
bank19  | LOG: Bank 19: Aggregated total: 95.0
bank19  | LOG: Bank 19: Final aggregated sum: 95.0
bank18 exited with code 0
bank19 exited with code 0
```