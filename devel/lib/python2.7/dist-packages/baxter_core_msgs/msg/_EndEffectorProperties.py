"""autogenerated by genpy from baxter_core_msgs/EndEffectorProperties.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class EndEffectorProperties(genpy.Message):
  _md5sum = "65f719b6b567d6b71b340982808da896"
  _type = "baxter_core_msgs/EndEffectorProperties"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint32 id               # EndEffectorId
uint8  ui_type
    # End Effector type enumeration, for the UI:
    uint8  NO_GRIPPER = 0
    uint8  SUCTION_CUP_GRIPPER = 1
    uint8  ELECTRIC_GRIPPER = 2
    uint8  CUSTOM_GRIPPER = 3
string manufacturer     # Manufacturer name
string product          # Product name
string serial_number    # Serial number, optional
string hardware_rev     # Hardware revision, optional
string firmware_rev     # Firmware revision, optional
string firmware_date    # Firmware date, optional
#
# End Effector Capabilities
bool   controls_grip    # true if the gripper has grip/release control
bool   senses_grip      # true if the gripper has grip sense
bool   reverses_grip    # true if the gripper has reverse-grip mode

bool   controls_force   # true if the gripper has force control
bool   senses_force     # true if the gripper has force sense

bool   controls_position # true if the gripper has position control
bool   senses_position   # true if the gripper has position sense
#
string properties       # JSON; other properties
"""
  # Pseudo-constants
  NO_GRIPPER = 0
  SUCTION_CUP_GRIPPER = 1
  ELECTRIC_GRIPPER = 2
  CUSTOM_GRIPPER = 3

  __slots__ = ['id','ui_type','manufacturer','product','serial_number','hardware_rev','firmware_rev','firmware_date','controls_grip','senses_grip','reverses_grip','controls_force','senses_force','controls_position','senses_position','properties']
  _slot_types = ['uint32','uint8','string','string','string','string','string','string','bool','bool','bool','bool','bool','bool','bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,ui_type,manufacturer,product,serial_number,hardware_rev,firmware_rev,firmware_date,controls_grip,senses_grip,reverses_grip,controls_force,senses_force,controls_position,senses_position,properties

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(EndEffectorProperties, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.ui_type is None:
        self.ui_type = 0
      if self.manufacturer is None:
        self.manufacturer = ''
      if self.product is None:
        self.product = ''
      if self.serial_number is None:
        self.serial_number = ''
      if self.hardware_rev is None:
        self.hardware_rev = ''
      if self.firmware_rev is None:
        self.firmware_rev = ''
      if self.firmware_date is None:
        self.firmware_date = ''
      if self.controls_grip is None:
        self.controls_grip = False
      if self.senses_grip is None:
        self.senses_grip = False
      if self.reverses_grip is None:
        self.reverses_grip = False
      if self.controls_force is None:
        self.controls_force = False
      if self.senses_force is None:
        self.senses_force = False
      if self.controls_position is None:
        self.controls_position = False
      if self.senses_position is None:
        self.senses_position = False
      if self.properties is None:
        self.properties = ''
    else:
      self.id = 0
      self.ui_type = 0
      self.manufacturer = ''
      self.product = ''
      self.serial_number = ''
      self.hardware_rev = ''
      self.firmware_rev = ''
      self.firmware_date = ''
      self.controls_grip = False
      self.senses_grip = False
      self.reverses_grip = False
      self.controls_force = False
      self.senses_force = False
      self.controls_position = False
      self.senses_position = False
      self.properties = ''

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
      buff.write(_struct_IB.pack(_x.id, _x.ui_type))
      _x = self.manufacturer
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.product
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.serial_number
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.hardware_rev
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.firmware_rev
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.firmware_date
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7B.pack(_x.controls_grip, _x.senses_grip, _x.reverses_grip, _x.controls_force, _x.senses_force, _x.controls_position, _x.senses_position))
      _x = self.properties
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
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
      end += 5
      (_x.id, _x.ui_type,) = _struct_IB.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.manufacturer = str[start:end].decode('utf-8')
      else:
        self.manufacturer = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.product = str[start:end].decode('utf-8')
      else:
        self.product = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.serial_number = str[start:end].decode('utf-8')
      else:
        self.serial_number = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.hardware_rev = str[start:end].decode('utf-8')
      else:
        self.hardware_rev = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.firmware_rev = str[start:end].decode('utf-8')
      else:
        self.firmware_rev = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.firmware_date = str[start:end].decode('utf-8')
      else:
        self.firmware_date = str[start:end]
      _x = self
      start = end
      end += 7
      (_x.controls_grip, _x.senses_grip, _x.reverses_grip, _x.controls_force, _x.senses_force, _x.controls_position, _x.senses_position,) = _struct_7B.unpack(str[start:end])
      self.controls_grip = bool(self.controls_grip)
      self.senses_grip = bool(self.senses_grip)
      self.reverses_grip = bool(self.reverses_grip)
      self.controls_force = bool(self.controls_force)
      self.senses_force = bool(self.senses_force)
      self.controls_position = bool(self.controls_position)
      self.senses_position = bool(self.senses_position)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.properties = str[start:end].decode('utf-8')
      else:
        self.properties = str[start:end]
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
      buff.write(_struct_IB.pack(_x.id, _x.ui_type))
      _x = self.manufacturer
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.product
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.serial_number
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.hardware_rev
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.firmware_rev
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.firmware_date
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7B.pack(_x.controls_grip, _x.senses_grip, _x.reverses_grip, _x.controls_force, _x.senses_force, _x.controls_position, _x.senses_position))
      _x = self.properties
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
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
      end += 5
      (_x.id, _x.ui_type,) = _struct_IB.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.manufacturer = str[start:end].decode('utf-8')
      else:
        self.manufacturer = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.product = str[start:end].decode('utf-8')
      else:
        self.product = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.serial_number = str[start:end].decode('utf-8')
      else:
        self.serial_number = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.hardware_rev = str[start:end].decode('utf-8')
      else:
        self.hardware_rev = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.firmware_rev = str[start:end].decode('utf-8')
      else:
        self.firmware_rev = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.firmware_date = str[start:end].decode('utf-8')
      else:
        self.firmware_date = str[start:end]
      _x = self
      start = end
      end += 7
      (_x.controls_grip, _x.senses_grip, _x.reverses_grip, _x.controls_force, _x.senses_force, _x.controls_position, _x.senses_position,) = _struct_7B.unpack(str[start:end])
      self.controls_grip = bool(self.controls_grip)
      self.senses_grip = bool(self.senses_grip)
      self.reverses_grip = bool(self.reverses_grip)
      self.controls_force = bool(self.controls_force)
      self.senses_force = bool(self.senses_force)
      self.controls_position = bool(self.controls_position)
      self.senses_position = bool(self.senses_position)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.properties = str[start:end].decode('utf-8')
      else:
        self.properties = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_IB = struct.Struct("<IB")
_struct_7B = struct.Struct("<7B")
