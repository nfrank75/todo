
# SFA

## Sale Force Automation

### Installation

pip3 install -r requirements.txt
create la base de donnee sfa
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver


## update configuration 

cp .env.sample .env 

change .env file for developement 

## for production 

change for production change .env for production 

cp .env.prod .env 


rsync -av -e "ssh -p $(PORT)" ./ $(SSH):$(PATH) \
        --exclude Makefile \
        --exclude .env \
        --exclude .git \
        --exclude .idea \
        --exclude .venv




rsync -av  -e "ssh -p 4444" . sfa@sfa-test.its-nh.com:/home/sfa/server_core --exclude .git --exclude .venv --exclude .idea --exclude .env --exclude .vscode

rsync -av  -e "ssh -p 22" . sfa@75.119.140.115:/home/sfa/buffer-middlware --exclude .git --exclude .venv --exclude .idea --exclude .env --exclude .vscode


rsync -av  -e "ssh -p 22" . ctc@192.168.1.236:/home/ctc/buffer-middleware --exclude .git --exclude .venv --exclude .idea --exclude .env --exclude .vscode




netstat -nlp | grep 8000
kill -p pid

python -m venv .venv


 nohup python3 manage.py runserver 0.0.0.0:8000 &


 
 decorator sample with parameter 

def avoid_duplicatated(operation_name):
    """
    Args:
     operation_name
    """

    def _method_wrapper(view_func):

        def _arguments_wrapper(request, *args, **kwargs) :
            
            return view_func(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper


    # WOrk In Progres

    ### Avoid duplicate 
        - Presence 
        - Request for load 
        - payment collection
        - order_create
        - customer_create
        - customer_update
        - create merchandising
        - set merchandising 
        - direct sale 