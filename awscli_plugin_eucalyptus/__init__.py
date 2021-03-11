import warnings

UFS_HOST = 'ufshost'
UFS_PORT = 'ufsport'
VERIFY_SSL = 'verify_ssl'
CA_BUNDLE = 'ca_bundle'
COMMAND_SERVICE_MAP = {
  'cloudwatch': 'monitoring',
  'elb': 'elasticloadbalancing',
  'elbv2': 'elasticloadbalancing',
  's3api': 's3'
}


def str2bool(value):
    return str(value).lower() in ['1', 'yes', 'y', 'true', 'on']

def get_verify_from_profile(profile):
    verify = True
    if VERIFY_SSL in profile:
        verify = str2bool(profile[VERIFY_SSL])
    return verify

def get_ca_bundle_from_profile(profile):
    return profile.get(CA_BUNDLE)

def get_endpoint_from_profile(profile, command):
    endpoint = None
    service = COMMAND_SERVICE_MAP.get(command, command)
    port = profile.get(UFS_PORT, '8773')
    if UFS_HOST in profile:
        endpoint = 'https://{}.{}:{}'.format(service, profile[UFS_HOST], port)
    return endpoint

def set_endpoint_from_profile(parsed_args, **kwargs):
    endpoint_url = parsed_args.endpoint_url
    command = parsed_args.command
    # If endpoint set on CLI option, use CLI endpoint
    if endpoint_url is None:
        session = kwargs['session']
        # Set profile to session so we can load profile from config
        if parsed_args.profile:
            session.set_config_variable('profile', parsed_args.profile)
        service_endpoint = get_endpoint_from_profile(session.get_scoped_config(), command)
        if service_endpoint is not None:
            parsed_args.endpoint_url = service_endpoint

def set_verify_from_profile(parsed_args, **kwargs):
    verify_ssl = parsed_args.verify_ssl
    command = parsed_args.command
    # By default verify_ssl is set to true
    # if --no-verify-ssl is specified, parsed_args.verify_ssl is False
    # so keep it
    if verify_ssl:
        session = kwargs['session']
        # Set profile to session so we can load profile from config
        if parsed_args.profile:
            session.set_config_variable('profile', parsed_args.profile)
        service_verify = get_verify_from_profile(session.get_scoped_config())
        if service_verify is not None:
            parsed_args.verify_ssl = service_verify
            if not service_verify:
                warnings.filterwarnings('ignore', 'Unverified HTTPS request')

def set_ca_bundle_from_profile(parsed_args, **kwargs):
    # Respect command line arg if present
    if parsed_args.ca_bundle:
        return

    session = kwargs['session']
    # Set profile to session so we can load profile from config
    if parsed_args.profile:
        session.set_config_variable('profile', parsed_args.profile)
    parsed_args.ca_bundle = get_ca_bundle_from_profile(session.get_scoped_config())

def awscli_initialize(cli):
    cli.register('top-level-args-parsed', set_endpoint_from_profile)
    cli.register('top-level-args-parsed', set_verify_from_profile)
    cli.register('top-level-args-parsed', set_ca_bundle_from_profile)

