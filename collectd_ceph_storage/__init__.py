#!/usr/bin/env python
#   Copyright 2017 Alex Krzos
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
"""
Collectd python plugin to read ceph storage stats off an OpenStack
Controller.
"""

import collectd
import json
import os
import subprocess
import time
import traceback


class CollectdCephStorage(object):
    def __init__(self):
        self.ceph_cluster = None
        self.ceph_latency_bench = False
        self.ceph_latency_bench_interval = 60
        self.ceph_mon_stats = False
        self.ceph_mon_stats_interval = 10
        self.ceph_osd_stats = False
        self.ceph_osd_stats_interval = 10
        self.ceph_pg_stats = False
        self.ceph_pg_stats_interval = 10
        self.ceph_pool_stats = False
        self.ceph_pool_stats_interval = 10

    def configure_callback(self, config):
        for node in config.children:
            val = str(node.values[0])
            if node.key == 'CephLatencyBench':
                self.ceph_latency_bench = val in ['True', 'true']
            elif node.key == 'CephMONStats':
                self.ceph_mon_stats = val in ['True', 'true']
            elif node.key == 'CephOSDStats':
                self.ceph_osd_stats = val in ['True', 'true']
            elif node.key == 'CephPGStats':
                self.ceph_pg_stats = val in ['True', 'true']
            elif node.key == 'CephPoolStats':
                self.ceph_pool_stats = val in ['True', 'true']
            elif node.key == 'CephCluster':
                self.ceph_cluster = val
            elif node.key == 'CephLatencyBenchInterval':
                self.ceph_latency_bench_interval = int(float(val))
            elif node.key == 'CephMONStatsInterval':
                self.ceph_mon_stats_interval = int(float(val))
            elif node.key == 'CephOSDStatsInterval':
                self.ceph_osd_stats_interval = int(float(val))
            elif node.key == 'CephPGStatsInterval':
                self.ceph_pg_stats_interval = int(float(val))
            elif node.key == 'CephPoolStatsInterval':
                self.ceph_pool_stats_interval = int(float(val))
            else:
                collectd.warning(
                    'collectd-ceph-storage: Unknown config key: {}'
                    .format(node.key))

        if not self.ceph_cluster:
            collectd.warning('collectd-ceph-storage: CephCluster Undefined')

        if self.ceph_latency_bench:
            collectd.info('Registered Ceph Bench')
            collectd.register_read(
                self.read_ceph_bench_latency,
                self.ceph_latency_bench_interval, name='ceph-latency')
        if self.ceph_mon_stats:
            collectd.info('Registered Ceph Mon')
            collectd.register_read(
                self.read_ceph_mon, self.ceph_mon_stats_interval,
                name='ceph-monitor')
        if self.ceph_osd_stats:
            collectd.info('Registered Ceph OSD')
            collectd.register_read(
                self.read_ceph_osd, self.ceph_osd_stats_interval,
                name='ceph-osd')
        if self.ceph_pg_stats:
            collectd.info('Registered CephPG')
            collectd.register_read(
                self.read_ceph_pg, self.ceph_pg_stats_interval, name='ceph-pg')
        if self.ceph_pool_stats:
            collectd.info('Registered Ceph Pool')
            collectd.register_read(
                self.read_ceph_pool, self.ceph_pool_stats_interval,
                name='ceph-pool')

    def dispatch_value(self, plugin_instance, type_instance, value, interval):
        metric = collectd.Values()
        metric.plugin = 'collectd-ceph-storage'
        metric.interval = interval
        metric.type = 'gauge'
        metric.plugin_instance = plugin_instance
        metric.type_instance = type_instance
        metric.values = [value]
        metric.dispatch()

    def read_ceph_bench_latency(self):
        collectd.info('Collecting Ceph Bench Latency')
        pass

    def read_ceph_mon(self):
        collectd.info('Collecting Ceph Mon')
        output = None
        try:
            ceph_command = (
                'ceph mon dump --format json --cluster {}'
                .format(self.ceph_cluster))
            output = subprocess.check_output(ceph_command, shell=True)
        except Exception as exc:
            collectd.error(
                'collectd-ceph-storage: ceph mon dump exception: {}'
                .format(exc))
            collectd.error(
                'collectd-ceph-storage: ceph mon dump traceback: {}'
                .format(traceback.format_exc()))
            return

        if output is None:
            collectd.error(
                'collectd-ceph-storage: ceph mon dump: output is None')

        json_data = json.loads(output)

        self.dispatch_value(
            'mon', 'number', len(json_data['mons']),
            self.ceph_mon_stats_interval)
        self.dispatch_value(
            'mon', 'quorum', len(json_data['quorum']),
            self.ceph_mon_stats_interval)

    def read_ceph_osd(self):
        collectd.info('Collecting Ceph OSD')
        pass

    def read_ceph_pg(self):
        collectd.info('Collecting Ceph PG')
        pass

    def read_ceph_pool(self):
        collectd.info('Collecting Ceph Pool')
        pass


collectd_ceph_storage = CollectdCephStorage()
collectd.register_config(collectd_ceph_storage.configure_callback)
