FROM centos:latest
RUN yum install python3  python3-devel   gcc-c++ -y && \
    python3 -m pip install --upgrade --force-reinstall pip && \
    yum install sudo -y && \
    yum install --assumeyes  python3-pip && \
    pip install keras && \
    pip install tensorflow --no-cache-dir  tensorflow && \
    pip install --upgrade pip tensorflow && \
    pip3 install flask && \
    pip3 install joblib && \
    pip3 install sklearn && \
    mkdir  /bs_pred
COPY  Brain.h5  /bs_pred
COPY  app.py  /bs_pred
RUN  mkdir /bs_pred/templates
COPY  home.html  /bs_pred/templates
COPY  output.html   /bs_pred/templates
EXPOSE  5000
WORKDIR  /bs_pred
CMD export FLASK_APP=app.py
ENTRYPOINT flask  run --host=0.0.0.0    --port=5000
                                                   
