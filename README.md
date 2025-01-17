# Description

Creates a sqlite db from zeek logs

# Installation

`pip install zeek_to_sqlite`

# Usage

**From command line:**

`python -m zeek_to_sqlite [-h] [--name NAME] --path PATH [--result RESULT] [--separator SEPARATOR]`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--name | -n | String | zeek.db | Name of the sqlite database written to result |
|--path | -p | String | - | Path to folder where the zeek logs are located |
|--result | -r | String | .\zeek-sqlite | Directory to write the resulting sqlite db |
|--separator | -s | String | \t | The separator used in zeek files |


# Example

The following command reads the zeek logs located in `./zeek` and creates a sqlite db with
the name `zeek-logs.db` under `./zeek-sqlite-db`

`python -m zeek_to_sqlite -p ./zeek -n zeek-logs.db -r ./zeek-sqlite-db`

Result:

```
################################################################################

zeek_to_sqlite by 5f0
Converts zeek logs into a sqlite database

Current working directory: path/to/dir

Datetime: 01/01/1970 10:20:30

################################################################################

            Separator: 
Location of zeek logs: ./zeek
Location of sqlite db: ./zeek-sqlite-db/zeek-logs.db

---

File to convert: ./zeek/conn.log
Table Name: conn
Columns: ['ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p', 'proto', 'service', 'duration', 'orig_bytes', 'resp_bytes', 'conn_state', 'local_orig', 'local_resp', 'missed_bytes', 'history', 'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', 'tunnel_parents']
Inserted rows: 193411

---

[other zeek logs]

---

################################################################################

Execution Time: 3.464370 sec
```


# License

MIT