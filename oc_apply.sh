#!/bin/bash

oc apply -f openshift/tasks/preprocess-task.yaml
oc apply -f openshift/taskruns/preprocess-taskrun.yaml
oc apply -f openshift/tasks/train-task.yaml
oc apply -f openshift/taskruns/train-taskrun.yaml

