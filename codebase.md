draw a flow chart for ai_hub code base and process

1. generate all the model for all 3 SP (QNN and Tflite) through axiom playlist
2. run the use case or plylist and result will strore is excel sheet .csv (test case name, time, meta info,imsdk version,FPS, Inf time, accuracy, framedrop, utilization(CPU,GPU,NPU).
3. push the data into influxDB schima inside table.
4. visulize the data in graphana dashboard.

+-----------------------------+
| Generate Models via Axiom  |
| Playlist for all 3 SPs     |
| (QNN, TFLite)              |
+-------------+-------------+
              |
              v
+-----------------------------+
| Run Use Case or Playlist   |
| & Collect Results          |
+-------------+-------------+
              |
              v
+-----------------------------+
| Store Results in CSV File  |
| (Testcase, Time, FPS, etc.)|
+-------------+-------------+
              |
              v
+-----------------------------+
| Push Data to InfluxDB      |
| (Write to Schema/Table)    |
+-------------+-------------+
              |
              v
+-----------------------------+
| Visualize Data in Grafana  |
| Dashboard (Charts/Graphs)  |
+-----------------------------+
