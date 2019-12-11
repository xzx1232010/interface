from app_mongo.models import App_action_statis
import json
import time
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def parse_text(request):
    if request.method == 'POST':
        myfile = request.FILES.get("file", None)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username != 'reocar' or password != 'reocar@123!@#':
            response = {'code': 500, 'message': 'username or password is error'}
            return HttpResponse(json.dumps(response), content_type='application/json; charset=utf-8')
        if myfile is not None:
            for chunk in myfile.chunks():
                res_str = chunk.decode('utf-8')
            res_list = res_str.strip().replace('\r', '\n').split('\n')
            res_list = list(filter(lambda x: x != '', res_list))  # 去除空行
        else:
            response = {'code': 500, 'message': 'text is error'}
            return HttpResponse(json.dumps(response), content_type='application/json; charset=utf-8')
        try:
            def process(x):
                x = json.loads(x)
                x['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(x['timestamp'])))
                for key in list(x.keys()):
                    if key not in ['content', 'timestamp', 'type', 'member_id', 'device_id',
                                   'extent', 'device_resolution', 'app_channel', 'system_version',
                                   'device_type', 'network_provider', 'network', 'app_version']:
                        del x[key]
                return x
            res_list = list(map(lambda x: process(x), res_list))
            output = []
            for i in range(len(res_list)):
                output.append(App_action_statis(**res_list[i]))
            App_action_statis.objects.insert(output)
            response = {'code': 200, 'message': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json; charset=utf-8')
        except Exception as e:
            response = {'code': 500, 'error': str(e)}
            return HttpResponse(json.dumps(response), content_type='application/json; charset=utf-8')
