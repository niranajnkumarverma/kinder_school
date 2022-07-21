@shared_task(name='realtime_task')
def RealTimeTask():
    time_s = time.time()
    result_trans = CustomModel_1.objects.all()
    result_tag = CustomModel_2.objects.all()
    result_trans_json = serializers.serialize('json', result_trans)
    result_tag_json = serializers.serialize('json', result_tag)
    # output = {"ktr": result_transmitter_json, "ktag": result_tag_json}
    # print(output)
    channel_layer = get_channel_layer()
    message = {'type': 'loc_message',
               'message_transmitter': result_trans_json,
               'message_tag': result_tag_json}
    async_to_sync(channel_layer.group_send)('core-realtime-data', message)
    print(time.time()-time_s)