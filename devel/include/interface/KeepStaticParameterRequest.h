/* Software License Agreement (BSD License)
 *
 * Copyright (c) 2011, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following
 *    disclaimer in the documentation and/or other materials provided
 *    with the distribution.
 *  * Neither the name of Willow Garage, Inc. nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * Auto-generated by genmsg_cpp from file /home/wqh/catkin_ws/src/interface/srv/KeepStaticParameter.srv
 *
 */


#ifndef INTERFACE_MESSAGE_KEEPSTATICPARAMETERREQUEST_H
#define INTERFACE_MESSAGE_KEEPSTATICPARAMETERREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace interface
{
template <class ContainerAllocator>
struct KeepStaticParameterRequest_
{
  typedef KeepStaticParameterRequest_<ContainerAllocator> Type;

  KeepStaticParameterRequest_()
    : position_neck_head(0.0)
    , position_baselink_neck(0.0)
    , velocity_left_fw(0.0)
    , velocity_right_fw(0.0)  {
    }
  KeepStaticParameterRequest_(const ContainerAllocator& _alloc)
    : position_neck_head(0.0)
    , position_baselink_neck(0.0)
    , velocity_left_fw(0.0)
    , velocity_right_fw(0.0)  {
    }



   typedef double _position_neck_head_type;
  _position_neck_head_type position_neck_head;

   typedef double _position_baselink_neck_type;
  _position_baselink_neck_type position_baselink_neck;

   typedef double _velocity_left_fw_type;
  _velocity_left_fw_type velocity_left_fw;

   typedef double _velocity_right_fw_type;
  _velocity_right_fw_type velocity_right_fw;




  typedef boost::shared_ptr< ::interface::KeepStaticParameterRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::interface::KeepStaticParameterRequest_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct KeepStaticParameterRequest_

typedef ::interface::KeepStaticParameterRequest_<std::allocator<void> > KeepStaticParameterRequest;

typedef boost::shared_ptr< ::interface::KeepStaticParameterRequest > KeepStaticParameterRequestPtr;
typedef boost::shared_ptr< ::interface::KeepStaticParameterRequest const> KeepStaticParameterRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::interface::KeepStaticParameterRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::interface::KeepStaticParameterRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace interface

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'interface': ['/home/wqh/catkin_ws/src/interface/msg'], 'std_msgs': ['/opt/ros/hydro/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::interface::KeepStaticParameterRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::interface::KeepStaticParameterRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::interface::KeepStaticParameterRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::interface::KeepStaticParameterRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::interface::KeepStaticParameterRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::interface::KeepStaticParameterRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::interface::KeepStaticParameterRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2bf5219bbb63705278c4859ab89c4529";
  }

  static const char* value(const ::interface::KeepStaticParameterRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2bf5219bbb637052ULL;
  static const uint64_t static_value2 = 0x78c4859ab89c4529ULL;
};

template<class ContainerAllocator>
struct DataType< ::interface::KeepStaticParameterRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "interface/KeepStaticParameterRequest";
  }

  static const char* value(const ::interface::KeepStaticParameterRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::interface::KeepStaticParameterRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 position_neck_head\n\
float64 position_baselink_neck\n\
float64 velocity_left_fw\n\
float64 velocity_right_fw\n\
";
  }

  static const char* value(const ::interface::KeepStaticParameterRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::interface::KeepStaticParameterRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.position_neck_head);
      stream.next(m.position_baselink_neck);
      stream.next(m.velocity_left_fw);
      stream.next(m.velocity_right_fw);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct KeepStaticParameterRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::interface::KeepStaticParameterRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::interface::KeepStaticParameterRequest_<ContainerAllocator>& v)
  {
    s << indent << "position_neck_head: ";
    Printer<double>::stream(s, indent + "  ", v.position_neck_head);
    s << indent << "position_baselink_neck: ";
    Printer<double>::stream(s, indent + "  ", v.position_baselink_neck);
    s << indent << "velocity_left_fw: ";
    Printer<double>::stream(s, indent + "  ", v.velocity_left_fw);
    s << indent << "velocity_right_fw: ";
    Printer<double>::stream(s, indent + "  ", v.velocity_right_fw);
  }
};

} // namespace message_operations
} // namespace ros

#endif // INTERFACE_MESSAGE_KEEPSTATICPARAMETERREQUEST_H