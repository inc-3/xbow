import requests
from passenc import encrypt_password

headers = {
    'User-Agent': '[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/778050538;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/EVN;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/MediaPad M1 8.0 (LTE);FBSV/9;FBOP/1;FBCA/x86_64:arm64-v8a;]',
    'Accept': 'application/json, text/json, text/x-json, text/javascript, application/xml, text/xml',
    # 'Accept-Encoding': 'gzip',
    'Content-Type': 'application/x-www-form-urlencoded; application/x-www-form-urlencoded; charset=utf-8',
    'X-Fb-Connection-Type': 'WIFI',
    'X-Fb-Http-Engine': 'Tigon/Liger',
    'X-Fb-Client-Ip': 'True',
    'X-Fb-Server-Cluster': 'True',
    'X-Tigon-Is-Retry': 'False',
    'X-Fb-Device-Group': '5427',
    'X-Graphql-Request-Purpose': 'fetch',
    'X-Fb-Privacy-Context': '3643298472347298',
    'X-Graphql-Client-Library': 'graphservice',
    'X-Fb-Net-Hni': '45201',
    'X-Fb-Sim-Hni': '45201',
    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
    'Expect': '100-continue',
}

data = {
    'method': 'post',
    'pretty': 'false',
    'format': 'json',
    'server_timestamps': 'true',
    'locale': 'en_US',
    'purpose': 'fetch',
    'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
    'fb_api_caller_class': 'graphservice',
    'client_doc_id': '11994080429534472888032717282',
    'variables': '{"params":{"params":"{\\"params\\":\\"{\\\\\\"client_input_params\\\\\\":{\\\\\\"sim_phones\\\\\\":[],\\\\\\"secure_family_device_id\\\\\\":\\\\\\"27f4e2fa-7328-450b-ae5b-2ff44e51b1ff\\\\\\",\\\\\\"attestation_result\\\\\\":{\\\\\\"data\\\\\\":\\\\\\"eyJjaGFsbGVuZ2Vfbm9uY2UiOiJFSTdyN0NXc1VXR3B6VVVPUE5aVnJaTjJRdUxWZlpFVWdUM2VKY0RIM2l3PSIsInVzZXJuYW1lIjoiNjE1ODE2Nzk0NzMwNzYifQ==\\\\\\",\\\\\\"signature\\\\\\":\\\\\\"MEQCIDHrmQ86yvC7yeVBi0eYpIr2cnhtaSWxYm8I ZcZ081fAiBLzhHez6CMvaQqaFrCvfCMYker7WNLiQ4L99JpVR9K Q==\\\\\\",\\\\\\"keyHash\\\\\\":\\\\\\"61eb800e73605cd79d7465f441af1b50d7ac408845b9c77ce18b66c24ff91073\\\\\\"},\\\\\\"auth_secure_device_id\\\\\\":\\\\\\"\\\\\\",\\\\\\"has_whatsapp_installed\\\\\\":0,\\\\\\"password\\\\\\":\\\\\\"#PWD_FB4A:2:1763785040:AeuGt0Qp+arIY4+RLycAAS117/pmrGagNqoZTiTh6KkzeO7lWb3RF+ODB4C/tdDUbHDBp8HthTrlyKSFpsab2GghpBiUAdL1b9bo9fFoeo/nqbaf8rZR5OrX04wOBghi88gx6MpTHDQL0CxATt1WWiFRg45RVx35eprinNlvqcz+1Dmcl3ux7gyq+QIzl4KnOZpy/1s+OIO4u0Y8CC3AUnkvtHZg6oFrpmeMoAWagWOt13E79HqoLTEijTJeS/6uCQcPlaQbTQj2RZ84OZpJ37qvcilFXFLu8wccgagPD18kXkOSkmNXV7GW6fetmbF2nFk0axP6spGDgxKwXue35SqKlAhHne+kb9yXXk/DIv7rwiUeyQYoZ5kg6Ry/b8aJmRdR1d/IFNg=\\\\\\",\\\\\\"sso_token_map_json_string\\\\\\":\\\\\\"\\\\\\",\\\\\\"event_flow\\\\\\":\\\\\\"login_manual\\\\\\",\\\\\\"password_contains_non_ascii\\\\\\":\\\\\\"false\\\\\\",\\\\\\"sim_serials\\\\\\":[],\\\\\\"client_known_key_hash\\\\\\":\\\\\\"\\\\\\",\\\\\\"encrypted_msisdn\\\\\\":\\\\\\"\\\\\\",\\\\\\"should_show_nested_nta_from_aymh\\\\\\":0,\\\\\\"device_id\\\\\\":\\\\\\"d2c6ad4f-e161-fbcb-8505-8d2e55e94805\\\\\\",\\\\\\"login_attempt_count\\\\\\":1,\\\\\\"machine_id\\\\\\":\\\\\\"\\\\\\",\\\\\\"flash_call_permission_status\\\\\\":{\\\\\\"READ_PHONE_STATE\\\\\\":\\\\\\"DENIED\\\\\\",\\\\\\"READ_CALL_LOG\\\\\\":\\\\\\"DENIED\\\\\\",\\\\\\"ANSWER_PHONE_CALLS\\\\\\":\\\\\\"DENIED\\\\\\"},\\\\\\"accounts_list\\\\\\":[],\\\\\\"family_device_id\\\\\\":\\\\\\"d2c6ad4f-e161-fbcb-8505-8d2e55e94805\\\\\\",\\\\\\"fb_ig_device_id\\\\\\":[],\\\\\\"device_emails\\\\\\":[],\\\\\\"try_num\\\\\\":1,\\\\\\"lois_settings\\\\\\":{\\\\\\"lois_token\\\\\\":\\\\\\"\\\\\\",\\\\\\"lara_override\\\\\\":\\\\\\"\\\\\\"},\\\\\\"event_step\\\\\\":\\\\\\"home_page\\\\\\",\\\\\\"headers_infra_flow_id\\\\\\":\\\\\\"a62a4652-c56e-49bc-8fa1-ffd0665b423e\\\\\\",\\\\\\"openid_tokens\\\\\\":{},\\\\\\"contact_point\\\\\\":\\\\\\"61581679473076\\\\\\"},\\\\\\"server_params\\\\\\":{\\\\\\"should_trigger_override_login_2fa_action\\\\\\":0,\\\\\\"is_from_logged_out\\\\\\":0,\\\\\\"should_trigger_override_login_success_action\\\\\\":0,\\\\\\"login_credential_type\\\\\\":\\\\\\"none\\\\\\",\\\\\\"server_login_source\\\\\\":\\\\\\"login\\\\\\",\\\\\\"waterfall_id\\\\\\":\\\\\\"6c282a17-f640-41e1-943d-cf23777249bd\\\\\\",\\\\\\"login_source\\\\\\":\\\\\\"Login\\\\\\",\\\\\\"is_platform_login\\\\\\":0,\\\\\\"pw_encryption_try_count\\\\\\":1,\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\":36707139,\\\\\\"offline_experiment_group\\\\\\":\\\\\\"caa_iteration_v6_perf_fb_2\\\\\\",\\\\\\"is_from_landing_page\\\\\\":0,\\\\\\"password_text_input_id\\\\\\":\\\\\\"nmi7ws:95\\\\\\",\\\\\\"is_from_empty_password\\\\\\":0,\\\\\\"ar_event_source\\\\\\":\\\\\\"login_home_page\\\\\\",\\\\\\"username_text_input_id\\\\\\":\\\\\\"nmi7ws:94\\\\\\",\\\\\\"layered_homepage_experiment_group\\\\\\":null,\\\\\\"device_id\\\\\\":\\\\\\"d2c6ad4f-e161-fbcb-8505-8d2e55e94805\\\\\\",\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\":1.42852366000951E14,\\\\\\"reg_flow_source\\\\\\":\\\\\\"login_home_native_integration_point\\\\\\",\\\\\\"is_caa_perf_enabled\\\\\\":1,\\\\\\"credential_type\\\\\\":\\\\\\"password\\\\\\",\\\\\\"is_from_password_entry_page\\\\\\":0,\\\\\\"caller\\\\\\":\\\\\\"gslr\\\\\\",\\\\\\"family_device_id\\\\\\":\\\\\\"d2c6ad4f-e161-fbcb-8505-8d2e55e94805\\\\\\",\\\\\\"INTERNAL_INFRA_THEME\\\\\\":\\\\\\"harm_f\\\\\\",\\\\\\"is_from_assistive_id\\\\\\":0,\\\\\\"access_flow_version\\\\\\":\\\\\\"F2_FLOW\\\\\\",\\\\\\"is_from_logged_in_switcher\\\\\\":0}}\\"}","bloks_versioning_id":"f7f7731412f4c87953c95acd93686df979f7c47efd9b38d1778f2ffa2ae19220","app_id":"com.bloks.www.bloks.caa.login.async.send_login_request"},"scale":"2","nt_context":{"using_white_navbar":true,"styles_id":"964d559c1e2aa0142b5069bc8cb1adea","pixel_ratio":2,"is_push_on":true,"debug_tooling_metadata_token":null,"is_flipper_enabled":false,"theme_params":[],"bloks_version":"f7f7731412f4c87953c95acd93686df979f7c47efd9b38d1778f2ffa2ae19220"}}',
    'fb_api_analytics_tags': '["GraphServices"]',
    'client_trace_id': 'd6869d96-7c75-4741-9f9c-7b58fdc6fcd8',
}

password = "itvanhai.dev9x"
encrypted_passwordx = encrypt_password(password)
data['variables'] = data['variables'].replace('#PWD_FB4A:2:1763785040:AeuGt0Qp+arIY4+RLycAAS117/pmrGagNqoZTiTh6KkzeO7lWb3RF+ODB4C/tdDUbHDBp8HthTrlyKSFpsab2GghpBiUAdL1b9bo9fFoeo/nqbaf8rZR5OrX04wOBghi88gx6MpTHDQL0CxATt1WWiFRg45RVx35eprinNlvqcz+1Dmcl3ux7gyq+QIzl4KnOZpy/1s+OIO4u0Y8CC3AUnkvtHZg6oFrpmeMoAWagWOt13E79HqoLTEijTJeS/6uCQcPlaQbTQj2RZ84OZpJ37qvcilFXFLu8wccgagPD18kXkOSkmNXV7GW6fetmbF2nFk0axP6spGDgxKwXue35SqKlAhHne+kb9yXXk/DIv7rwiUeyQYoZ5kg6Ry/b8aJmRdR1d/IFNg=', encrypted_passwordx, 1)

response = requests.post('https://b-graph.facebook.com/graphql', headers=headers, data=data)

print(response.text)