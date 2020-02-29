# AWS CLI plugin for Eucalyptus Cloud service endpoints

An awscli plugin to enable Eucalyptus service endpoints via configuration.

## AWS CLI endpoint plugin

This plugin is heavily based on the [AWS CLI endpoint plugin](https://github.com/wbingli/awscli-plugin-endpoint)
which can also be used with Eucalyptus clouds as per this [blog](https://blog.eucalyptus.cloud/post/tools-awscli/)

## Installation

To install the latest release of the Eucalyptus plugin:

```
$ pip install awscli-plugin-eucalyptus
```

To install the Eucalyptus plugin from source:

```
$ pip install git+https://github.com/corymbia/eucalyptus-awscli-plugin.git
```

This requires `pip` and `git` are available.

## Configuration

To enable the plugin for a profile (or default) set the `ufshost` and other optional items:

```
$ cat .aws/config 
[plugins]
eucalyptus = awscli_plugin_eucalyptus

[default]
ufshost = euca-10-10-10-10.euca.me
ufsport = 8773
verify_ssl = yes
```

## Usage

Assuming the plugin is configured for the default profile and text output:

```
$ aws ec2 describe-regions
REGIONS	http://euca-10-10-10-10.euca.me:8773/	eucalyptus
```

or:

```
$ aws sts get-caller-identity
000366223261	arn:aws:iam::000366223261:user/admin	AIDAAY3MOQOZPRWX2TU2G
```

Commands not supported by Eucalyptus will fail.
