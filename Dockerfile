FROM kdelfour/cloud9-docker
MAINTAINER myself
RUN apt-get -qq update
#RUN apt-get -qq -y install curl 
#RUN curl -O -v "https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh"
COPY Anaconda3-4.2.0-Linux-x86_64.sh /home/
RUN chmod 777 /home/Anaconda3-4.2.0-Linux-x86_64.sh
RUN bash /home/Anaconda3-4.2.0-Linux-x86_64.sh -b -p $HOME/anaconda
