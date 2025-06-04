#!/bin/bash

oc apply -f openshift/tasks/preprocess-task.yaml
oc apply -f openshift/tasks/train-task.yaml
oc apply -f openshift/tasks/build-task.yaml     
oc apply -f openshift/tasks/deploy-task.yaml 

oc apply -f openshift/tasks/pipeline.yaml
oc apply -f openshift/taskruns/pipelinerun.yaml

