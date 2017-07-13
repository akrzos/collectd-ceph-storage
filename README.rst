Collectd Ceph Storage
=====================

|collectd-ceph-storage|

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

Install / Configuration
-----------------------

1. Assuming you have collectd installed already, append the following
   plugin details to your collectd.conf config file.  Adjust the
   configuration items as you see fit.  The plugin must be able to
   subprocess the ceph and rados commands.

   ::

       ```
       <LoadPlugin python>
         Globals true
       </LoadPlugin>

       <Plugin python>
         LogTraces true
         Interactive false
         Import "collectd_ceph_storage"
         <Module collectd_ceph_storage>
           CephCluster "ceph"

           CephRadosBench False
           CephRadosBenchInterval 60
           CephMONStats True
           CephMONStatsInterval 10
           CephOSDStats True
           CephOSDStatsInterval 10
           CephPGStats True
           CephPGStatsInterval 10
           CephPoolStats True
           CephPoolStatsInterval 10
         </Module>
       </Plugin>
       ```

2. Install plugin

   ::

       ```
       [root@overcloud-controller-0 ~]# pip install collectd-ceph-storage
       ```

3. Restart collectd

   ::

       [root@overcloud-controller-0 ~]# systemctl restart collectd

4. View metrics on Ceph in your TSDB

Resources
---------

1. `Ceph.com`_
2. `Collectd.org`_

.. _Ceph.com: https://ceph.com/
.. _Collectd.org: https://collectd.org/

.. |collectd-ceph-storage| image:: https://badge.fury.io/py/collectd-ceph-storage.svg
    :target: https://pypi.python.org/pypi/collectd-ceph-storage
