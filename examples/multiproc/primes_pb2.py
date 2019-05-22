# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: multiproc/primes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='multiproc/primes.proto',
  package='primes',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16multiproc/primes.proto\x12\x06primes\x1a\x1egoogle/protobuf/wrappers.proto\"\x19\n\x07Request\x12\x0e\n\x06number\x18\x01 \x01(\x03\"5\n\x05Reply\x12,\n\x08is_prime\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue23\n\x06Primes\x12)\n\x05\x43heck\x12\x0f.primes.Request\x1a\r.primes.Reply\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='primes.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='primes.Request.number', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=91,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='primes.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_prime', full_name='primes.Reply.is_prime', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=146,
)

_REPLY.fields_by_name['is_prime'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'multiproc.primes_pb2'
  # @@protoc_insertion_point(class_scope:primes.Request)
  ))
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), dict(
  DESCRIPTOR = _REPLY,
  __module__ = 'multiproc.primes_pb2'
  # @@protoc_insertion_point(class_scope:primes.Reply)
  ))
_sym_db.RegisterMessage(Reply)



_PRIMES = _descriptor.ServiceDescriptor(
  name='Primes',
  full_name='primes.Primes',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=148,
  serialized_end=199,
  methods=[
  _descriptor.MethodDescriptor(
    name='Check',
    full_name='primes.Primes.Check',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_REPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRIMES)

DESCRIPTOR.services_by_name['Primes'] = _PRIMES

# @@protoc_insertion_point(module_scope)
