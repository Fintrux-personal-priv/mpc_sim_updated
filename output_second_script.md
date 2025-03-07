```bash
Sahbaazs-MacBook-Air:mpc_sim_updated skywarrior$ docker compose up
WARN[0000] /Users/skywarrior/mpc_sim_updated/docker-compose.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 20/20
 ✔ Network mpc_sim_updated_mpc-net  Created                                                                         0.1s 
 ✔ Container bank1                  Created                                                                         0.0s 
 ✔ Container bank2                  Created                                                                         0.0s 
 ✔ Container bank3                  Created                                                                         0.0s 
 ✔ Container bank4                  Created                                                                         0.0s 
 ✔ Container bank5                  Created                                                                         0.0s 
 ✔ Container bank6                  Created                                                                         0.0s 
 ✔ Container bank7                  Created                                                                         0.0s 
 ✔ Container bank8                  Created                                                                         0.0s 
 ✔ Container bank9                  Created                                                                         0.1s 
 ✔ Container bank10                 Created                                                                         0.0s 
 ✔ Container bank11                 Created                                                                         0.0s 
 ✔ Container bank12                 Created                                                                         0.0s 
 ✔ Container bank13                 Created                                                                         0.0s 
 ✔ Container bank14                 Created                                                                         0.0s 
 ✔ Container bank15                 Created                                                                         0.0s 
 ✔ Container bank16                 Created                                                                         0.0s 
 ✔ Container bank17                 Created                                                                         0.0s 
 ✔ Container bank18                 Created                                                                         0.0s 
 ✔ Container bank19                 Created                                                                         0.0s 
Attaching to bank1, bank10, bank11, bank12, bank13, bank14, bank15, bank16, bank17, bank18, bank19, bank2, bank3, bank4, bank5, bank6, bank7, bank8, bank9
bank1   | LOG: Bank 1: ======= Starting Process =======
bank1   | LOG: Bank 1: Bank 1 posted commitment: 16dc368a89b428b2485484313ba67a3912ca03f2b2b42429174a4f8b3dc84e44
bank1   | LOG: Bank 1: ZKP verification passed for commitment: 16dc368a89b428b2485484313ba67a3912ca03f2b2b42429174a4f8b3dc84e44
bank1   | LOG: Bank 1: Generated shares: [126, 184, 105, 14, 51, 128, 109, 28, 33, 188, 105, 7, 192, 36, 104, 10, 152, 54, -1525] (sum: 101)
bank1   | LOG: Bank 1: Sent 184 to bank2 on port 6002
bank1   |  * Serving Flask app 'mpc'
bank1   |  * Debug mode: off
bank1   | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank1   |  * Running on all addresses (0.0.0.0)
bank1   |  * Running on http://127.0.0.1:8001
bank1   |  * Running on http://172.18.0.2:8001
bank1   | Press CTRL+C to quit
bank2   | LOG: Bank 2: ======= Starting Process =======
bank2   |  * Serving Flask app 'mpc'
bank2   | LOG: Bank 2: Bank 2 posted commitment: 37834f2f25762f23e1f74a531cbe445db73d6765ebe60878a7dfbecd7d4af6e1
bank2   | LOG: Bank 2: ZKP verification passed for commitment: 37834f2f25762f23e1f74a531cbe445db73d6765ebe60878a7dfbecd7d4af6e1
bank2   | LOG: Bank 2: Generated shares: [87, 14, 123, 108, 201, 53, 188, 159, 118, 178, 187, 28, 192, 147, 26, 202, 133, 102, -2144] (sum: 102)
bank2   | LOG: Bank 2: Sent 87 to bank1 on port 6001
bank2   |  * Debug mode: off
bank2   | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank2   |  * Running on all addresses (0.0.0.0)
bank2   |  * Running on http://127.0.0.1:8002
bank2   |  * Running on http://172.18.0.3:8002
bank2   | Press CTRL+C to quit
bank3   | LOG: Bank 3: ======= Starting Process =======
bank3   | LOG: Bank 3: Bank 3 posted commitment: 454f63ac30c8322997ef025edff6abd23e0dbe7b8a3d5126a894e4a168c1b59b
bank3   | LOG: Bank 3: ZKP verification passed for commitment: 454f63ac30c8322997ef025edff6abd23e0dbe7b8a3d5126a894e4a168c1b59b
bank3   | LOG: Bank 3: Generated shares: [87, 166, 152, 16, 126, 15, 106, 72, 45, 88, 109, 112, 97, 72, 99, 196, 159, 176, -1790] (sum: 103)
bank3   | LOG: Bank 3: Sent 87 to bank1 on port 6001
bank3   |  * Serving Flask app 'mpc'
bank3   |  * Debug mode: off
bank3   | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank3   |  * Running on all addresses (0.0.0.0)
bank3   |  * Running on http://127.0.0.1:8003
bank3   |  * Running on http://172.18.0.4:8003
bank3   | Press CTRL+C to quit
bank4   | LOG: Bank 4: ======= Starting Process =======
bank4   |  * Serving Flask app 'mpc'
bank4   |  * Debug mode: off
bank4   | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank4   |  * Running on all addresses (0.0.0.0)
bank4   |  * Running on http://127.0.0.1:8004
bank4   |  * Running on http://172.18.0.5:8004
bank4   | Press CTRL+C to quit
bank5   | LOG: Bank 5: ======= Starting Process =======
bank5   | LOG: Bank 5: Bank 5 posted commitment: 1253e9373e781b7500266caa55150e08e210bc8cd8cc70d89985e3600155e860
bank5   | LOG: Bank 5: ZKP verification passed for commitment: 1253e9373e781b7500266caa55150e08e210bc8cd8cc70d89985e3600155e860
bank5   | LOG: Bank 5: Generated shares: [47, 206, 110, 161, 52, 33, 189, 172, 56, 112, 47, 139, 86, 167, 7, 45, 66, 106, -1696] (sum: 105)
bank5   | LOG: Bank 5: Sent 47 to bank1 on port 6001
bank5   |  * Serving Flask app 'mpc'
bank5   |  * Debug mode: off
bank5   | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank5   |  * Running on all addresses (0.0.0.0)
bank5   |  * Running on http://127.0.0.1:8005
bank5   |  * Running on http://172.18.0.6:8005
bank5   | Press CTRL+C to quit
bank6   | LOG: Bank 6: ======= Starting Process =======
bank6   | LOG: Bank 6: Bank 6 posted commitment: 482d9673cfee5de391f97fde4d1c84f9f8d6f2cf0784fcffb958b4032de7236c
bank6   | LOG: Bank 6: ZKP verification passed for commitment: 482d9673cfee5de391f97fde4d1c84f9f8d6f2cf0784fcffb958b4032de7236c
bank6   | LOG: Bank 6: Generated shares: [137, 20, 83, 50, 157, 34, 188, 189, 176, 191, 116, 202, 155, 101, 40, 184, 5, 96, -2018] (sum: 106)
bank6   | LOG: Bank 6: Sent 137 to bank1 on port 6001
bank6   |  * Serving Flask app 'mpc'
bank6   |  * Debug mode: off
bank6   | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank6   |  * Running on all addresses (0.0.0.0)
bank6   |  * Running on http://127.0.0.1:8006
bank6   |  * Running on http://172.18.0.7:8006
bank6   | Press CTRL+C to quit
bank7   | LOG: Bank 7: ======= Starting Process =======
bank7   | LOG: Bank 7: Bank 7 posted commitment: 3346f2bbf6c34bd2dbe28bd1bb657d0e9c37392a1d5ec9929e6a5df4763ddc2d
bank7   | LOG: Bank 7: ZKP verification passed for commitment: 3346f2bbf6c34bd2dbe28bd1bb657d0e9c37392a1d5ec9929e6a5df4763ddc2d
bank7   | LOG: Bank 7: Generated shares: [139, 187, 143, 78, 165, 152, 112, 46, 32, 38, 25, 103, 15, 60, 72, 136, 37, 116, -1549] (sum: 107)
bank7   | LOG: Bank 7: Sent 139 to bank1 on port 6001
bank7   |  * Serving Flask app 'mpc'
bank7   |  * Debug mode: off
bank7   | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank7   |  * Running on all addresses (0.0.0.0)
bank7   |  * Running on http://127.0.0.1:8007
bank7   |  * Running on http://172.18.0.8:8007
bank7   | Press CTRL+C to quit
bank8   | LOG: Bank 8: ======= Starting Process =======
bank8   |  * Serving Flask app 'mpc'
bank8   |  * Debug mode: off
bank8   | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank8   |  * Running on all addresses (0.0.0.0)
bank8   |  * Running on http://127.0.0.1:8008
bank8   |  * Running on http://172.18.0.9:8008
bank8   | Press CTRL+C to quit
bank9   | LOG: Bank 9: ======= Starting Process =======
bank9   | LOG: Bank 9: Bank 9 posted commitment: 0fd42b3f73c448b34940b339f87d07adf116b05c0227aad72e8f0ee90533e699
bank9   | LOG: Bank 9: ZKP verification passed for commitment: 0fd42b3f73c448b34940b339f87d07adf116b05c0227aad72e8f0ee90533e699
bank9   | LOG: Bank 9: Generated shares: [87, 1, 113, 119, 158, 13, 198, 63, 30, 122, 183, 11, 78, 165, 2, 8, 213, 160, -1615] (sum: 109)
bank9   | LOG: Bank 9: Sent 87 to bank1 on port 6001
bank9   |  * Serving Flask app 'mpc'
bank9   |  * Debug mode: off
bank9   | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank9   |  * Running on all addresses (0.0.0.0)
bank9   |  * Running on http://127.0.0.1:8009
bank9   |  * Running on http://172.18.0.10:8009
bank9   | Press CTRL+C to quit
bank10  | LOG: Bank 10: ======= Starting Process =======
bank10  | LOG: Bank 10: Bank 10 posted commitment: 9bdb2af6799204a299c603994b8e400e4b1fd625efdb74066cc869fee42c9df3
bank10  | LOG: Bank 10: ZKP verification passed for commitment: 9bdb2af6799204a299c603994b8e400e4b1fd625efdb74066cc869fee42c9df3
bank10  | LOG: Bank 10: Generated shares: [157, 220, 9, 212, 209, 23, 194, 69, 153, 119, 149, 176, 60, 25, 109, 126, 101, 48, -2049] (sum: 110)
bank10  | LOG: Bank 10: Sent 157 to bank1 on port 6001
bank10  |  * Serving Flask app 'mpc'
bank10  |  * Debug mode: off
bank10  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank10  |  * Running on all addresses (0.0.0.0)
bank10  |  * Running on http://127.0.0.1:8010
bank10  |  * Running on http://172.18.0.11:8010
bank10  | Press CTRL+C to quit
bank11  | LOG: Bank 11: ======= Starting Process =======
bank11  |  * Serving Flask app 'mpc'
bank11  |  * Debug mode: off
bank11  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank11  |  * Running on all addresses (0.0.0.0)
bank11  |  * Running on http://127.0.0.1:8011
bank11  |  * Running on http://172.18.0.12:8011
bank11  | Press CTRL+C to quit
bank12  | LOG: Bank 12: ======= Starting Process =======
bank12  |  * Serving Flask app 'mpc'
bank12  | LOG: Bank 12: Bank 12 posted commitment: b1556dea32e9d0cdbfed038fd7787275775ea40939c146a64e205bcb349ad02f
bank12  | LOG: Bank 12: ZKP verification passed for commitment: b1556dea32e9d0cdbfed038fd7787275775ea40939c146a64e205bcb349ad02f
bank12  | LOG: Bank 12: Generated shares: [167, 168, 185, 219, 205, 4, 40, 30, 146, 116, 70, 199, 122, 150, 68, 144, 95, 7, -2023] (sum: 112)
bank12  | LOG: Bank 12: Sent 167 to bank1 on port 6001
bank12  |  * Debug mode: off
bank12  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank12  |  * Running on all addresses (0.0.0.0)
bank12  |  * Running on http://127.0.0.1:8012
bank12  |  * Running on http://172.18.0.13:8012
bank12  | Press CTRL+C to quit
bank13  | LOG: Bank 13: ======= Starting Process =======
bank13  | LOG: Bank 13: Bank 13 posted commitment: 6c658ee83fb7e812482494f3e416a876f63f418a0b8a1f5e76d47ee4177035cb
bank13  | LOG: Bank 13: ZKP verification passed for commitment: 6c658ee83fb7e812482494f3e416a876f63f418a0b8a1f5e76d47ee4177035cb
bank13  | LOG: Bank 13: Generated shares: [123, 38, 53, 185, 58, 51, 31, 160, 70, 201, 122, 22, 148, 155, 62, 160, 107, 97, -1730] (sum: 113)
bank13  | LOG: Bank 13: Sent 123 to bank1 on port 6001
bank13  |  * Serving Flask app 'mpc'
bank13  |  * Debug mode: off
bank13  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank13  |  * Running on all addresses (0.0.0.0)
bank13  |  * Running on http://127.0.0.1:8013
bank13  |  * Running on http://172.18.0.14:8013
bank13  | Press CTRL+C to quit
bank14  | LOG: Bank 14: ======= Starting Process =======
bank14  |  * Serving Flask app 'mpc'
bank14  |  * Debug mode: off
bank14  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank14  |  * Running on all addresses (0.0.0.0)
bank14  |  * Running on http://127.0.0.1:8014
bank14  |  * Running on http://172.18.0.15:8014
bank14  | Press CTRL+C to quit
bank15  | LOG: Bank 15: ======= Starting Process =======
bank15  |  * Serving Flask app 'mpc'
bank15  | LOG: Bank 15: Bank 15 posted commitment: 28dae7c8bde2f3ca608f86d0e16a214dee74c74bee011cdfdd46bc04b655bc14
bank15  | LOG: Bank 15: ZKP verification passed for commitment: 28dae7c8bde2f3ca608f86d0e16a214dee74c74bee011cdfdd46bc04b655bc14
bank15  | LOG: Bank 15: Generated shares: [47, 124, 74, 215, 189, 173, 112, 45, 154, 173, 26, 38, 165, 16, 23, 139, 106, 120, -1824] (sum: 115)
bank15  | LOG: Bank 15: Sent 47 to bank1 on port 6001
bank15  |  * Debug mode: off
bank15  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank15  |  * Running on all addresses (0.0.0.0)
bank15  |  * Running on http://127.0.0.1:8015
bank15  |  * Running on http://172.18.0.16:8015
bank15  | Press CTRL+C to quit
bank16  | LOG: Bank 16: ======= Starting Process =======
bank16  | LOG: Bank 16: Bank 16 posted commitment: e5b861a6d8a966dfca7e7341cd3eb6be9901688d547a72ebed0b1f5e14f3d08d
bank16  | LOG: Bank 16: ZKP verification passed for commitment: e5b861a6d8a966dfca7e7341cd3eb6be9901688d547a72ebed0b1f5e14f3d08d
bank16  | LOG: Bank 16: Generated shares: [51, 25, 71, 159, 87, 59, 53, 124, 89, 115, 158, 142, 68, 214, 86, 104, 195, 29, -1713] (sum: 116)
bank16  | LOG: Bank 16: Sent 51 to bank1 on port 6001
bank16  |  * Serving Flask app 'mpc'
bank16  |  * Debug mode: off
bank16  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank16  |  * Running on all addresses (0.0.0.0)
bank16  |  * Running on http://127.0.0.1:8016
bank16  |  * Running on http://172.18.0.17:8016
bank16  | Press CTRL+C to quit
bank17  | LOG: Bank 17: ======= Starting Process =======
bank17  | LOG: Bank 17: Bank 17 posted commitment: 2ac878b0e2180616993b4b6aa71e61166fdc86c28d47e359d0ee537eb11d46d3
bank17  | LOG: Bank 17: ZKP verification passed for commitment: 2ac878b0e2180616993b4b6aa71e61166fdc86c28d47e359d0ee537eb11d46d3
bank17  | LOG: Bank 17: Generated shares: [169, 2, 52, 174, 67, 6, 199, 169, 190, 169, 152, 26, 228, 142, 27, 134, 19, 197, -2005] (sum: 117)
bank17  | LOG: Bank 17: Sent 169 to bank1 on port 6001
bank17  |  * Serving Flask app 'mpc'
bank17  |  * Debug mode: off
bank17  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank17  |  * Running on all addresses (0.0.0.0)
bank17  |  * Running on http://127.0.0.1:8017
bank17  |  * Running on http://172.18.0.18:8017
bank17  | Press CTRL+C to quit
bank18  | LOG: Bank 18: ======= Starting Process =======
bank18  | LOG: Bank 18: Bank 18 posted commitment: 85daaf6f7055cd5736287faed9603d712920092c4f8fd0097ec3b650bf27530e
bank18  | LOG: Bank 18: ZKP verification passed for commitment: 85daaf6f7055cd5736287faed9603d712920092c4f8fd0097ec3b650bf27530e
bank18  | LOG: Bank 18: Generated shares: [177, 66, 22, 89, 102, 158, 50, 195, 137, 15, 150, 114, 31, 168, 225, 110, 42, 62, -1795] (sum: 118)
bank18  | LOG: Bank 18: Sent 177 to bank1 on port 6001
bank18  |  * Serving Flask app 'mpc'
bank18  |  * Debug mode: off
bank18  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank18  |  * Running on all addresses (0.0.0.0)
bank18  |  * Running on http://127.0.0.1:8018
bank18  |  * Running on http://172.18.0.19:8018
bank18  | Press CTRL+C to quit
bank19  | LOG: Bank 19: ======= Starting Process =======
bank19  | LOG: Bank 19: Bank 19 posted commitment: 3038bfb575bee6a0e61945eff8784835bb2c720634e42734678c083994b7f018
bank19  | LOG: Bank 19: ZKP verification passed for commitment: 3038bfb575bee6a0e61945eff8784835bb2c720634e42734678c083994b7f018
bank19  | LOG: Bank 19: Generated shares: [223, 16, 140, 54, 74, 34, 132, 114, 93, 62, 164, 226, 103, 155, 154, 84, 165, 68, -1942] (sum: 119)
bank19  | LOG: Bank 19: Sent 223 to bank1 on port 6001
bank19  |  * Serving Flask app 'mpc'
bank19  |  * Debug mode: off
bank19  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
bank19  |  * Running on all addresses (0.0.0.0)
bank19  |  * Running on http://127.0.0.1:8019
bank19  |  * Running on http://172.18.0.20:8019
bank19  | Press CTRL+C to quit
bank1   | LOG: Bank 1: Sent 105 to bank3 on port 6003
bank1   | LOG: Bank 1: Sent 14 to bank4 on port 6004
bank1   | LOG: Bank 1: Sent 51 to bank5 on port 6005
bank1   | LOG: Bank 1: Sent 128 to bank6 on port 6006
bank1   | LOG: Bank 1: Sent 109 to bank7 on port 6007
bank1   | LOG: Bank 1: Sent 28 to bank8 on port 6008
bank1   | LOG: Bank 1: Sent 33 to bank9 on port 6009
bank1   | LOG: Bank 1: Sent 188 to bank10 on port 6010
bank1   | LOG: Bank 1: Sent 105 to bank11 on port 6011
bank1   | LOG: Bank 1: Sent 7 to bank12 on port 6012
bank1   | LOG: Bank 1: Sent 192 to bank13 on port 6013
bank1   | LOG: Bank 1: Sent 36 to bank14 on port 6014
bank1   | LOG: Bank 1: Sent 104 to bank15 on port 6015
bank1   | LOG: Bank 1: Sent 10 to bank16 on port 6016
bank1   | LOG: Bank 1: Sent 152 to bank17 on port 6017
bank1   | LOG: Bank 1: Sent 54 to bank18 on port 6018
bank1   | LOG: Bank 1: Sent -1525 to bank19 on port 6019
bank1   | LOG: Bank 1: Received shares: []
bank1   | LOG: Bank 1: Error: Secret sharing failed! -1525 vs 101
bank1   | LOG: Bank 1: Sent 2429 to bank2 on port 7002
bank1   | LOG: Bank 1: Error: Missing commitments in bulletin board!
bank1   | LOG: Bank 1: Final aggregate: -2328, Expected: 2090
bank1   | Traceback (most recent call last):
bank1   |   File "/app/mpc.py", line 485, in <module>
bank1   |     main()
bank1   |   File "/app/mpc.py", line 480, in main
bank1   |     assert final_aggregate == expected
bank1   | AssertionError
bank2   | LOG: Bank 2: Sent 123 to bank3 on port 6003
bank2   | LOG: Bank 2: Sent 108 to bank4 on port 6004
bank2   | LOG: Bank 2: Sent 201 to bank5 on port 6005
bank2   | LOG: Bank 2: Sent 53 to bank6 on port 6006
bank2   | LOG: Bank 2: Sent 188 to bank7 on port 6007
bank2   | LOG: Bank 2: Sent 159 to bank8 on port 6008
bank2   | LOG: Bank 2: Sent 118 to bank9 on port 6009
bank2   | LOG: Bank 2: Sent 178 to bank10 on port 6010
bank2   | LOG: Bank 2: Sent 187 to bank11 on port 6011
bank2   | LOG: Bank 2: Sent 28 to bank12 on port 6012
bank2   | LOG: Bank 2: Sent 192 to bank13 on port 6013
bank2   | LOG: Bank 2: Sent 147 to bank14 on port 6014
bank2   | LOG: Bank 2: Sent 26 to bank15 on port 6015
bank2   | LOG: Bank 2: Sent 202 to bank16 on port 6016
bank2   | LOG: Bank 2: Sent 133 to bank17 on port 6017
bank2   | LOG: Bank 2: Sent 102 to bank18 on port 6018
bank2   | LOG: Bank 2: Sent -2144 to bank19 on port 6019
bank2   | LOG: Bank 2: Received shares: []
bank2   | LOG: Bank 2: Error: Secret sharing failed! -2144 vs 102
bank2   | LOG: Bank 2: Sent 102 to bank3 on port 7003
bank2   | LOG: Bank 2: Error: Missing commitments in bulletin board!
bank2   | LOG: Bank 2: ======= Process Finished =======
bank3   | LOG: Bank 3: Sent 166 to bank2 on port 6002
bank3   | LOG: Bank 3: Sent 16 to bank4 on port 6004
bank3   | LOG: Bank 3: Sent 126 to bank5 on port 6005
bank3   | LOG: Bank 3: Sent 15 to bank6 on port 6006
bank3   | LOG: Bank 3: Sent 106 to bank7 on port 6007
bank3   | LOG: Bank 3: Sent 72 to bank8 on port 6008
bank3   | LOG: Bank 3: Sent 45 to bank9 on port 6009
bank3   | LOG: Bank 3: Sent 88 to bank10 on port 6010
bank3   | LOG: Bank 3: Sent 109 to bank11 on port 6011
bank3   | LOG: Bank 3: Sent 112 to bank12 on port 6012
bank3   | LOG: Bank 3: Sent 97 to bank13 on port 6013
bank3   | LOG: Bank 3: Sent 72 to bank14 on port 6014
bank3   | LOG: Bank 3: Sent 99 to bank15 on port 6015
bank3   | LOG: Bank 3: Sent 196 to bank16 on port 6016
bank3   | LOG: Bank 3: Sent 159 to bank17 on port 6017
bank3   | LOG: Bank 3: Sent 176 to bank18 on port 6018
bank3   | LOG: Bank 3: Sent -1790 to bank19 on port 6019
bank3   | LOG: Bank 3: Received shares: []
bank3   | LOG: Bank 3: Error: Secret sharing failed! -1790 vs 103
bank3   | LOG: Bank 3: Sent 103 to bank4 on port 7004
bank3   | LOG: Bank 3: Error: Missing commitments in bulletin board!
bank3   | LOG: Bank 3: ======= Process Finished =======
bank4   | LOG: Bank 4: Bank 4 posted commitment: 5ef6fdf32513aa7cd11f72beccf132b9224d33f271471fff402742887a171edf
bank4   | LOG: Bank 4: ZKP verification passed for commitment: 5ef6fdf32513aa7cd11f72beccf132b9224d33f271471fff402742887a171edf
bank4   | LOG: Bank 4: Generated shares: [22, 17, 79, 35, 201, 64, 144, 116, 206, 17, 142, 29, 151, 16, 14, 197, 196, 27, -1569] (sum: 104)
bank4   | LOG: Bank 4: Sent 22 to bank1 on port 6001
bank4   | LOG: Bank 4: Sent 17 to bank2 on port 6002
bank4   | LOG: Bank 4: Sent 79 to bank3 on port 6003
bank4   | LOG: Bank 4: Sent 201 to bank5 on port 6005
bank4   | LOG: Bank 4: Sent 64 to bank6 on port 6006
bank4   | LOG: Bank 4: Sent 144 to bank7 on port 6007
bank4   | LOG: Bank 4: Sent 116 to bank8 on port 6008
bank4   | LOG: Bank 4: Sent 206 to bank9 on port 6009
bank4   | LOG: Bank 4: Sent 17 to bank10 on port 6010
bank4   | LOG: Bank 4: Sent 142 to bank11 on port 6011
bank4   | LOG: Bank 4: Sent 29 to bank12 on port 6012
bank4   | LOG: Bank 4: Sent 151 to bank13 on port 6013
bank4   | LOG: Bank 4: Sent 16 to bank14 on port 6014
bank4   | LOG: Bank 4: Sent 14 to bank15 on port 6015
bank4   | LOG: Bank 4: Sent 197 to bank16 on port 6016
bank4   | LOG: Bank 4: Sent 196 to bank17 on port 6017
bank4   | LOG: Bank 4: Sent 27 to bank18 on port 6018
bank4   | LOG: Bank 4: Sent -1569 to bank19 on port 6019
bank4   | LOG: Bank 4: Received shares: []
bank4   | LOG: Bank 4: Error: Secret sharing failed! -1569 vs 104
bank4   | LOG: Bank 4: Sent 104 to bank5 on port 7005
bank4   | LOG: Bank 4: Error: Missing commitments in bulletin board!
bank4   | LOG: Bank 4: ======= Process Finished =======
bank5   | LOG: Bank 5: Sent 206 to bank2 on port 6002
bank5   | LOG: Bank 5: Sent 110 to bank3 on port 6003
bank5   | LOG: Bank 5: Sent 161 to bank4 on port 6004
bank5   | LOG: Bank 5: Sent 33 to bank6 on port 6006
bank5   | LOG: Bank 5: Sent 189 to bank7 on port 6007
bank5   | LOG: Bank 5: Sent 172 to bank8 on port 6008
bank5   | LOG: Bank 5: Sent 56 to bank9 on port 6009
bank5   | LOG: Bank 5: Sent 112 to bank10 on port 6010
bank5   | LOG: Bank 5: Sent 47 to bank11 on port 6011
bank5   | LOG: Bank 5: Sent 139 to bank12 on port 6012
bank5   | LOG: Bank 5: Sent 86 to bank13 on port 6013
bank5   | LOG: Bank 5: Sent 167 to bank14 on port 6014
bank5   | LOG: Bank 5: Sent 7 to bank15 on port 6015
bank5   | LOG: Bank 5: Sent 45 to bank16 on port 6016
bank5   | LOG: Bank 5: Sent 66 to bank17 on port 6017
bank5   | LOG: Bank 5: Sent 106 to bank18 on port 6018
bank5   | LOG: Bank 5: Sent -1696 to bank19 on port 6019
bank5   | LOG: Bank 5: Received shares: []
bank5   | LOG: Bank 5: Error: Secret sharing failed! -1696 vs 105
bank5   | LOG: Bank 5: Sent 105 to bank6 on port 7006
bank5   | LOG: Bank 5: Error: Missing commitments in bulletin board!
bank5   | LOG: Bank 5: ======= Process Finished =======
bank1 exited with code 1
bank6   | LOG: Bank 6: Sent 20 to bank2 on port 6002
bank6   | LOG: Bank 6: Sent 83 to bank3 on port 6003
bank6   | LOG: Bank 6: Sent 50 to bank4 on port 6004
bank6   | LOG: Bank 6: Sent 157 to bank5 on port 6005
bank6   | LOG: Bank 6: Sent 188 to bank7 on port 6007
bank6   | LOG: Bank 6: Sent 189 to bank8 on port 6008
bank6   | LOG: Bank 6: Sent 176 to bank9 on port 6009
bank6   | LOG: Bank 6: Sent 191 to bank10 on port 6010
bank6   | LOG: Bank 6: Sent 116 to bank11 on port 6011
bank6   | LOG: Bank 6: Sent 202 to bank12 on port 6012
bank6   | LOG: Bank 6: Sent 155 to bank13 on port 6013
bank6   | LOG: Bank 6: Sent 101 to bank14 on port 6014
bank6   | LOG: Bank 6: Sent 40 to bank15 on port 6015
bank6   | LOG: Bank 6: Sent 184 to bank16 on port 6016
bank6   | LOG: Bank 6: Sent 5 to bank17 on port 6017
bank6   | LOG: Bank 6: Sent 96 to bank18 on port 6018
bank6   | LOG: Bank 6: Sent -2018 to bank19 on port 6019
bank6   | LOG: Bank 6: Received shares: []
bank6   | LOG: Bank 6: Error: Secret sharing failed! -2018 vs 106
bank6   | LOG: Bank 6: Sent 106 to bank7 on port 7007
bank6   | LOG: Bank 6: Error: Missing commitments in bulletin board!
bank6   | LOG: Bank 6: ======= Process Finished =======
bank2 exited with code 0
bank7   | LOG: Bank 7: Sent 187 to bank2 on port 6002
bank7   | LOG: Bank 7: Sent 143 to bank3 on port 6003
bank7   | LOG: Bank 7: Sent 78 to bank4 on port 6004
bank7   | LOG: Bank 7: Sent 165 to bank5 on port 6005
bank7   | LOG: Bank 7: Sent 152 to bank6 on port 6006
bank7   | LOG: Bank 7: Sent 46 to bank8 on port 6008
bank7   | LOG: Bank 7: Sent 32 to bank9 on port 6009
bank7   | LOG: Bank 7: Sent 38 to bank10 on port 6010
bank7   | LOG: Bank 7: Sent 25 to bank11 on port 6011
bank7   | LOG: Bank 7: Sent 103 to bank12 on port 6012
bank7   | LOG: Bank 7: Sent 15 to bank13 on port 6013
bank7   | LOG: Bank 7: Sent 60 to bank14 on port 6014
bank7   | LOG: Bank 7: Sent 72 to bank15 on port 6015
bank7   | LOG: Bank 7: Sent 136 to bank16 on port 6016
bank7   | LOG: Bank 7: Sent 37 to bank17 on port 6017
bank7   | LOG: Bank 7: Sent 116 to bank18 on port 6018
bank7   | LOG: Bank 7: Sent -1549 to bank19 on port 6019
bank7   | LOG: Bank 7: Received shares: []
bank7   | LOG: Bank 7: Error: Secret sharing failed! -1549 vs 107
bank7   | LOG: Bank 7: Sent 107 to bank8 on port 7008
bank7   | LOG: Bank 7: Error: Missing commitments in bulletin board!
bank7   | LOG: Bank 7: ======= Process Finished =======
bank3 exited with code 0
bank8   | LOG: Bank 8: Bank 8 posted commitment: 9537f32ec7599e1ae953af6c9f929fe747ff9dadf79a9beff1f304c550173011
bank8   | LOG: Bank 8: ZKP verification passed for commitment: 9537f32ec7599e1ae953af6c9f929fe747ff9dadf79a9beff1f304c550173011
bank8   | LOG: Bank 8: Generated shares: [34, 171, 113, 193, 214, 113, 206, 211, 29, 75, 124, 186, 200, 30, 145, 129, 32, 132, -2229] (sum: 108)
bank8   | LOG: Bank 8: Sent 34 to bank1 on port 6001
bank8   | LOG: Bank 8: Sent 171 to bank2 on port 6002
bank8   | LOG: Bank 8: Sent 113 to bank3 on port 6003
bank8   | LOG: Bank 8: Sent 193 to bank4 on port 6004
bank8   | LOG: Bank 8: Sent 214 to bank5 on port 6005
bank8   | LOG: Bank 8: Sent 113 to bank6 on port 6006
bank8   | LOG: Bank 8: Sent 206 to bank7 on port 6007
bank8   | LOG: Bank 8: Sent 29 to bank9 on port 6009
bank8   | LOG: Bank 8: Sent 75 to bank10 on port 6010
bank8   | LOG: Bank 8: Sent 124 to bank11 on port 6011
bank8   | LOG: Bank 8: Sent 186 to bank12 on port 6012
bank8   | LOG: Bank 8: Sent 200 to bank13 on port 6013
bank8   | LOG: Bank 8: Sent 30 to bank14 on port 6014
bank8   | LOG: Bank 8: Sent 145 to bank15 on port 6015
bank8   | LOG: Bank 8: Sent 129 to bank16 on port 6016
bank8   | LOG: Bank 8: Sent 32 to bank17 on port 6017
bank8   | LOG: Bank 8: Sent 132 to bank18 on port 6018
bank8   | LOG: Bank 8: Sent -2229 to bank19 on port 6019
bank8   | LOG: Bank 8: Received shares: []
bank8   | LOG: Bank 8: Error: Secret sharing failed! -2229 vs 108
bank8   | LOG: Bank 8: Sent 108 to bank9 on port 7009
bank8   | LOG: Bank 8: Error: Missing commitments in bulletin board!
bank8   | LOG: Bank 8: ======= Process Finished =======
bank4 exited with code 0
bank9   | LOG: Bank 9: Sent 1 to bank2 on port 6002
bank9   | LOG: Bank 9: Sent 113 to bank3 on port 6003
bank9   | LOG: Bank 9: Sent 119 to bank4 on port 6004
bank9   | LOG: Bank 9: Sent 158 to bank5 on port 6005
bank9   | LOG: Bank 9: Sent 13 to bank6 on port 6006
bank9   | LOG: Bank 9: Sent 198 to bank7 on port 6007
bank9   | LOG: Bank 9: Sent 63 to bank8 on port 6008
bank9   | LOG: Bank 9: Sent 122 to bank10 on port 6010
bank9   | LOG: Bank 9: Sent 183 to bank11 on port 6011
bank9   | LOG: Bank 9: Sent 11 to bank12 on port 6012
bank9   | LOG: Bank 9: Sent 78 to bank13 on port 6013
bank9   | LOG: Bank 9: Sent 165 to bank14 on port 6014
bank9   | LOG: Bank 9: Sent 2 to bank15 on port 6015
bank9   | LOG: Bank 9: Sent 8 to bank16 on port 6016
bank9   | LOG: Bank 9: Sent 213 to bank17 on port 6017
bank9   | LOG: Bank 9: Sent 160 to bank18 on port 6018
bank9   | LOG: Bank 9: Sent -1615 to bank19 on port 6019
bank9   | LOG: Bank 9: Received shares: []
bank9   | LOG: Bank 9: Error: Secret sharing failed! -1615 vs 109
bank9   | LOG: Bank 9: Sent 109 to bank10 on port 7010
bank9   | LOG: Bank 9: Error: Missing commitments in bulletin board!
bank9   | LOG: Bank 9: ======= Process Finished =======
bank10  | LOG: Bank 10: Sent 220 to bank2 on port 6002
bank10  | LOG: Bank 10: Sent 9 to bank3 on port 6003
bank10  | LOG: Bank 10: Sent 212 to bank4 on port 6004
bank10  | LOG: Bank 10: Sent 209 to bank5 on port 6005
bank10  | LOG: Bank 10: Sent 23 to bank6 on port 6006
bank10  | LOG: Bank 10: Sent 194 to bank7 on port 6007
bank10  | LOG: Bank 10: Sent 69 to bank8 on port 6008
bank10  | LOG: Bank 10: Sent 153 to bank9 on port 6009
bank10  | LOG: Bank 10: Sent 149 to bank11 on port 6011
bank10  | LOG: Bank 10: Sent 176 to bank12 on port 6012
bank10  | LOG: Bank 10: Sent 60 to bank13 on port 6013
bank10  | LOG: Bank 10: Sent 25 to bank14 on port 6014
bank10  | LOG: Bank 10: Sent 109 to bank15 on port 6015
bank10  | LOG: Bank 10: Sent 126 to bank16 on port 6016
bank10  | LOG: Bank 10: Sent 101 to bank17 on port 6017
bank10  | LOG: Bank 10: Sent 48 to bank18 on port 6018
bank10  | LOG: Bank 10: Sent -2049 to bank19 on port 6019
bank10  | LOG: Bank 10: Received shares: []
bank10  | LOG: Bank 10: Error: Secret sharing failed! -2049 vs 110
bank10  | LOG: Bank 10: Sent 110 to bank11 on port 7011
bank10  | LOG: Bank 10: Error: Missing commitments in bulletin board!
bank10  | LOG: Bank 10: ======= Process Finished =======
bank5 exited with code 0
bank6 exited with code 0
bank11  | LOG: Bank 11: Bank 11 posted commitment: f6e0a1e2ac41945a9aa7ff8a8aaa0cebc12a3bcc981a929ad5cf810a090e11ae
bank11  | LOG: Bank 11: ZKP verification passed for commitment: f6e0a1e2ac41945a9aa7ff8a8aaa0cebc12a3bcc981a929ad5cf810a090e11ae
bank11  | LOG: Bank 11: Generated shares: [148, 51, 6, 63, 107, 183, 210, 152, 57, 78, 87, 129, 194, 126, 59, 181, 20, 134, -1874] (sum: 111)
bank11  | LOG: Bank 11: Sent 148 to bank1 on port 6001
bank11  | LOG: Bank 11: Sent 51 to bank2 on port 6002
bank11  | LOG: Bank 11: Sent 6 to bank3 on port 6003
bank11  | LOG: Bank 11: Sent 63 to bank4 on port 6004
bank11  | LOG: Bank 11: Sent 107 to bank5 on port 6005
bank11  | LOG: Bank 11: Sent 183 to bank6 on port 6006
bank11  | LOG: Bank 11: Sent 210 to bank7 on port 6007
bank11  | LOG: Bank 11: Sent 152 to bank8 on port 6008
bank11  | LOG: Bank 11: Sent 57 to bank9 on port 6009
bank11  | LOG: Bank 11: Sent 78 to bank10 on port 6010
bank11  | LOG: Bank 11: Sent 129 to bank12 on port 6012
bank11  | LOG: Bank 11: Sent 194 to bank13 on port 6013
bank11  | LOG: Bank 11: Sent 126 to bank14 on port 6014
bank11  | LOG: Bank 11: Sent 59 to bank15 on port 6015
bank11  | LOG: Bank 11: Sent 181 to bank16 on port 6016
bank11  | LOG: Bank 11: Sent 20 to bank17 on port 6017
bank11  | LOG: Bank 11: Sent 134 to bank18 on port 6018
bank11  | LOG: Bank 11: Sent -1874 to bank19 on port 6019
bank11  | LOG: Bank 11: Received shares: []
bank11  | LOG: Bank 11: Error: Secret sharing failed! -1874 vs 111
bank11  | LOG: Bank 11: Sent 111 to bank12 on port 7012
bank11  | LOG: Bank 11: Error: Missing commitments in bulletin board!
bank11  | LOG: Bank 11: ======= Process Finished =======
bank12  | LOG: Bank 12: Sent 168 to bank2 on port 6002
bank12  | LOG: Bank 12: Sent 185 to bank3 on port 6003
bank12  | LOG: Bank 12: Sent 219 to bank4 on port 6004
bank12  | LOG: Bank 12: Sent 205 to bank5 on port 6005
bank12  | LOG: Bank 12: Sent 4 to bank6 on port 6006
bank12  | LOG: Bank 12: Sent 40 to bank7 on port 6007
bank12  | LOG: Bank 12: Sent 30 to bank8 on port 6008
bank12  | LOG: Bank 12: Sent 146 to bank9 on port 6009
bank12  | LOG: Bank 12: Sent 116 to bank10 on port 6010
bank12  | LOG: Bank 12: Sent 70 to bank11 on port 6011
bank12  | LOG: Bank 12: Sent 122 to bank13 on port 6013
bank12  | LOG: Bank 12: Sent 150 to bank14 on port 6014
bank12  | LOG: Bank 12: Sent 68 to bank15 on port 6015
bank12  | LOG: Bank 12: Sent 144 to bank16 on port 6016
bank12  | LOG: Bank 12: Sent 95 to bank17 on port 6017
bank12  | LOG: Bank 12: Sent 7 to bank18 on port 6018
bank12  | LOG: Bank 12: Sent -2023 to bank19 on port 6019
bank12  | LOG: Bank 12: Received shares: []
bank12  | LOG: Bank 12: Error: Secret sharing failed! -2023 vs 112
bank12  | LOG: Bank 12: Sent 112 to bank13 on port 7013
bank12  | LOG: Bank 12: Error: Missing commitments in bulletin board!
bank12  | LOG: Bank 12: ======= Process Finished =======
bank7 exited with code 0
bank13  | LOG: Bank 13: Sent 38 to bank2 on port 6002
bank13  | LOG: Bank 13: Sent 53 to bank3 on port 6003
bank13  | LOG: Bank 13: Sent 185 to bank4 on port 6004
bank13  | LOG: Bank 13: Sent 58 to bank5 on port 6005
bank13  | LOG: Bank 13: Sent 51 to bank6 on port 6006
bank13  | LOG: Bank 13: Sent 31 to bank7 on port 6007
bank13  | LOG: Bank 13: Sent 160 to bank8 on port 6008
bank13  | LOG: Bank 13: Sent 70 to bank9 on port 6009
bank13  | LOG: Bank 13: Sent 201 to bank10 on port 6010
bank13  | LOG: Bank 13: Sent 122 to bank11 on port 6011
bank13  | LOG: Bank 13: Sent 22 to bank12 on port 6012
bank13  | LOG: Bank 13: Sent 155 to bank14 on port 6014
bank13  | LOG: Bank 13: Sent 62 to bank15 on port 6015
bank13  | LOG: Bank 13: Sent 160 to bank16 on port 6016
bank13  | LOG: Bank 13: Sent 107 to bank17 on port 6017
bank13  | LOG: Bank 13: Sent 97 to bank18 on port 6018
bank13  | LOG: Bank 13: Sent -1730 to bank19 on port 6019
bank13  | LOG: Bank 13: Received shares: []
bank13  | LOG: Bank 13: Error: Secret sharing failed! -1730 vs 113
bank13  | LOG: Bank 13: Sent 113 to bank14 on port 7014
bank13  | LOG: Bank 13: Error: Missing commitments in bulletin board!
bank13  | LOG: Bank 13: ======= Process Finished =======
bank8 exited with code 0
bank14  | LOG: Bank 14: Bank 14 posted commitment: 9f1f9dce319c4700ef28ec8c53bd3cc8e6abe64c68385479ab89215806a5bdd6
bank14  | LOG: Bank 14: ZKP verification passed for commitment: 9f1f9dce319c4700ef28ec8c53bd3cc8e6abe64c68385479ab89215806a5bdd6
bank14  | LOG: Bank 14: Generated shares: [51, 50, 111, 62, 123, 139, 98, 209, 126, 85, 219, 161, 63, 59, 143, 129, 139, 179, -2032] (sum: 114)
bank14  | LOG: Bank 14: Sent 51 to bank1 on port 6001
bank14  | LOG: Bank 14: Sent 50 to bank2 on port 6002
bank14  | LOG: Bank 14: Sent 111 to bank3 on port 6003
bank14  | LOG: Bank 14: Sent 62 to bank4 on port 6004
bank14  | LOG: Bank 14: Sent 123 to bank5 on port 6005
bank14  | LOG: Bank 14: Sent 139 to bank6 on port 6006
bank14  | LOG: Bank 14: Sent 98 to bank7 on port 6007
bank14  | LOG: Bank 14: Sent 209 to bank8 on port 6008
bank14  | LOG: Bank 14: Sent 126 to bank9 on port 6009
bank14  | LOG: Bank 14: Sent 85 to bank10 on port 6010
bank14  | LOG: Bank 14: Sent 219 to bank11 on port 6011
bank14  | LOG: Bank 14: Sent 161 to bank12 on port 6012
bank14  | LOG: Bank 14: Sent 63 to bank13 on port 6013
bank14  | LOG: Bank 14: Sent 143 to bank15 on port 6015
bank14  | LOG: Bank 14: Sent 129 to bank16 on port 6016
bank14  | LOG: Bank 14: Sent 139 to bank17 on port 6017
bank14  | LOG: Bank 14: Sent 179 to bank18 on port 6018
bank14  | LOG: Bank 14: Sent -2032 to bank19 on port 6019
bank14  | LOG: Bank 14: Received shares: []
bank14  | LOG: Bank 14: Error: Secret sharing failed! -2032 vs 114
bank14  | LOG: Bank 14: Sent 114 to bank15 on port 7015
bank14  | LOG: Bank 14: Error: Missing commitments in bulletin board!
bank14  | LOG: Bank 14: ======= Process Finished =======
bank9 exited with code 0
bank15  | LOG: Bank 15: Sent 124 to bank2 on port 6002
bank15  | LOG: Bank 15: Sent 74 to bank3 on port 6003
bank15  | LOG: Bank 15: Sent 215 to bank4 on port 6004
bank15  | LOG: Bank 15: Sent 189 to bank5 on port 6005
bank15  | LOG: Bank 15: Sent 173 to bank6 on port 6006
bank15  | LOG: Bank 15: Sent 112 to bank7 on port 6007
bank15  | LOG: Bank 15: Sent 45 to bank8 on port 6008
bank15  | LOG: Bank 15: Sent 154 to bank9 on port 6009
bank15  | LOG: Bank 15: Sent 173 to bank10 on port 6010
bank15  | LOG: Bank 15: Sent 26 to bank11 on port 6011
bank15  | LOG: Bank 15: Sent 38 to bank12 on port 6012
bank15  | LOG: Bank 15: Sent 165 to bank13 on port 6013
bank15  | LOG: Bank 15: Sent 16 to bank14 on port 6014
bank15  | LOG: Bank 15: Sent 139 to bank16 on port 6016
bank15  | LOG: Bank 15: Sent 106 to bank17 on port 6017
bank15  | LOG: Bank 15: Sent 120 to bank18 on port 6018
bank15  | LOG: Bank 15: Sent -1824 to bank19 on port 6019
bank15  | LOG: Bank 15: Received shares: []
bank15  | LOG: Bank 15: Error: Secret sharing failed! -1824 vs 115
bank15  | LOG: Bank 15: Sent 115 to bank16 on port 7016
bank15  | LOG: Bank 15: Error: Missing commitments in bulletin board!
bank15  | LOG: Bank 15: ======= Process Finished =======
bank10 exited with code 0
bank16  | LOG: Bank 16: Sent 25 to bank2 on port 6002
bank16  | LOG: Bank 16: Sent 71 to bank3 on port 6003
bank16  | LOG: Bank 16: Sent 159 to bank4 on port 6004
bank16  | LOG: Bank 16: Sent 87 to bank5 on port 6005
bank16  | LOG: Bank 16: Sent 59 to bank6 on port 6006
bank16  | LOG: Bank 16: Sent 53 to bank7 on port 6007
bank16  | LOG: Bank 16: Sent 124 to bank8 on port 6008
bank16  | LOG: Bank 16: Sent 89 to bank9 on port 6009
bank16  | LOG: Bank 16: Sent 115 to bank10 on port 6010
bank16  | LOG: Bank 16: Sent 158 to bank11 on port 6011
bank16  | LOG: Bank 16: Sent 142 to bank12 on port 6012
bank16  | LOG: Bank 16: Sent 68 to bank13 on port 6013
bank16  | LOG: Bank 16: Sent 214 to bank14 on port 6014
bank16  | LOG: Bank 16: Sent 86 to bank15 on port 6015
bank16  | LOG: Bank 16: Sent 195 to bank17 on port 6017
bank16  | LOG: Bank 16: Sent 29 to bank18 on port 6018
bank16  | LOG: Bank 16: Sent -1713 to bank19 on port 6019
bank16  | LOG: Bank 16: Received shares: []
bank16  | LOG: Bank 16: Error: Secret sharing failed! -1713 vs 116
bank16  | LOG: Bank 16: Sent 116 to bank17 on port 7017
bank16  | LOG: Bank 16: Error: Missing commitments in bulletin board!
bank16  | LOG: Bank 16: ======= Process Finished =======
bank17  | LOG: Bank 17: Sent 2 to bank2 on port 6002
bank17  | LOG: Bank 17: Sent 52 to bank3 on port 6003
bank17  | LOG: Bank 17: Sent 174 to bank4 on port 6004
bank17  | LOG: Bank 17: Sent 67 to bank5 on port 6005
bank17  | LOG: Bank 17: Sent 6 to bank6 on port 6006
bank17  | LOG: Bank 17: Sent 199 to bank7 on port 6007
bank17  | LOG: Bank 17: Sent 169 to bank8 on port 6008
bank17  | LOG: Bank 17: Sent 190 to bank9 on port 6009
bank17  | LOG: Bank 17: Sent 169 to bank10 on port 6010
bank17  | LOG: Bank 17: Sent 152 to bank11 on port 6011
bank17  | LOG: Bank 17: Sent 26 to bank12 on port 6012
bank17  | LOG: Bank 17: Sent 228 to bank13 on port 6013
bank17  | LOG: Bank 17: Sent 142 to bank14 on port 6014
bank17  | LOG: Bank 17: Sent 27 to bank15 on port 6015
bank17  | LOG: Bank 17: Sent 134 to bank16 on port 6016
bank17  | LOG: Bank 17: Sent 197 to bank18 on port 6018
bank17  | LOG: Bank 17: Sent -2005 to bank19 on port 6019
bank17  | LOG: Bank 17: Received shares: []
bank17  | LOG: Bank 17: Error: Secret sharing failed! -2005 vs 117
bank17  | LOG: Bank 17: Sent 117 to bank18 on port 7018
bank17  | LOG: Bank 17: Error: Missing commitments in bulletin board!
bank17  | LOG: Bank 17: ======= Process Finished =======
bank11 exited with code 0
bank18  | LOG: Bank 18: Sent 66 to bank2 on port 6002
bank18  | LOG: Bank 18: Sent 22 to bank3 on port 6003
bank18  | LOG: Bank 18: Sent 89 to bank4 on port 6004
bank18  | LOG: Bank 18: Sent 102 to bank5 on port 6005
bank18  | LOG: Bank 18: Sent 158 to bank6 on port 6006
bank18  | LOG: Bank 18: Sent 50 to bank7 on port 6007
bank18  | LOG: Bank 18: Sent 195 to bank8 on port 6008
bank18  | LOG: Bank 18: Sent 137 to bank9 on port 6009
bank18  | LOG: Bank 18: Sent 15 to bank10 on port 6010
bank18  | LOG: Bank 18: Sent 150 to bank11 on port 6011
bank18  | LOG: Bank 18: Sent 114 to bank12 on port 6012
bank18  | LOG: Bank 18: Sent 31 to bank13 on port 6013
bank18  | LOG: Bank 18: Sent 168 to bank14 on port 6014
bank18  | LOG: Bank 18: Sent 225 to bank15 on port 6015
bank18  | LOG: Bank 18: Sent 110 to bank16 on port 6016
bank18  | LOG: Bank 18: Sent 42 to bank17 on port 6017
bank18  | LOG: Bank 18: Sent -1795 to bank19 on port 6019
bank18  | LOG: Bank 18: Received shares: []
bank18  | LOG: Bank 18: Error: Secret sharing failed! -1795 vs 118
bank18  | LOG: Bank 18: Sent 118 to bank19 on port 7019
bank18  | LOG: Bank 18: Error: Missing commitments in bulletin board!
bank18  | LOG: Bank 18: ======= Process Finished =======
bank12 exited with code 0
bank19  | LOG: Bank 19: Sent 16 to bank2 on port 6002
bank19  | LOG: Bank 19: Sent 140 to bank3 on port 6003
bank19  | LOG: Bank 19: Sent 54 to bank4 on port 6004
bank19  | LOG: Bank 19: Sent 74 to bank5 on port 6005
bank19  | LOG: Bank 19: Sent 34 to bank6 on port 6006
bank19  | LOG: Bank 19: Sent 132 to bank7 on port 6007
bank19  | LOG: Bank 19: Sent 114 to bank8 on port 6008
bank19  | LOG: Bank 19: Sent 93 to bank9 on port 6009
bank19  | LOG: Bank 19: Sent 62 to bank10 on port 6010
bank19  | LOG: Bank 19: Sent 164 to bank11 on port 6011
bank19  | LOG: Bank 19: Sent 226 to bank12 on port 6012
bank19  | LOG: Bank 19: Sent 103 to bank13 on port 6013
bank19  | LOG: Bank 19: Sent 155 to bank14 on port 6014
bank19  | LOG: Bank 19: Sent 154 to bank15 on port 6015
bank19  | LOG: Bank 19: Sent 84 to bank16 on port 6016
bank19  | LOG: Bank 19: Sent 165 to bank17 on port 6017
bank19  | LOG: Bank 19: Sent 68 to bank18 on port 6018
bank19  | LOG: Bank 19: Received shares: []
bank19  | LOG: Bank 19: Error: Secret sharing failed! -1942 vs 119
bank19  | LOG: Bank 19: Sent 119 to bank1 on port 5001
bank19  | LOG: Bank 19: Error: Missing commitments in bulletin board!
bank19  | LOG: Bank 19: ======= Process Finished =======
bank13 exited with code 0
bank14 exited with code 0
bank15 exited with code 0
bank16 exited with code 0
bank17 exited with code 0
bank18 exited with code 0
bank19 exited with code 0
```