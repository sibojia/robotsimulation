"""autogenerated by genpy from baxter_core_msgs/NavigatorState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class NavigatorState(genpy.Message):
  _md5sum = "c91873a1e27ea9e2268873827e29eb68"
  _type = "baxter_core_msgs/NavigatorState"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# OK button
bool ok
# Cancel button
bool cancel
# Show button
bool show
# Wheel button
uint8   wheel

# true if the inner light is on, false if not
bool innerLight

# true if the outer light is on, false if not
bool outerLight

"""
  __slots__ = ['ok','cancel','show','wheel','innerLight','outerLight']
  _slot_types = ['bool','bool','bool','uint8','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ok,cancel,show,wheel,innerLight,outerLight

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(NavigatorState, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.ok is None:
        self.ok = False
      if self.cancel is None:
        self.cancel = False
      if self.show is None:
        self.show = False
      if self.wheel is None:
        self.wheel = 0
      if self.innerLight is None:
        self.innerLight = False
      if self.outerLight is None:
        self.outerLight = False
    else:
      self.ok = False
      self.cancel = False
      self.show = False
      self.wheel = 0
      self.innerLight = False
      self.outerLight = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_6B.pack(_x.ok, _x.cancel, _x.show, _x.wheel, _x.innerLight, _x.outerLight))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.ok, _x.cancel, _x.show, _x.wheel, _x.innerLight, _x.outerLight,) = _struct_6B.unpack(str[start:end])
      self.ok = bool(self.ok)
      self.cancel = bool(self.cancel)
      self.show = bool(self.show)
      self.innerLight = bool(self.innerLight)
      self.outerLight = bool(self.outerLight)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_6B.pack(_x.ok, _x.cancel, _x.show, _x.wheel, _x.innerLight, _x.outerLight))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.ok, _x.cancel, _x.show, _x.wheel, _x.innerLight, _x.outerLight,) = _struct_6B.unpack(str[start:end])
      self.ok = bool(self.ok)
      self.cancel = bool(self.cancel)
      self.show = bool(self.show)
      self.innerLight = bool(self.innerLight)
      self.outerLight = bool(self.outerLight)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_6B = struct.Struct("<6B")
