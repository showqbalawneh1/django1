
import time

class FirstMiddleware:

    def __init__ (self ,get_response):
        global first_time 
        first_time= time.time()
        self.get_response=get_response 
        print ("hello")
        print ("programmer")
    def __call__ (self, request):
        start_time = time.time()
        response=self.get_response(request)
        duration = time.time() - start_time
        all_duration=time.time()-first_time
        print(f"the request {request} took {round(duration,6)} seconds to complete.")
        print(f"the you spent this this time {round (all_duration/60,4)} minute in this session")
        return response