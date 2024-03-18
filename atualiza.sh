#!/bin/bash
echo "atualizando o código python do simulador no servidor raspberry pi..."
scp -P 2288 /home/marcelo/simulacetam/*.* marcelo@192.168.15.103:/home/marcelo/git/simulacetam

