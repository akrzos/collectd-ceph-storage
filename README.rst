Collectd Ceph Storage
=====================

Yet another Ceph Collectd Plugin in Python


Overview
--------

This plugin issues commands against Ceph in order to obtain valuable metrics
regarding the performance and health of your Ceph cluster.

Sample Graphs
-------------

.. figure:: https://github.com/akrzos/collectd-ceph-storage/blob/master/sample-dashboard-1.png
  :alt: Sample Graphs

.. figure:: https://github.com/akrzos/collectd-ceph-storage/blob/master/sample-dashboard-2.png
  :alt: Sample Graphs

Metrics
-------
| collectd-ceph-storage-cluster/gauge-total_avail
| collectd-ceph-storage-cluster/gauge-total_space
| collectd-ceph-storage-cluster/gauge-total_used
| collectd-ceph-storage-mon/gauge-number
| collectd-ceph-storage-mon/gauge-quorum
| collectd-ceph-storage-osd-(*)/gauge-apply_latency_ms
| collectd-ceph-storage-osd-(*)/gauge-commit_latency_ms
| collectd-ceph-storage-osd-(*)/gauge-kb_total
| collectd-ceph-storage-osd-(*)/gauge-kb_used
| collectd-ceph-storage-osd-(*)/gauge-num_snap_trimming
| collectd-ceph-storage-osd-(*)/gauge-snap_trim_queue_len
| collectd-ceph-storage-osd/gauge-down
| collectd-ceph-storage-osd/gauge-in
| collectd-ceph-storage-osd/gauge-out
| collectd-ceph-storage-osd/gauge-up
| collectd-ceph-storage-pg/gauge-active
| collectd-ceph-storage-pg/gauge-clean
| collectd-ceph-storage-pg/gauge-scrubbing
| collectd-ceph-storage-pool-(pool name)/gauge-bytes_used
| collectd-ceph-storage-pool-(pool name)/gauge-kb_used
| collectd-ceph-storage-pool-(pool name)/gauge-objects
| collectd-ceph-storage-pool-(pool name)/gauge-pg_num
| collectd-ceph-storage-pool-(pool name)/gauge-pgp_num
| collectd-ceph-storage-pool-(pool name)/gauge-read_bytes_sec
| collectd-ceph-storage-pool-(pool name)/gauge-read_op_per_sec
| collectd-ceph-storage-pool-(pool name)/gauge-size
| collectd-ceph-storage-pool-(pool name)/gauge-write_bytes_sec
| collectd-ceph-storage-pool-(pool name)/gauge-write_op_per_sec
| collectd-ceph-storage-pool/gauge-number
