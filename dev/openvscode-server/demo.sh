wget 'https://github.com/gitpod-io/openvscode-server/releases/download/openvscode-server-v1.64.2/openvscode-server-v1.64.2-linux-x64.tar.gz' -O openvscode-server.tgz
tar zxf openvscode-server.tgz
cd openvscode-server-*x64
./bin/openvscode-server  --without-connection-token --port=8765 --host 0.0.0.0