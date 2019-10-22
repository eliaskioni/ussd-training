from ussd.core import UssdView, UssdRequest,_customer_journey_files


class USSDGateway(UssdView):
    path = os.path.dirname(os.path.abspath(__file__))
    customer_journey_conf = path + "/github-repo-journey.yml"

    def post(self, req):
        session_id = req.data.get('session_id')
        user_input = req.data.get('text')
        ussd_request = UssdRequest(
            phone_number=req.data['phoneNumber'].strip('+'),
            session_id=session_id,
            ussd_input=user_input,
            service_code=req.data['serviceCode'],
            language=req.data.get('language', 'en')
        )

        return ussd_request
