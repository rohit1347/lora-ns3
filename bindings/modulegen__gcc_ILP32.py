from pybindgen import Module, FileCodeSink, param, retval, cppclass, typehandlers


import pybindgen.settings
import warnings

class ErrorHandler(pybindgen.settings.ErrorHandler):
    def handle_error(self, wrapper, exception, traceback_):
        warnings.warn("exception %r in wrapper %s" % (exception, wrapper))
        return True
pybindgen.settings.error_handler = ErrorHandler()


import sys

def module_init():
    root_module = Module('ns.lora', cpp_namespace='::ns3')
    return root_module

def register_types(module):
    root_module = module.get_root()
    
    ## lora-mac-command.h (module 'lora'): ns3::LoRaMacCommandCid [enumeration]
    module.add_enum('LoRaMacCommandCid', ['LINK_CHECK', 'LINK_ADR', 'DUTY_CYCLE', 'RX_PARAM_SETUP', 'DEV_STATUS', 'NEW_CHANNEL', 'RX_TIMING', 'LORA_COMMAND_PROPRIETARY'])
    ## lora-mac-command.h (module 'lora'): ns3::LoRaMacCommandDirection [enumeration]
    module.add_enum('LoRaMacCommandDirection', ['TOBASE', 'FROMBASE'])
    ## address.h (module 'network'): ns3::Address [class]
    module.add_class('Address', import_from_module='ns.network')
    ## address.h (module 'network'): ns3::Address::MaxSize_e [enumeration]
    module.add_enum('MaxSize_e', ['MAX_SIZE'], outer_class=root_module['ns3::Address'], import_from_module='ns.network')
    ## application-container.h (module 'network'): ns3::ApplicationContainer [class]
    module.add_class('ApplicationContainer', import_from_module='ns.network')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::Application > > const_iterator', u'ns3::ApplicationContainer::Iterator')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::Application > > const_iterator*', u'ns3::ApplicationContainer::Iterator*')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::Application > > const_iterator&', u'ns3::ApplicationContainer::Iterator&')
    ## trace-helper.h (module 'network'): ns3::AsciiTraceHelper [class]
    module.add_class('AsciiTraceHelper', import_from_module='ns.network')
    ## trace-helper.h (module 'network'): ns3::AsciiTraceHelperForDevice [class]
    module.add_class('AsciiTraceHelperForDevice', allow_subclassing=True, import_from_module='ns.network')
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList [class]
    module.add_class('AttributeConstructionList', import_from_module='ns.core')
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item [struct]
    module.add_class('Item', import_from_module='ns.core', outer_class=root_module['ns3::AttributeConstructionList'])
    typehandlers.add_type_alias(u'std::list< ns3::AttributeConstructionList::Item > const_iterator', u'ns3::AttributeConstructionList::CIterator')
    typehandlers.add_type_alias(u'std::list< ns3::AttributeConstructionList::Item > const_iterator*', u'ns3::AttributeConstructionList::CIterator*')
    typehandlers.add_type_alias(u'std::list< ns3::AttributeConstructionList::Item > const_iterator&', u'ns3::AttributeConstructionList::CIterator&')
    ## spectrum-model.h (module 'spectrum'): ns3::BandInfo [struct]
    module.add_class('BandInfo', import_from_module='ns.spectrum')
    ## buffer.h (module 'network'): ns3::Buffer [class]
    module.add_class('Buffer', import_from_module='ns.network')
    ## buffer.h (module 'network'): ns3::Buffer::Iterator [class]
    module.add_class('Iterator', import_from_module='ns.network', outer_class=root_module['ns3::Buffer'])
    ## packet.h (module 'network'): ns3::ByteTagIterator [class]
    module.add_class('ByteTagIterator', import_from_module='ns.network')
    ## packet.h (module 'network'): ns3::ByteTagIterator::Item [class]
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::ByteTagIterator'])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList [class]
    module.add_class('ByteTagList', import_from_module='ns.network')
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator [class]
    module.add_class('Iterator', import_from_module='ns.network', outer_class=root_module['ns3::ByteTagList'])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item [struct]
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::ByteTagList::Iterator'])
    ## callback.h (module 'core'): ns3::CallbackBase [class]
    module.add_class('CallbackBase', import_from_module='ns.core')
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::AttributeAccessor> [struct]
    module.add_class('DefaultDeleter', import_from_module='ns.core', template_parameters=['ns3::AttributeAccessor'])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::AttributeChecker> [struct]
    module.add_class('DefaultDeleter', import_from_module='ns.core', template_parameters=['ns3::AttributeChecker'])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::AttributeValue> [struct]
    module.add_class('DefaultDeleter', import_from_module='ns.core', template_parameters=['ns3::AttributeValue'])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::CallbackImplBase> [struct]
    module.add_class('DefaultDeleter', import_from_module='ns.core', template_parameters=['ns3::CallbackImplBase'])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::EventImpl> [struct]
    module.add_class('DefaultDeleter', import_from_module='ns.core', template_parameters=['ns3::EventImpl'])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::Hash::Implementation> [struct]
    module.add_class('DefaultDeleter', import_from_module='ns.core', template_parameters=['ns3::Hash::Implementation'])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::NixVector> [struct]
    module.add_class('DefaultDeleter', import_from_module='ns.core', template_parameters=['ns3::NixVector'])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::OutputStreamWrapper> [struct]
    module.add_class('DefaultDeleter', import_from_module='ns.core', template_parameters=['ns3::OutputStreamWrapper'])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::Packet> [struct]
    module.add_class('DefaultDeleter', import_from_module='ns.core', template_parameters=['ns3::Packet'])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::SpectrumModel> [struct]
    module.add_class('DefaultDeleter', import_from_module='ns.core', template_parameters=['ns3::SpectrumModel'])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::SpectrumSignalParameters> [struct]
    module.add_class('DefaultDeleter', import_from_module='ns.core', template_parameters=['ns3::SpectrumSignalParameters'])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::SpectrumValue> [struct]
    module.add_class('DefaultDeleter', import_from_module='ns.core', template_parameters=['ns3::SpectrumValue'])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::TraceSourceAccessor> [struct]
    module.add_class('DefaultDeleter', import_from_module='ns.core', template_parameters=['ns3::TraceSourceAccessor'])
    ## device-energy-model-container.h (module 'energy'): ns3::DeviceEnergyModelContainer [class]
    module.add_class('DeviceEnergyModelContainer', import_from_module='ns.energy')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::DeviceEnergyModel > > const_iterator', u'ns3::DeviceEnergyModelContainer::Iterator')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::DeviceEnergyModel > > const_iterator*', u'ns3::DeviceEnergyModelContainer::Iterator*')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::DeviceEnergyModel > > const_iterator&', u'ns3::DeviceEnergyModelContainer::Iterator&')
    ## energy-model-helper.h (module 'energy'): ns3::DeviceEnergyModelHelper [class]
    module.add_class('DeviceEnergyModelHelper', allow_subclassing=True, import_from_module='ns.energy')
    ## lora-network.h (module 'lora'): ns3::DeviceRxSettings [struct]
    module.add_class('DeviceRxSettings')
    ## energy-model-helper.h (module 'energy'): ns3::EnergySourceHelper [class]
    module.add_class('EnergySourceHelper', allow_subclassing=True, import_from_module='ns.energy')
    ## event-id.h (module 'core'): ns3::EventId [class]
    module.add_class('EventId', import_from_module='ns.core')
    ## hash.h (module 'core'): ns3::Hasher [class]
    module.add_class('Hasher', import_from_module='ns.core')
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address [class]
    module.add_class('Ipv4Address', import_from_module='ns.network')
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address [class]
    root_module['ns3::Ipv4Address'].implicitly_converts_to(root_module['ns3::Address'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask [class]
    module.add_class('Ipv4Mask', import_from_module='ns.network')
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address [class]
    module.add_class('Ipv6Address', import_from_module='ns.network')
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address [class]
    root_module['ns3::Ipv6Address'].implicitly_converts_to(root_module['ns3::Address'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix [class]
    module.add_class('Ipv6Prefix', import_from_module='ns.network')
    ## lora-energy-source-helper.h (module 'lora'): ns3::LoRaEnergySourceHelper [class]
    module.add_class('LoRaEnergySourceHelper', parent=root_module['ns3::EnergySourceHelper'])
    ## lora-radio-energy-model-helper.h (module 'lora'): ns3::LoRaRadioEnergyModelHelper [class]
    module.add_class('LoRaRadioEnergyModelHelper', parent=root_module['ns3::DeviceEnergyModelHelper'])
    ## mac32-address.h (module 'lora'): ns3::Mac32Address [class]
    module.add_class('Mac32Address')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Mac32Address const )', u'ns3::Mac32Address::TracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Mac32Address const )*', u'ns3::Mac32Address::TracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Mac32Address const )&', u'ns3::Mac32Address::TracedCallback&')
    ## mac32-address.h (module 'lora'): ns3::Mac32Address [class]
    root_module['ns3::Mac32Address'].implicitly_converts_to(root_module['ns3::Address'])
    ## mac48-address.h (module 'network'): ns3::Mac48Address [class]
    module.add_class('Mac48Address', import_from_module='ns.network')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Mac48Address )', u'ns3::Mac48Address::TracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Mac48Address )*', u'ns3::Mac48Address::TracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Mac48Address )&', u'ns3::Mac48Address::TracedCallback&')
    ## mac48-address.h (module 'network'): ns3::Mac48Address [class]
    root_module['ns3::Mac48Address'].implicitly_converts_to(root_module['ns3::Address'])
    ## mac8-address.h (module 'network'): ns3::Mac8Address [class]
    module.add_class('Mac8Address', import_from_module='ns.network')
    ## mac8-address.h (module 'network'): ns3::Mac8Address [class]
    root_module['ns3::Mac8Address'].implicitly_converts_to(root_module['ns3::Address'])
    ## net-device-container.h (module 'network'): ns3::NetDeviceContainer [class]
    module.add_class('NetDeviceContainer', import_from_module='ns.network')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::NetDevice > > const_iterator', u'ns3::NetDeviceContainer::Iterator')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::NetDevice > > const_iterator*', u'ns3::NetDeviceContainer::Iterator*')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::NetDevice > > const_iterator&', u'ns3::NetDeviceContainer::Iterator&')
    ## node-container.h (module 'network'): ns3::NodeContainer [class]
    module.add_class('NodeContainer', import_from_module='ns.network')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::Node > > const_iterator', u'ns3::NodeContainer::Iterator')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::Node > > const_iterator*', u'ns3::NodeContainer::Iterator*')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::Node > > const_iterator&', u'ns3::NodeContainer::Iterator&')
    ## object-base.h (module 'core'): ns3::ObjectBase [class]
    module.add_class('ObjectBase', allow_subclassing=True, import_from_module='ns.core')
    ## object.h (module 'core'): ns3::ObjectDeleter [struct]
    module.add_class('ObjectDeleter', import_from_module='ns.core')
    ## object-factory.h (module 'core'): ns3::ObjectFactory [class]
    module.add_class('ObjectFactory', import_from_module='ns.core')
    ## lora-network.h (module 'lora'): ns3::PacketId [struct]
    module.add_class('PacketId')
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata [class]
    module.add_class('PacketMetadata', import_from_module='ns.network')
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item [struct]
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::PacketMetadata'])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::ItemType [enumeration]
    module.add_enum('ItemType', ['PAYLOAD', 'HEADER', 'TRAILER'], outer_class=root_module['ns3::PacketMetadata::Item'], import_from_module='ns.network')
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::ItemIterator [class]
    module.add_class('ItemIterator', import_from_module='ns.network', outer_class=root_module['ns3::PacketMetadata'])
    ## lora-network.h (module 'lora'): ns3::PacketStats [struct]
    module.add_class('PacketStats')
    ## packet.h (module 'network'): ns3::PacketTagIterator [class]
    module.add_class('PacketTagIterator', import_from_module='ns.network')
    ## packet.h (module 'network'): ns3::PacketTagIterator::Item [class]
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::PacketTagIterator'])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList [class]
    module.add_class('PacketTagList', import_from_module='ns.network')
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData [struct]
    module.add_class('TagData', import_from_module='ns.network', outer_class=root_module['ns3::PacketTagList'])
    ## pcap-file.h (module 'network'): ns3::PcapFile [class]
    module.add_class('PcapFile', import_from_module='ns.network')
    ## trace-helper.h (module 'network'): ns3::PcapHelper [class]
    module.add_class('PcapHelper', import_from_module='ns.network')
    ## trace-helper.h (module 'network'): ns3::PcapHelper::DataLinkType [enumeration]
    module.add_enum('DataLinkType', ['DLT_NULL', 'DLT_EN10MB', 'DLT_PPP', 'DLT_RAW', 'DLT_IEEE802_11', 'DLT_LINUX_SLL', 'DLT_PRISM_HEADER', 'DLT_IEEE802_11_RADIO', 'DLT_IEEE802_15_4', 'DLT_NETLINK'], outer_class=root_module['ns3::PcapHelper'], import_from_module='ns.network')
    ## trace-helper.h (module 'network'): ns3::PcapHelperForDevice [class]
    module.add_class('PcapHelperForDevice', allow_subclassing=True, import_from_module='ns.network')
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter> [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::Object', 'ns3::ObjectBase', 'ns3::ObjectDeleter'], parent=root_module['ns3::ObjectBase'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simulator.h (module 'core'): ns3::Simulator [class]
    module.add_class('Simulator', destructor_visibility='private', import_from_module='ns.core')
    ## simulator.h (module 'core'): ns3::Simulator [enumeration]
    module.add_enum('', ['NO_CONTEXT'], outer_class=root_module['ns3::Simulator'], import_from_module='ns.core')
    ## tag.h (module 'network'): ns3::Tag [class]
    module.add_class('Tag', import_from_module='ns.network', parent=root_module['ns3::ObjectBase'])
    ## tag-buffer.h (module 'network'): ns3::TagBuffer [class]
    module.add_class('TagBuffer', import_from_module='ns.network')
    ## nstime.h (module 'core'): ns3::TimeWithUnit [class]
    module.add_class('TimeWithUnit', import_from_module='ns.core')
    ## traced-value.h (module 'core'): ns3::TracedValue<double> [class]
    module.add_class('TracedValue', import_from_module='ns.core', template_parameters=['double'])
    ## traced-value.h (module 'core'): ns3::TracedValue<ns3::LoRaPhy::State> [class]
    module.add_class('TracedValue', template_parameters=['ns3::LoRaPhy::State'])
    ## type-id.h (module 'core'): ns3::TypeId [class]
    module.add_class('TypeId', import_from_module='ns.core')
    ## type-id.h (module 'core'): ns3::TypeId::AttributeFlag [enumeration]
    module.add_enum('AttributeFlag', ['ATTR_GET', 'ATTR_SET', 'ATTR_CONSTRUCT', 'ATTR_SGC'], outer_class=root_module['ns3::TypeId'], import_from_module='ns.core')
    ## type-id.h (module 'core'): ns3::TypeId::SupportLevel [enumeration]
    module.add_enum('SupportLevel', ['SUPPORTED', 'DEPRECATED', 'OBSOLETE'], outer_class=root_module['ns3::TypeId'], import_from_module='ns.core')
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation [struct]
    module.add_class('AttributeInformation', import_from_module='ns.core', outer_class=root_module['ns3::TypeId'])
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation [struct]
    module.add_class('TraceSourceInformation', import_from_module='ns.core', outer_class=root_module['ns3::TypeId'])
    typehandlers.add_type_alias(u'uint32_t', u'ns3::TypeId::hash_t')
    typehandlers.add_type_alias(u'uint32_t*', u'ns3::TypeId::hash_t*')
    typehandlers.add_type_alias(u'uint32_t&', u'ns3::TypeId::hash_t&')
    ## vector.h (module 'core'): ns3::Vector2D [class]
    module.add_class('Vector2D', import_from_module='ns.core')
    ## vector.h (module 'core'): ns3::Vector3D [class]
    module.add_class('Vector3D', import_from_module='ns.core')
    ## empty.h (module 'core'): ns3::empty [class]
    module.add_class('empty', import_from_module='ns.core')
    ## int64x64-128.h (module 'core'): ns3::int64x64_t [class]
    module.add_class('int64x64_t', import_from_module='ns.core')
    ## int64x64-128.h (module 'core'): ns3::int64x64_t::impl_type [enumeration]
    module.add_enum('impl_type', ['int128_impl', 'cairo_impl', 'ld_impl'], outer_class=root_module['ns3::int64x64_t'], import_from_module='ns.core')
    ## chunk.h (module 'network'): ns3::Chunk [class]
    module.add_class('Chunk', import_from_module='ns.network', parent=root_module['ns3::ObjectBase'])
    ## header.h (module 'network'): ns3::Header [class]
    module.add_class('Header', import_from_module='ns.network', parent=root_module['ns3::Chunk'])
    ## lora-helper.h (module 'lora'): ns3::LoRaHelper [class]
    module.add_class('LoRaHelper', parent=[root_module['ns3::PcapHelperForDevice'], root_module['ns3::AsciiTraceHelperForDevice']])
    ## lora-mac-header.h (module 'lora'): ns3::LoRaMacHeader [class]
    module.add_class('LoRaMacHeader', parent=root_module['ns3::Header'])
    ## lora-mac-header.h (module 'lora'): ns3::LoRaMacHeader::LoRaMacType [enumeration]
    module.add_enum('LoRaMacType', ['LORA_MAC_JOIN_REQUEST', 'LORA_MAC_JOIN_ACCEPT', 'LORA_MAC_UNCONFIRMED_DATA_UP', 'LORA_MAC_UNCONFIRMED_DATA_DOWN', 'LORA_MAC_CONFIRMED_DATA_UP', 'LORA_MAC_CONFIRMED_DATA_DOWN', 'LORA_MAC_BEACON', 'LORA_MAC_PROPRIETARY'], outer_class=root_module['ns3::LoRaMacHeader'])
    ## lora-mac-header.h (module 'lora'): ns3::LoRaMacHeader::KeyIdModeType [enumeration]
    module.add_enum('KeyIdModeType', ['IMPLICIT', 'NOKEYSOURCE', 'SHORTKEYSOURCE', 'LONGKEYSOURCE'], outer_class=root_module['ns3::LoRaMacHeader'])
    ## lora-mac-header.h (module 'lora'): ns3::LoRaMacHeader::FrameVersionType [enumeration]
    module.add_enum('FrameVersionType', ['LORA2003', 'LORA2006', 'FRAME_VERSION_RESERVED'], outer_class=root_module['ns3::LoRaMacHeader'])
    ## lora-phy-header.h (module 'lora'): ns3::LoRaPhyHeader [class]
    module.add_class('LoRaPhyHeader', parent=root_module['ns3::Header'])
    ## object.h (module 'core'): ns3::Object [class]
    module.add_class('Object', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter >'])
    ## object.h (module 'core'): ns3::Object::AggregateIterator [class]
    module.add_class('AggregateIterator', import_from_module='ns.core', outer_class=root_module['ns3::Object'])
    ## pcap-file-wrapper.h (module 'network'): ns3::PcapFileWrapper [class]
    module.add_class('PcapFileWrapper', import_from_module='ns.network', parent=root_module['ns3::Object'])
    ## propagation-delay-model.h (module 'propagation'): ns3::PropagationDelayModel [class]
    module.add_class('PropagationDelayModel', import_from_module='ns.propagation', parent=root_module['ns3::Object'])
    ## propagation-loss-model.h (module 'propagation'): ns3::PropagationLossModel [class]
    module.add_class('PropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::Object'])
    ## propagation-delay-model.h (module 'propagation'): ns3::RandomPropagationDelayModel [class]
    module.add_class('RandomPropagationDelayModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationDelayModel'])
    ## propagation-loss-model.h (module 'propagation'): ns3::RandomPropagationLossModel [class]
    module.add_class('RandomPropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    ## random-variable-stream.h (module 'core'): ns3::RandomVariableStream [class]
    module.add_class('RandomVariableStream', import_from_module='ns.core', parent=root_module['ns3::Object'])
    ## propagation-loss-model.h (module 'propagation'): ns3::RangePropagationLossModel [class]
    module.add_class('RangePropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    ## random-variable-stream.h (module 'core'): ns3::SequentialRandomVariable [class]
    module.add_class('SequentialRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::AttributeAccessor', 'ns3::empty', 'ns3::DefaultDeleter<ns3::AttributeAccessor>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::AttributeChecker', 'ns3::empty', 'ns3::DefaultDeleter<ns3::AttributeChecker>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::AttributeValue', 'ns3::empty', 'ns3::DefaultDeleter<ns3::AttributeValue>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::CallbackImplBase', 'ns3::empty', 'ns3::DefaultDeleter<ns3::CallbackImplBase>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::EventImpl', 'ns3::empty', 'ns3::DefaultDeleter<ns3::EventImpl>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::Hash::Implementation', 'ns3::empty', 'ns3::DefaultDeleter<ns3::Hash::Implementation>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::NixVector', 'ns3::empty', 'ns3::DefaultDeleter<ns3::NixVector>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::OutputStreamWrapper', 'ns3::empty', 'ns3::DefaultDeleter<ns3::OutputStreamWrapper>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::Packet', 'ns3::empty', 'ns3::DefaultDeleter<ns3::Packet>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::QueueItem, ns3::empty, ns3::DefaultDeleter<ns3::QueueItem> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::QueueItem', 'ns3::empty', 'ns3::DefaultDeleter<ns3::QueueItem>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumModel> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::SpectrumModel', 'ns3::empty', 'ns3::DefaultDeleter<ns3::SpectrumModel>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumSignalParameters> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::SpectrumSignalParameters', 'ns3::empty', 'ns3::DefaultDeleter<ns3::SpectrumSignalParameters>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumValue> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::SpectrumValue', 'ns3::empty', 'ns3::DefaultDeleter<ns3::SpectrumValue>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::TraceSourceAccessor', 'ns3::empty', 'ns3::DefaultDeleter<ns3::TraceSourceAccessor>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## spectrum-model.h (module 'spectrum'): ns3::SpectrumModel [class]
    module.add_class('SpectrumModel', import_from_module='ns.spectrum', parent=root_module['ns3::SimpleRefCount< ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumModel> >'])
    ## spectrum-phy.h (module 'spectrum'): ns3::SpectrumPhy [class]
    module.add_class('SpectrumPhy', import_from_module='ns.spectrum', parent=root_module['ns3::Object'])
    ## spectrum-propagation-loss-model.h (module 'spectrum'): ns3::SpectrumPropagationLossModel [class]
    module.add_class('SpectrumPropagationLossModel', import_from_module='ns.spectrum', parent=root_module['ns3::Object'])
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters [struct]
    module.add_class('SpectrumSignalParameters', import_from_module='ns.spectrum', parent=root_module['ns3::SimpleRefCount< ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumSignalParameters> >'])
    ## spectrum-value.h (module 'spectrum'): ns3::SpectrumValue [class]
    module.add_class('SpectrumValue', import_from_module='ns.spectrum', parent=root_module['ns3::SimpleRefCount< ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumValue> >'])
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::SpectrumValue > )', u'ns3::SpectrumValue::TracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::SpectrumValue > )*', u'ns3::SpectrumValue::TracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::SpectrumValue > )&', u'ns3::SpectrumValue::TracedCallback&')
    ## propagation-loss-model.h (module 'propagation'): ns3::ThreeLogDistancePropagationLossModel [class]
    module.add_class('ThreeLogDistancePropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    ## nstime.h (module 'core'): ns3::Time [class]
    module.add_class('Time', import_from_module='ns.core')
    ## nstime.h (module 'core'): ns3::Time::Unit [enumeration]
    module.add_enum('Unit', ['Y', 'D', 'H', 'MIN', 'S', 'MS', 'US', 'NS', 'PS', 'FS', 'LAST'], outer_class=root_module['ns3::Time'], import_from_module='ns.core')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Time )', u'ns3::Time::TracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Time )*', u'ns3::Time::TracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Time )&', u'ns3::Time::TracedCallback&')
    ## nstime.h (module 'core'): ns3::Time [class]
    root_module['ns3::Time'].implicitly_converts_to(root_module['ns3::int64x64_t'])
    ## trace-source-accessor.h (module 'core'): ns3::TraceSourceAccessor [class]
    module.add_class('TraceSourceAccessor', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >'])
    ## trailer.h (module 'network'): ns3::Trailer [class]
    module.add_class('Trailer', import_from_module='ns.network', parent=root_module['ns3::Chunk'])
    ## random-variable-stream.h (module 'core'): ns3::TriangularRandomVariable [class]
    module.add_class('TriangularRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## propagation-loss-model.h (module 'propagation'): ns3::TwoRayGroundPropagationLossModel [class]
    module.add_class('TwoRayGroundPropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    ## random-variable-stream.h (module 'core'): ns3::UniformRandomVariable [class]
    module.add_class('UniformRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## random-variable-stream.h (module 'core'): ns3::WeibullRandomVariable [class]
    module.add_class('WeibullRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## random-variable-stream.h (module 'core'): ns3::ZetaRandomVariable [class]
    module.add_class('ZetaRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## random-variable-stream.h (module 'core'): ns3::ZipfRandomVariable [class]
    module.add_class('ZipfRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## application.h (module 'network'): ns3::Application [class]
    module.add_class('Application', import_from_module='ns.network', parent=root_module['ns3::Object'])
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Time const &, ns3::Address const & )', u'ns3::Application::DelayAddressCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Time const &, ns3::Address const & )*', u'ns3::Application::DelayAddressCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Time const &, ns3::Address const & )&', u'ns3::Application::DelayAddressCallback&')
    typehandlers.add_type_alias(u'void ( * ) ( std::string const &, std::string const & )', u'ns3::Application::StateTransitionCallback')
    typehandlers.add_type_alias(u'void ( * ) ( std::string const &, std::string const & )*', u'ns3::Application::StateTransitionCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( std::string const &, std::string const & )&', u'ns3::Application::StateTransitionCallback&')
    ## attribute.h (module 'core'): ns3::AttributeAccessor [class]
    module.add_class('AttributeAccessor', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >'])
    ## attribute.h (module 'core'): ns3::AttributeChecker [class]
    module.add_class('AttributeChecker', allow_subclassing=False, automatic_type_narrowing=True, import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >'])
    ## attribute.h (module 'core'): ns3::AttributeValue [class]
    module.add_class('AttributeValue', allow_subclassing=False, automatic_type_narrowing=True, import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >'])
    ## boolean.h (module 'core'): ns3::BooleanChecker [class]
    module.add_class('BooleanChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## boolean.h (module 'core'): ns3::BooleanValue [class]
    module.add_class('BooleanValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## callback.h (module 'core'): ns3::CallbackChecker [class]
    module.add_class('CallbackChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## callback.h (module 'core'): ns3::CallbackImplBase [class]
    module.add_class('CallbackImplBase', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >'])
    ## callback.h (module 'core'): ns3::CallbackValue [class]
    module.add_class('CallbackValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## channel.h (module 'network'): ns3::Channel [class]
    module.add_class('Channel', import_from_module='ns.network', parent=root_module['ns3::Object'])
    ## random-variable-stream.h (module 'core'): ns3::ConstantRandomVariable [class]
    module.add_class('ConstantRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## propagation-delay-model.h (module 'propagation'): ns3::ConstantSpeedPropagationDelayModel [class]
    module.add_class('ConstantSpeedPropagationDelayModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationDelayModel'])
    ## random-variable-stream.h (module 'core'): ns3::DeterministicRandomVariable [class]
    module.add_class('DeterministicRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## device-energy-model.h (module 'energy'): ns3::DeviceEnergyModel [class]
    module.add_class('DeviceEnergyModel', import_from_module='ns.energy', parent=root_module['ns3::Object'])
    typehandlers.add_type_alias(u'ns3::Callback< void, int, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::DeviceEnergyModel::ChangeStateCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, int, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::DeviceEnergyModel::ChangeStateCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, int, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::DeviceEnergyModel::ChangeStateCallback&')
    ## double.h (module 'core'): ns3::DoubleValue [class]
    module.add_class('DoubleValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## random-variable-stream.h (module 'core'): ns3::EmpiricalRandomVariable [class]
    module.add_class('EmpiricalRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## attribute.h (module 'core'): ns3::EmptyAttributeAccessor [class]
    module.add_class('EmptyAttributeAccessor', import_from_module='ns.core', parent=root_module['ns3::AttributeAccessor'])
    ## attribute.h (module 'core'): ns3::EmptyAttributeChecker [class]
    module.add_class('EmptyAttributeChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## attribute.h (module 'core'): ns3::EmptyAttributeValue [class]
    module.add_class('EmptyAttributeValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## energy-harvester.h (module 'energy'): ns3::EnergyHarvester [class]
    module.add_class('EnergyHarvester', import_from_module='ns.energy', parent=root_module['ns3::Object'])
    ## energy-source.h (module 'energy'): ns3::EnergySource [class]
    module.add_class('EnergySource', import_from_module='ns.energy', parent=root_module['ns3::Object'])
    ## energy-source-container.h (module 'energy'): ns3::EnergySourceContainer [class]
    module.add_class('EnergySourceContainer', import_from_module='ns.energy', parent=root_module['ns3::Object'])
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::EnergySource > > const_iterator', u'ns3::EnergySourceContainer::Iterator')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::EnergySource > > const_iterator*', u'ns3::EnergySourceContainer::Iterator*')
    typehandlers.add_type_alias(u'std::vector< ns3::Ptr< ns3::EnergySource > > const_iterator&', u'ns3::EnergySourceContainer::Iterator&')
    ## enum.h (module 'core'): ns3::EnumChecker [class]
    module.add_class('EnumChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## enum.h (module 'core'): ns3::EnumValue [class]
    module.add_class('EnumValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## random-variable-stream.h (module 'core'): ns3::ErlangRandomVariable [class]
    module.add_class('ErlangRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## event-impl.h (module 'core'): ns3::EventImpl [class]
    module.add_class('EventImpl', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >'])
    ## random-variable-stream.h (module 'core'): ns3::ExponentialRandomVariable [class]
    module.add_class('ExponentialRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## propagation-loss-model.h (module 'propagation'): ns3::FixedRssLossModel [class]
    module.add_class('FixedRssLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    ## propagation-loss-model.h (module 'propagation'): ns3::FriisPropagationLossModel [class]
    module.add_class('FriisPropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    ## random-variable-stream.h (module 'core'): ns3::GammaRandomVariable [class]
    module.add_class('GammaRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## gw-trailer.h (module 'lora'): ns3::GwTrailer [class]
    module.add_class('GwTrailer', parent=root_module['ns3::Trailer'])
    ## integer.h (module 'core'): ns3::IntegerValue [class]
    module.add_class('IntegerValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressChecker [class]
    module.add_class('Ipv4AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressValue [class]
    module.add_class('Ipv4AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskChecker [class]
    module.add_class('Ipv4MaskChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskValue [class]
    module.add_class('Ipv4MaskValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressChecker [class]
    module.add_class('Ipv6AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressValue [class]
    module.add_class('Ipv6AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixChecker [class]
    module.add_class('Ipv6PrefixChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixValue [class]
    module.add_class('Ipv6PrefixValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## lora-application.h (module 'lora'): ns3::LoRaApplication [class]
    module.add_class('LoRaApplication', parent=root_module['ns3::Application'])
    ## lora-error-model.h (module 'lora'): ns3::LoRaErrorModel [class]
    module.add_class('LoRaErrorModel', parent=root_module['ns3::Object'])
    ## lora-mac-command.h (module 'lora'): ns3::LoRaMacCommand [class]
    module.add_class('LoRaMacCommand', parent=root_module['ns3::Object'])
    ## lora-mac-trailer.h (module 'lora'): ns3::LoRaMacTrailer [class]
    module.add_class('LoRaMacTrailer', parent=root_module['ns3::Trailer'])
    ## lora-network.h (module 'lora'): ns3::LoRaNetwork [class]
    module.add_class('LoRaNetwork', parent=root_module['ns3::Application'])
    ## lora-network-application.h (module 'lora'): ns3::LoRaNetworkApplication [class]
    module.add_class('LoRaNetworkApplication', parent=root_module['ns3::Application'])
    ## lora-network-trailer.h (module 'lora'): ns3::LoRaNetworkTrailer [class]
    module.add_class('LoRaNetworkTrailer', parent=root_module['ns3::Trailer'])
    ## lora-no-power-application.h (module 'lora'): ns3::LoRaNoPowerApplication [class]
    module.add_class('LoRaNoPowerApplication', parent=root_module['ns3::LoRaNetworkApplication'])
    ## lora-phy.h (module 'lora'): ns3::LoRaPhy [class]
    module.add_class('LoRaPhy', parent=root_module['ns3::SpectrumPhy'])
    ## lora-phy.h (module 'lora'): ns3::LoRaPhy::State [enumeration]
    module.add_enum('State', ['TX', 'RX', 'IDLE'], outer_class=root_module['ns3::LoRaPhy'])
    ## lora-power-application.h (module 'lora'): ns3::LoRaPowerApplication [class]
    module.add_class('LoRaPowerApplication', parent=root_module['ns3::LoRaNetworkApplication'])
    ## lora-radio-energy-model.h (module 'lora'): ns3::LoRaRadioEnergyModel [class]
    module.add_class('LoRaRadioEnergyModel', parent=root_module['ns3::DeviceEnergyModel'])
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LoRaRadioEnergyModel::LoRaRadioEnergyDepletionCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LoRaRadioEnergyModel::LoRaRadioEnergyDepletionCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LoRaRadioEnergyModel::LoRaRadioEnergyDepletionCallback&')
    ## lora-sink-application.h (module 'lora'): ns3::LoRaSinkApplication [class]
    module.add_class('LoRaSinkApplication', parent=root_module['ns3::Application'])
    ## lora-spectrum-signal-parameters.h (module 'lora'): ns3::LoRaSpectrumSignalParameters [struct]
    module.add_class('LoRaSpectrumSignalParameters', parent=root_module['ns3::SpectrumSignalParameters'])
    ## lora-test-application.h (module 'lora'): ns3::LoRaTestApplication [class]
    module.add_class('LoRaTestApplication', parent=root_module['ns3::LoRaNetworkApplication'])
    ## propagation-loss-model.h (module 'propagation'): ns3::LogDistancePropagationLossModel [class]
    module.add_class('LogDistancePropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    ## random-variable-stream.h (module 'core'): ns3::LogNormalRandomVariable [class]
    module.add_class('LogNormalRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## mac32-address.h (module 'lora'): ns3::Mac32AddressChecker [class]
    module.add_class('Mac32AddressChecker', parent=root_module['ns3::AttributeChecker'])
    ## mac32-address.h (module 'lora'): ns3::Mac32AddressValue [class]
    module.add_class('Mac32AddressValue', parent=root_module['ns3::AttributeValue'])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressChecker [class]
    module.add_class('Mac48AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressValue [class]
    module.add_class('Mac48AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## propagation-loss-model.h (module 'propagation'): ns3::MatrixPropagationLossModel [class]
    module.add_class('MatrixPropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    ## mobility-model.h (module 'mobility'): ns3::MobilityModel [class]
    module.add_class('MobilityModel', import_from_module='ns.mobility', parent=root_module['ns3::Object'])
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::MobilityModel const > )', u'ns3::MobilityModel::TracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::MobilityModel const > )*', u'ns3::MobilityModel::TracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::MobilityModel const > )&', u'ns3::MobilityModel::TracedCallback&')
    ## propagation-loss-model.h (module 'propagation'): ns3::NakagamiPropagationLossModel [class]
    module.add_class('NakagamiPropagationLossModel', import_from_module='ns.propagation', parent=root_module['ns3::PropagationLossModel'])
    ## net-device.h (module 'network'): ns3::NetDevice [class]
    module.add_class('NetDevice', import_from_module='ns.network', parent=root_module['ns3::Object'])
    ## net-device.h (module 'network'): ns3::NetDevice::PacketType [enumeration]
    module.add_enum('PacketType', ['PACKET_HOST', 'NS3_PACKET_HOST', 'PACKET_BROADCAST', 'NS3_PACKET_BROADCAST', 'PACKET_MULTICAST', 'NS3_PACKET_MULTICAST', 'PACKET_OTHERHOST', 'NS3_PACKET_OTHERHOST'], outer_class=root_module['ns3::NetDevice'], import_from_module='ns.network')
    typehandlers.add_type_alias(u'void ( * ) (  )', u'ns3::NetDevice::LinkChangeTracedCallback')
    typehandlers.add_type_alias(u'void ( * ) (  )*', u'ns3::NetDevice::LinkChangeTracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) (  )&', u'ns3::NetDevice::LinkChangeTracedCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::NetDevice::ReceiveCallback')
    typehandlers.add_type_alias(u'ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::NetDevice::ReceiveCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::NetDevice::ReceiveCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', u'ns3::NetDevice::PromiscReceiveCallback')
    typehandlers.add_type_alias(u'ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::NetDevice::PromiscReceiveCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::NetDevice::PromiscReceiveCallback&')
    ## new-channel-ans.h (module 'lora'): ns3::NewChannelAns [class]
    module.add_class('NewChannelAns', parent=root_module['ns3::LoRaMacCommand'])
    ## new-channel-req.h (module 'lora'): ns3::NewChannelReq [class]
    module.add_class('NewChannelReq', parent=root_module['ns3::LoRaMacCommand'])
    ## nix-vector.h (module 'network'): ns3::NixVector [class]
    module.add_class('NixVector', import_from_module='ns.network', parent=root_module['ns3::SimpleRefCount< ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >'])
    ## node.h (module 'network'): ns3::Node [class]
    module.add_class('Node', import_from_module='ns.network', parent=root_module['ns3::Object'])
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', u'ns3::Node::ProtocolHandler')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::Node::ProtocolHandler*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::Node::ProtocolHandler&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::Node::DeviceAdditionListener')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::Node::DeviceAdditionListener*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::Node::DeviceAdditionListener&')
    ## random-variable-stream.h (module 'core'): ns3::NormalRandomVariable [class]
    module.add_class('NormalRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryChecker [class]
    module.add_class('ObjectFactoryChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryValue [class]
    module.add_class('ObjectFactoryValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## output-stream-wrapper.h (module 'network'): ns3::OutputStreamWrapper [class]
    module.add_class('OutputStreamWrapper', import_from_module='ns.network', parent=root_module['ns3::SimpleRefCount< ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> >'])
    ## packet.h (module 'network'): ns3::Packet [class]
    module.add_class('Packet', import_from_module='ns.network', parent=root_module['ns3::SimpleRefCount< ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >'])
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const > )', u'ns3::Packet::TracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const > )*', u'ns3::Packet::TracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const > )&', u'ns3::Packet::TracedCallback&')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const >, ns3::Address const & )', u'ns3::Packet::AddressTracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const >, ns3::Address const & )*', u'ns3::Packet::AddressTracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const >, ns3::Address const & )&', u'ns3::Packet::AddressTracedCallback&')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const > const, ns3::Address const &, ns3::Address const & )', u'ns3::Packet::TwoAddressTracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const > const, ns3::Address const &, ns3::Address const & )*', u'ns3::Packet::TwoAddressTracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const > const, ns3::Address const &, ns3::Address const & )&', u'ns3::Packet::TwoAddressTracedCallback&')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const >, ns3::Mac48Address )', u'ns3::Packet::Mac48AddressTracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const >, ns3::Mac48Address )*', u'ns3::Packet::Mac48AddressTracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const >, ns3::Mac48Address )&', u'ns3::Packet::Mac48AddressTracedCallback&')
    typehandlers.add_type_alias(u'void ( * ) ( uint32_t, uint32_t )', u'ns3::Packet::SizeTracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( uint32_t, uint32_t )*', u'ns3::Packet::SizeTracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( uint32_t, uint32_t )&', u'ns3::Packet::SizeTracedCallback&')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const >, double )', u'ns3::Packet::SinrTracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const >, double )*', u'ns3::Packet::SinrTracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::Packet const >, double )&', u'ns3::Packet::SinrTracedCallback&')
    ## random-variable-stream.h (module 'core'): ns3::ParetoRandomVariable [class]
    module.add_class('ParetoRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## queue-item.h (module 'network'): ns3::QueueItem [class]
    module.add_class('QueueItem', import_from_module='ns.network', parent=root_module['ns3::SimpleRefCount< ns3::QueueItem, ns3::empty, ns3::DefaultDeleter<ns3::QueueItem> >'])
    ## queue-item.h (module 'network'): ns3::QueueItem::Uint8Values [enumeration]
    module.add_enum('Uint8Values', ['IP_DSFIELD'], outer_class=root_module['ns3::QueueItem'], import_from_module='ns.network')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::QueueItem const > )', u'ns3::QueueItem::TracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::QueueItem const > )*', u'ns3::QueueItem::TracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::QueueItem const > )&', u'ns3::QueueItem::TracedCallback&')
    ## rx-param-setup-ans.h (module 'lora'): ns3::RxParamSetupAns [class]
    module.add_class('RxParamSetupAns', parent=root_module['ns3::LoRaMacCommand'])
    ## rx-param-setup-req.h (module 'lora'): ns3::RxParamSetupReq [class]
    module.add_class('RxParamSetupReq', parent=root_module['ns3::LoRaMacCommand'])
    ## rx-timing-setup-ans.h (module 'lora'): ns3::RxTimingSetupAns [class]
    module.add_class('RxTimingSetupAns', parent=root_module['ns3::LoRaMacCommand'])
    ## rx-timing-setup-req.h (module 'lora'): ns3::RxTimingSetupReq [class]
    module.add_class('RxTimingSetupReq', parent=root_module['ns3::LoRaMacCommand'])
    ## spectrum-channel.h (module 'spectrum'): ns3::SpectrumChannel [class]
    module.add_class('SpectrumChannel', import_from_module='ns.spectrum', parent=root_module['ns3::Channel'])
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::SpectrumPhy const >, ns3::Ptr< ns3::SpectrumPhy const >, double )', u'ns3::SpectrumChannel::LossTracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::SpectrumPhy const >, ns3::Ptr< ns3::SpectrumPhy const >, double )*', u'ns3::SpectrumChannel::LossTracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::SpectrumPhy const >, ns3::Ptr< ns3::SpectrumPhy const >, double )&', u'ns3::SpectrumChannel::LossTracedCallback&')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::MobilityModel const >, ns3::Ptr< ns3::MobilityModel const >, double, double, double, double )', u'ns3::SpectrumChannel::GainTracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::MobilityModel const >, ns3::Ptr< ns3::MobilityModel const >, double, double, double, double )*', u'ns3::SpectrumChannel::GainTracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::MobilityModel const >, ns3::Ptr< ns3::MobilityModel const >, double, double, double, double )&', u'ns3::SpectrumChannel::GainTracedCallback&')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::SpectrumSignalParameters > )', u'ns3::SpectrumChannel::SignalParametersTracedCallback')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::SpectrumSignalParameters > )*', u'ns3::SpectrumChannel::SignalParametersTracedCallback*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Ptr< ns3::SpectrumSignalParameters > )&', u'ns3::SpectrumChannel::SignalParametersTracedCallback&')
    ## nstime.h (module 'core'): ns3::TimeValue [class]
    module.add_class('TimeValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## type-id.h (module 'core'): ns3::TypeIdChecker [class]
    module.add_class('TypeIdChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## type-id.h (module 'core'): ns3::TypeIdValue [class]
    module.add_class('TypeIdValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## uinteger.h (module 'core'): ns3::UintegerValue [class]
    module.add_class('UintegerValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## vector.h (module 'core'): ns3::Vector2DChecker [class]
    module.add_class('Vector2DChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## vector.h (module 'core'): ns3::Vector2DValue [class]
    module.add_class('Vector2DValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## vector.h (module 'core'): ns3::Vector3DChecker [class]
    module.add_class('Vector3DChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## vector.h (module 'core'): ns3::Vector3DValue [class]
    module.add_class('Vector3DValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## address.h (module 'network'): ns3::AddressChecker [class]
    module.add_class('AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## address.h (module 'network'): ns3::AddressValue [class]
    module.add_class('AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## callback.h (module 'core'): ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['bool', 'ns3::Ptr<ns3::NetDevice>', 'ns3::Ptr<const ns3::Packet>', 'unsigned short', 'const ns3::Address &', 'const ns3::Address &', 'ns3::NetDevice::PacketType', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['bool', 'ns3::Ptr<ns3::NetDevice>', 'ns3::Ptr<const ns3::Packet>', 'unsigned short', 'const ns3::Address &', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<bool, ns3::Ptr<ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['bool', 'ns3::Ptr<ns3::Packet>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['ns3::ObjectBase *', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, double, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['void', 'double', 'double', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::LoRaPhy::State, ns3::LoRaPhy::State, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', template_parameters=['void', 'ns3::LoRaPhy::State', 'ns3::LoRaPhy::State', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::Ptr<const ns3::MobilityModel>, double, double, double, double, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['void', 'ns3::Ptr<const ns3::MobilityModel>', 'ns3::Ptr<const ns3::MobilityModel>', 'double', 'double', 'double', 'double', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['void', 'ns3::Ptr<const ns3::MobilityModel>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<const ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['void', 'ns3::Ptr<const ns3::Packet>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<const ns3::SpectrumPhy>, ns3::Ptr<const ns3::SpectrumPhy>, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['void', 'ns3::Ptr<const ns3::SpectrumPhy>', 'ns3::Ptr<const ns3::SpectrumPhy>', 'double', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['void', 'ns3::Ptr<ns3::NetDevice>', 'ns3::Ptr<const ns3::Packet>', 'unsigned short', 'const ns3::Address &', 'const ns3::Address &', 'ns3::NetDevice::PacketType', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['void', 'ns3::Ptr<ns3::NetDevice>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<ns3::SpectrumSignalParameters>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['void', 'ns3::Ptr<ns3::SpectrumSignalParameters>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['void', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, std::basic_string<char>, std::basic_string<char>, bool, double, double, double, ns3::empty, ns3::empty, ns3::empty> [class]
    module.add_class('CallbackImpl', import_from_module='ns.core', template_parameters=['void', 'std::basic_string<char>', 'std::basic_string<char>', 'bool', 'double', 'double', 'double', 'ns3::empty', 'ns3::empty', 'ns3::empty'], parent=root_module['ns3::CallbackImplBase'])
    ## dev-status-ans.h (module 'lora'): ns3::DevStatusAns [class]
    module.add_class('DevStatusAns', parent=root_module['ns3::LoRaMacCommand'])
    ## dev-status-req.h (module 'lora'): ns3::DevStatusReq [class]
    module.add_class('DevStatusReq', parent=root_module['ns3::LoRaMacCommand'])
    ## duty-cycle-ans.h (module 'lora'): ns3::DutyCycleAns [class]
    module.add_class('DutyCycleAns', parent=root_module['ns3::LoRaMacCommand'])
    ## duty-cycle-req.h (module 'lora'): ns3::DutyCycleReq [class]
    module.add_class('DutyCycleReq', parent=root_module['ns3::LoRaMacCommand'])
    ## link-adr-ans.h (module 'lora'): ns3::LinkAdrAns [class]
    module.add_class('LinkAdrAns', parent=root_module['ns3::LoRaMacCommand'])
    ## link-adr-req.h (module 'lora'): ns3::LinkAdrReq [class]
    module.add_class('LinkAdrReq', parent=root_module['ns3::LoRaMacCommand'])
    ## link-check-ans.h (module 'lora'): ns3::LinkCheckAns [class]
    module.add_class('LinkCheckAns', parent=root_module['ns3::LoRaMacCommand'])
    ## link-check-req.h (module 'lora'): ns3::LinkCheckReq [class]
    module.add_class('LinkCheckReq', parent=root_module['ns3::LoRaMacCommand'])
    ## lora-gw-phy.h (module 'lora'): ns3::LoRaGwPhy [class]
    module.add_class('LoRaGwPhy', parent=root_module['ns3::LoRaPhy'])
    ## lora-net-device.h (module 'lora'): ns3::LoRaNetDevice [class]
    module.add_class('LoRaNetDevice', parent=root_module['ns3::NetDevice'])
    ## lora-net-device.h (module 'lora'): ns3::LoRaNetDevice::State [enumeration]
    module.add_enum('State', ['IDLE', 'TIMEOUT', 'TX', 'RX', 'RETRANSMISSION', 'RX1_PENDING', 'RX2_PENDING', 'BEACON'], outer_class=root_module['ns3::LoRaNetDevice'])
    ## lora-rs-net-device.h (module 'lora'): ns3::LoRaRsNetDevice [class]
    module.add_class('LoRaRsNetDevice', parent=root_module['ns3::LoRaNetDevice'])
    ## queue-item.h (module 'network'): ns3::QueueDiscItem [class]
    module.add_class('QueueDiscItem', import_from_module='ns.network', parent=root_module['ns3::QueueItem'])
    ## lora-gw-net-device.h (module 'lora'): ns3::LoRaGwNetDevice [class]
    module.add_class('LoRaGwNetDevice', parent=root_module['ns3::LoRaNetDevice'])
    ## lora-gw-net-device.h (module 'lora'): ns3::LoRaGwNetDevice::DeviceInfo [struct]
    module.add_class('DeviceInfo', outer_class=root_module['ns3::LoRaGwNetDevice'])
    typehandlers.add_type_alias(u'ns3::Callback< std::tuple< unsigned short, unsigned char, unsigned char >, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LoRaGwNetDevice::SettingCallback')
    typehandlers.add_type_alias(u'ns3::Callback< std::tuple< unsigned short, unsigned char, unsigned char >, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LoRaGwNetDevice::SettingCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< std::tuple< unsigned short, unsigned char, unsigned char >, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LoRaGwNetDevice::SettingCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< void, double, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LoRaGwNetDevice::RssiCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, double, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LoRaGwNetDevice::RssiCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, double, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LoRaGwNetDevice::RssiCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LoRaGwNetDevice::PowerCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LoRaGwNetDevice::PowerCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LoRaGwNetDevice::PowerCallback&')
    ## lora-rs-gw-net-device.h (module 'lora'): ns3::LoRaRsGwNetDevice [class]
    module.add_class('LoRaRsGwNetDevice', parent=root_module['ns3::LoRaGwNetDevice'])
    ## lora-rs-gw-net-device.h (module 'lora'): ns3::LoRaRsGwNetDevice::DeviceInfo [struct]
    module.add_class('DeviceInfo', outer_class=root_module['ns3::LoRaRsGwNetDevice'])
    typehandlers.add_type_alias(u'ns3::Callback< std::tuple< unsigned short, unsigned char, unsigned char >, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LoRaRsGwNetDevice::SettingCallback')
    typehandlers.add_type_alias(u'ns3::Callback< std::tuple< unsigned short, unsigned char, unsigned char >, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LoRaRsGwNetDevice::SettingCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< std::tuple< unsigned short, unsigned char, unsigned char >, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LoRaRsGwNetDevice::SettingCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< void, double, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LoRaRsGwNetDevice::RssiCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, double, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LoRaRsGwNetDevice::RssiCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, double, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LoRaRsGwNetDevice::RssiCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LoRaRsGwNetDevice::PowerCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LoRaRsGwNetDevice::PowerCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LoRaRsGwNetDevice::PowerCallback&')
    module.add_container('std::list< ns3::Ptr< ns3::LoRaMacCommand > >', 'ns3::Ptr< ns3::LoRaMacCommand >', container_type=u'list')
    module.add_container('std::list< std::tuple< unsigned char, unsigned char > >', 'std::tuple< unsigned char, unsigned char >', container_type=u'list')
    module.add_container('std::vector< double >', 'double', container_type=u'vector')
    module.add_container('ns3::Bands', 'ns3::BandInfo', container_type=u'vector')
    typehandlers.add_type_alias(u'std::vector< double >', u'ns3::Values')
    typehandlers.add_type_alias(u'std::vector< double >*', u'ns3::Values*')
    typehandlers.add_type_alias(u'std::vector< double >&', u'ns3::Values&')
    typehandlers.add_type_alias(u'std::vector< ns3::BandInfo >', u'ns3::Bands')
    typehandlers.add_type_alias(u'std::vector< ns3::BandInfo >*', u'ns3::Bands*')
    typehandlers.add_type_alias(u'std::vector< ns3::BandInfo >&', u'ns3::Bands&')
    typehandlers.add_type_alias(u'uint32_t', u'ns3::SpectrumModelUid_t')
    typehandlers.add_type_alias(u'uint32_t*', u'ns3::SpectrumModelUid_t*')
    typehandlers.add_type_alias(u'uint32_t&', u'ns3::SpectrumModelUid_t&')
    typehandlers.add_type_alias(u'ns3::Vector3D', u'ns3::Vector')
    typehandlers.add_type_alias(u'ns3::Vector3D*', u'ns3::Vector*')
    typehandlers.add_type_alias(u'ns3::Vector3D&', u'ns3::Vector&')
    module.add_typedef(root_module['ns3::Vector3D'], 'Vector')
    typehandlers.add_type_alias(u'ns3::Vector3DValue', u'ns3::VectorValue')
    typehandlers.add_type_alias(u'ns3::Vector3DValue*', u'ns3::VectorValue*')
    typehandlers.add_type_alias(u'ns3::Vector3DValue&', u'ns3::VectorValue&')
    module.add_typedef(root_module['ns3::Vector3DValue'], 'VectorValue')
    typehandlers.add_type_alias(u'ns3::Vector3DChecker', u'ns3::VectorChecker')
    typehandlers.add_type_alias(u'ns3::Vector3DChecker*', u'ns3::VectorChecker*')
    typehandlers.add_type_alias(u'ns3::Vector3DChecker&', u'ns3::VectorChecker&')
    module.add_typedef(root_module['ns3::Vector3DChecker'], 'VectorChecker')
    typehandlers.add_type_alias(u'ns3::LoRaMacCommandCid', u'ns3::LoRaMacCommandCid')
    typehandlers.add_type_alias(u'ns3::LoRaMacCommandCid*', u'ns3::LoRaMacCommandCid*')
    typehandlers.add_type_alias(u'ns3::LoRaMacCommandCid&', u'ns3::LoRaMacCommandCid&')
    typehandlers.add_type_alias(u'ns3::LoRaMacCommandDirection', u'ns3::LoRaMacCommandDirection')
    typehandlers.add_type_alias(u'ns3::LoRaMacCommandDirection*', u'ns3::LoRaMacCommandDirection*')
    typehandlers.add_type_alias(u'ns3::LoRaMacCommandDirection&', u'ns3::LoRaMacCommandDirection&')
    typehandlers.add_type_alias(u'ns3::Callback< bool, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::GenericPhyTxStartCallback')
    typehandlers.add_type_alias(u'ns3::Callback< bool, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::GenericPhyTxStartCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< bool, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::GenericPhyTxStartCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::GenericPhyTxEndCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::GenericPhyTxEndCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::GenericPhyTxEndCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::GenericPhyRxStartCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::GenericPhyRxStartCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::GenericPhyRxStartCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::GenericPhyRxEndErrorCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::GenericPhyRxEndErrorCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::GenericPhyRxEndErrorCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::GenericPhyRxEndOkCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::GenericPhyRxEndOkCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::GenericPhyRxEndOkCallback&')
    
    ## Register a nested module for the namespace FatalImpl
    
    nested_module = module.add_cpp_namespace('FatalImpl')
    register_types_ns3_FatalImpl(nested_module)
    
    
    ## Register a nested module for the namespace Hash
    
    nested_module = module.add_cpp_namespace('Hash')
    register_types_ns3_Hash(nested_module)
    
    
    ## Register a nested module for the namespace TracedValueCallback
    
    nested_module = module.add_cpp_namespace('TracedValueCallback')
    register_types_ns3_TracedValueCallback(nested_module)
    
    
    ## Register a nested module for the namespace internal
    
    nested_module = module.add_cpp_namespace('internal')
    register_types_ns3_internal(nested_module)
    

def register_types_ns3_FatalImpl(module):
    root_module = module.get_root()
    

def register_types_ns3_Hash(module):
    root_module = module.get_root()
    
    ## hash-function.h (module 'core'): ns3::Hash::Implementation [class]
    module.add_class('Implementation', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >'])
    typehandlers.add_type_alias(u'uint32_t ( * ) ( char const *, std::size_t const )', u'ns3::Hash::Hash32Function_ptr')
    typehandlers.add_type_alias(u'uint32_t ( * ) ( char const *, std::size_t const )*', u'ns3::Hash::Hash32Function_ptr*')
    typehandlers.add_type_alias(u'uint32_t ( * ) ( char const *, std::size_t const )&', u'ns3::Hash::Hash32Function_ptr&')
    typehandlers.add_type_alias(u'uint64_t ( * ) ( char const *, std::size_t const )', u'ns3::Hash::Hash64Function_ptr')
    typehandlers.add_type_alias(u'uint64_t ( * ) ( char const *, std::size_t const )*', u'ns3::Hash::Hash64Function_ptr*')
    typehandlers.add_type_alias(u'uint64_t ( * ) ( char const *, std::size_t const )&', u'ns3::Hash::Hash64Function_ptr&')
    
    ## Register a nested module for the namespace Function
    
    nested_module = module.add_cpp_namespace('Function')
    register_types_ns3_Hash_Function(nested_module)
    

def register_types_ns3_Hash_Function(module):
    root_module = module.get_root()
    
    ## hash-fnv.h (module 'core'): ns3::Hash::Function::Fnv1a [class]
    module.add_class('Fnv1a', import_from_module='ns.core', parent=root_module['ns3::Hash::Implementation'])
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash32 [class]
    module.add_class('Hash32', import_from_module='ns.core', parent=root_module['ns3::Hash::Implementation'])
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash64 [class]
    module.add_class('Hash64', import_from_module='ns.core', parent=root_module['ns3::Hash::Implementation'])
    ## hash-murmur3.h (module 'core'): ns3::Hash::Function::Murmur3 [class]
    module.add_class('Murmur3', import_from_module='ns.core', parent=root_module['ns3::Hash::Implementation'])

def register_types_ns3_TracedValueCallback(module):
    root_module = module.get_root()
    
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Time, ns3::Time )', u'ns3::TracedValueCallback::Time')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Time, ns3::Time )*', u'ns3::TracedValueCallback::Time*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Time, ns3::Time )&', u'ns3::TracedValueCallback::Time&')
    typehandlers.add_type_alias(u'void ( * ) ( bool, bool )', u'ns3::TracedValueCallback::Bool')
    typehandlers.add_type_alias(u'void ( * ) ( bool, bool )*', u'ns3::TracedValueCallback::Bool*')
    typehandlers.add_type_alias(u'void ( * ) ( bool, bool )&', u'ns3::TracedValueCallback::Bool&')
    typehandlers.add_type_alias(u'void ( * ) ( int8_t, int8_t )', u'ns3::TracedValueCallback::Int8')
    typehandlers.add_type_alias(u'void ( * ) ( int8_t, int8_t )*', u'ns3::TracedValueCallback::Int8*')
    typehandlers.add_type_alias(u'void ( * ) ( int8_t, int8_t )&', u'ns3::TracedValueCallback::Int8&')
    typehandlers.add_type_alias(u'void ( * ) ( uint8_t, uint8_t )', u'ns3::TracedValueCallback::Uint8')
    typehandlers.add_type_alias(u'void ( * ) ( uint8_t, uint8_t )*', u'ns3::TracedValueCallback::Uint8*')
    typehandlers.add_type_alias(u'void ( * ) ( uint8_t, uint8_t )&', u'ns3::TracedValueCallback::Uint8&')
    typehandlers.add_type_alias(u'void ( * ) ( int16_t, int16_t )', u'ns3::TracedValueCallback::Int16')
    typehandlers.add_type_alias(u'void ( * ) ( int16_t, int16_t )*', u'ns3::TracedValueCallback::Int16*')
    typehandlers.add_type_alias(u'void ( * ) ( int16_t, int16_t )&', u'ns3::TracedValueCallback::Int16&')
    typehandlers.add_type_alias(u'void ( * ) ( uint16_t, uint16_t )', u'ns3::TracedValueCallback::Uint16')
    typehandlers.add_type_alias(u'void ( * ) ( uint16_t, uint16_t )*', u'ns3::TracedValueCallback::Uint16*')
    typehandlers.add_type_alias(u'void ( * ) ( uint16_t, uint16_t )&', u'ns3::TracedValueCallback::Uint16&')
    typehandlers.add_type_alias(u'void ( * ) ( int32_t, int32_t )', u'ns3::TracedValueCallback::Int32')
    typehandlers.add_type_alias(u'void ( * ) ( int32_t, int32_t )*', u'ns3::TracedValueCallback::Int32*')
    typehandlers.add_type_alias(u'void ( * ) ( int32_t, int32_t )&', u'ns3::TracedValueCallback::Int32&')
    typehandlers.add_type_alias(u'void ( * ) ( uint32_t, uint32_t )', u'ns3::TracedValueCallback::Uint32')
    typehandlers.add_type_alias(u'void ( * ) ( uint32_t, uint32_t )*', u'ns3::TracedValueCallback::Uint32*')
    typehandlers.add_type_alias(u'void ( * ) ( uint32_t, uint32_t )&', u'ns3::TracedValueCallback::Uint32&')
    typehandlers.add_type_alias(u'void ( * ) ( double, double )', u'ns3::TracedValueCallback::Double')
    typehandlers.add_type_alias(u'void ( * ) ( double, double )*', u'ns3::TracedValueCallback::Double*')
    typehandlers.add_type_alias(u'void ( * ) ( double, double )&', u'ns3::TracedValueCallback::Double&')
    typehandlers.add_type_alias(u'void ( * ) (  )', u'ns3::TracedValueCallback::Void')
    typehandlers.add_type_alias(u'void ( * ) (  )*', u'ns3::TracedValueCallback::Void*')
    typehandlers.add_type_alias(u'void ( * ) (  )&', u'ns3::TracedValueCallback::Void&')

def register_types_ns3_internal(module):
    root_module = module.get_root()
    

def register_methods(root_module):
    register_Ns3Address_methods(root_module, root_module['ns3::Address'])
    register_Ns3ApplicationContainer_methods(root_module, root_module['ns3::ApplicationContainer'])
    register_Ns3AsciiTraceHelper_methods(root_module, root_module['ns3::AsciiTraceHelper'])
    register_Ns3AsciiTraceHelperForDevice_methods(root_module, root_module['ns3::AsciiTraceHelperForDevice'])
    register_Ns3AttributeConstructionList_methods(root_module, root_module['ns3::AttributeConstructionList'])
    register_Ns3AttributeConstructionListItem_methods(root_module, root_module['ns3::AttributeConstructionList::Item'])
    register_Ns3BandInfo_methods(root_module, root_module['ns3::BandInfo'])
    register_Ns3Buffer_methods(root_module, root_module['ns3::Buffer'])
    register_Ns3BufferIterator_methods(root_module, root_module['ns3::Buffer::Iterator'])
    register_Ns3ByteTagIterator_methods(root_module, root_module['ns3::ByteTagIterator'])
    register_Ns3ByteTagIteratorItem_methods(root_module, root_module['ns3::ByteTagIterator::Item'])
    register_Ns3ByteTagList_methods(root_module, root_module['ns3::ByteTagList'])
    register_Ns3ByteTagListIterator_methods(root_module, root_module['ns3::ByteTagList::Iterator'])
    register_Ns3ByteTagListIteratorItem_methods(root_module, root_module['ns3::ByteTagList::Iterator::Item'])
    register_Ns3CallbackBase_methods(root_module, root_module['ns3::CallbackBase'])
    register_Ns3DefaultDeleter__Ns3AttributeAccessor_methods(root_module, root_module['ns3::DefaultDeleter< ns3::AttributeAccessor >'])
    register_Ns3DefaultDeleter__Ns3AttributeChecker_methods(root_module, root_module['ns3::DefaultDeleter< ns3::AttributeChecker >'])
    register_Ns3DefaultDeleter__Ns3AttributeValue_methods(root_module, root_module['ns3::DefaultDeleter< ns3::AttributeValue >'])
    register_Ns3DefaultDeleter__Ns3CallbackImplBase_methods(root_module, root_module['ns3::DefaultDeleter< ns3::CallbackImplBase >'])
    register_Ns3DefaultDeleter__Ns3EventImpl_methods(root_module, root_module['ns3::DefaultDeleter< ns3::EventImpl >'])
    register_Ns3DefaultDeleter__Ns3HashImplementation_methods(root_module, root_module['ns3::DefaultDeleter< ns3::Hash::Implementation >'])
    register_Ns3DefaultDeleter__Ns3NixVector_methods(root_module, root_module['ns3::DefaultDeleter< ns3::NixVector >'])
    register_Ns3DefaultDeleter__Ns3OutputStreamWrapper_methods(root_module, root_module['ns3::DefaultDeleter< ns3::OutputStreamWrapper >'])
    register_Ns3DefaultDeleter__Ns3Packet_methods(root_module, root_module['ns3::DefaultDeleter< ns3::Packet >'])
    register_Ns3DefaultDeleter__Ns3SpectrumModel_methods(root_module, root_module['ns3::DefaultDeleter< ns3::SpectrumModel >'])
    register_Ns3DefaultDeleter__Ns3SpectrumSignalParameters_methods(root_module, root_module['ns3::DefaultDeleter< ns3::SpectrumSignalParameters >'])
    register_Ns3DefaultDeleter__Ns3SpectrumValue_methods(root_module, root_module['ns3::DefaultDeleter< ns3::SpectrumValue >'])
    register_Ns3DefaultDeleter__Ns3TraceSourceAccessor_methods(root_module, root_module['ns3::DefaultDeleter< ns3::TraceSourceAccessor >'])
    register_Ns3DeviceEnergyModelContainer_methods(root_module, root_module['ns3::DeviceEnergyModelContainer'])
    register_Ns3DeviceEnergyModelHelper_methods(root_module, root_module['ns3::DeviceEnergyModelHelper'])
    register_Ns3DeviceRxSettings_methods(root_module, root_module['ns3::DeviceRxSettings'])
    register_Ns3EnergySourceHelper_methods(root_module, root_module['ns3::EnergySourceHelper'])
    register_Ns3EventId_methods(root_module, root_module['ns3::EventId'])
    register_Ns3Hasher_methods(root_module, root_module['ns3::Hasher'])
    register_Ns3Ipv4Address_methods(root_module, root_module['ns3::Ipv4Address'])
    register_Ns3Ipv4Mask_methods(root_module, root_module['ns3::Ipv4Mask'])
    register_Ns3Ipv6Address_methods(root_module, root_module['ns3::Ipv6Address'])
    register_Ns3Ipv6Prefix_methods(root_module, root_module['ns3::Ipv6Prefix'])
    register_Ns3LoRaEnergySourceHelper_methods(root_module, root_module['ns3::LoRaEnergySourceHelper'])
    register_Ns3LoRaRadioEnergyModelHelper_methods(root_module, root_module['ns3::LoRaRadioEnergyModelHelper'])
    register_Ns3Mac32Address_methods(root_module, root_module['ns3::Mac32Address'])
    register_Ns3Mac48Address_methods(root_module, root_module['ns3::Mac48Address'])
    register_Ns3Mac8Address_methods(root_module, root_module['ns3::Mac8Address'])
    register_Ns3NetDeviceContainer_methods(root_module, root_module['ns3::NetDeviceContainer'])
    register_Ns3NodeContainer_methods(root_module, root_module['ns3::NodeContainer'])
    register_Ns3ObjectBase_methods(root_module, root_module['ns3::ObjectBase'])
    register_Ns3ObjectDeleter_methods(root_module, root_module['ns3::ObjectDeleter'])
    register_Ns3ObjectFactory_methods(root_module, root_module['ns3::ObjectFactory'])
    register_Ns3PacketId_methods(root_module, root_module['ns3::PacketId'])
    register_Ns3PacketMetadata_methods(root_module, root_module['ns3::PacketMetadata'])
    register_Ns3PacketMetadataItem_methods(root_module, root_module['ns3::PacketMetadata::Item'])
    register_Ns3PacketMetadataItemIterator_methods(root_module, root_module['ns3::PacketMetadata::ItemIterator'])
    register_Ns3PacketStats_methods(root_module, root_module['ns3::PacketStats'])
    register_Ns3PacketTagIterator_methods(root_module, root_module['ns3::PacketTagIterator'])
    register_Ns3PacketTagIteratorItem_methods(root_module, root_module['ns3::PacketTagIterator::Item'])
    register_Ns3PacketTagList_methods(root_module, root_module['ns3::PacketTagList'])
    register_Ns3PacketTagListTagData_methods(root_module, root_module['ns3::PacketTagList::TagData'])
    register_Ns3PcapFile_methods(root_module, root_module['ns3::PcapFile'])
    register_Ns3PcapHelper_methods(root_module, root_module['ns3::PcapHelper'])
    register_Ns3PcapHelperForDevice_methods(root_module, root_module['ns3::PcapHelperForDevice'])
    register_Ns3SimpleRefCount__Ns3Object_Ns3ObjectBase_Ns3ObjectDeleter_methods(root_module, root_module['ns3::SimpleRefCount< ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter >'])
    register_Ns3Simulator_methods(root_module, root_module['ns3::Simulator'])
    register_Ns3Tag_methods(root_module, root_module['ns3::Tag'])
    register_Ns3TagBuffer_methods(root_module, root_module['ns3::TagBuffer'])
    register_Ns3TimeWithUnit_methods(root_module, root_module['ns3::TimeWithUnit'])
    register_Ns3TracedValue__Double_methods(root_module, root_module['ns3::TracedValue< double >'])
    register_Ns3TracedValue__Ns3LoRaPhyState_methods(root_module, root_module['ns3::TracedValue< ns3::LoRaPhy::State >'])
    register_Ns3TypeId_methods(root_module, root_module['ns3::TypeId'])
    register_Ns3TypeIdAttributeInformation_methods(root_module, root_module['ns3::TypeId::AttributeInformation'])
    register_Ns3TypeIdTraceSourceInformation_methods(root_module, root_module['ns3::TypeId::TraceSourceInformation'])
    register_Ns3Vector2D_methods(root_module, root_module['ns3::Vector2D'])
    register_Ns3Vector3D_methods(root_module, root_module['ns3::Vector3D'])
    register_Ns3Empty_methods(root_module, root_module['ns3::empty'])
    register_Ns3Int64x64_t_methods(root_module, root_module['ns3::int64x64_t'])
    register_Ns3Chunk_methods(root_module, root_module['ns3::Chunk'])
    register_Ns3Header_methods(root_module, root_module['ns3::Header'])
    register_Ns3LoRaHelper_methods(root_module, root_module['ns3::LoRaHelper'])
    register_Ns3LoRaMacHeader_methods(root_module, root_module['ns3::LoRaMacHeader'])
    register_Ns3LoRaPhyHeader_methods(root_module, root_module['ns3::LoRaPhyHeader'])
    register_Ns3Object_methods(root_module, root_module['ns3::Object'])
    register_Ns3ObjectAggregateIterator_methods(root_module, root_module['ns3::Object::AggregateIterator'])
    register_Ns3PcapFileWrapper_methods(root_module, root_module['ns3::PcapFileWrapper'])
    register_Ns3PropagationDelayModel_methods(root_module, root_module['ns3::PropagationDelayModel'])
    register_Ns3PropagationLossModel_methods(root_module, root_module['ns3::PropagationLossModel'])
    register_Ns3RandomPropagationDelayModel_methods(root_module, root_module['ns3::RandomPropagationDelayModel'])
    register_Ns3RandomPropagationLossModel_methods(root_module, root_module['ns3::RandomPropagationLossModel'])
    register_Ns3RandomVariableStream_methods(root_module, root_module['ns3::RandomVariableStream'])
    register_Ns3RangePropagationLossModel_methods(root_module, root_module['ns3::RangePropagationLossModel'])
    register_Ns3SequentialRandomVariable_methods(root_module, root_module['ns3::SequentialRandomVariable'])
    register_Ns3SimpleRefCount__Ns3AttributeAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeAccessor__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >'])
    register_Ns3SimpleRefCount__Ns3AttributeChecker_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeChecker__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >'])
    register_Ns3SimpleRefCount__Ns3AttributeValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeValue__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >'])
    register_Ns3SimpleRefCount__Ns3CallbackImplBase_Ns3Empty_Ns3DefaultDeleter__lt__ns3CallbackImplBase__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >'])
    register_Ns3SimpleRefCount__Ns3EventImpl_Ns3Empty_Ns3DefaultDeleter__lt__ns3EventImpl__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >'])
    register_Ns3SimpleRefCount__Ns3HashImplementation_Ns3Empty_Ns3DefaultDeleter__lt__ns3HashImplementation__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >'])
    register_Ns3SimpleRefCount__Ns3NixVector_Ns3Empty_Ns3DefaultDeleter__lt__ns3NixVector__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >'])
    register_Ns3SimpleRefCount__Ns3OutputStreamWrapper_Ns3Empty_Ns3DefaultDeleter__lt__ns3OutputStreamWrapper__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> >'])
    register_Ns3SimpleRefCount__Ns3Packet_Ns3Empty_Ns3DefaultDeleter__lt__ns3Packet__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >'])
    register_Ns3SimpleRefCount__Ns3QueueItem_Ns3Empty_Ns3DefaultDeleter__lt__ns3QueueItem__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::QueueItem, ns3::empty, ns3::DefaultDeleter<ns3::QueueItem> >'])
    register_Ns3SimpleRefCount__Ns3SpectrumModel_Ns3Empty_Ns3DefaultDeleter__lt__ns3SpectrumModel__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumModel> >'])
    register_Ns3SimpleRefCount__Ns3SpectrumSignalParameters_Ns3Empty_Ns3DefaultDeleter__lt__ns3SpectrumSignalParameters__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumSignalParameters> >'])
    register_Ns3SimpleRefCount__Ns3SpectrumValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3SpectrumValue__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumValue> >'])
    register_Ns3SimpleRefCount__Ns3TraceSourceAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3TraceSourceAccessor__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >'])
    register_Ns3SpectrumModel_methods(root_module, root_module['ns3::SpectrumModel'])
    register_Ns3SpectrumPhy_methods(root_module, root_module['ns3::SpectrumPhy'])
    register_Ns3SpectrumPropagationLossModel_methods(root_module, root_module['ns3::SpectrumPropagationLossModel'])
    register_Ns3SpectrumSignalParameters_methods(root_module, root_module['ns3::SpectrumSignalParameters'])
    register_Ns3SpectrumValue_methods(root_module, root_module['ns3::SpectrumValue'])
    register_Ns3ThreeLogDistancePropagationLossModel_methods(root_module, root_module['ns3::ThreeLogDistancePropagationLossModel'])
    register_Ns3Time_methods(root_module, root_module['ns3::Time'])
    register_Ns3TraceSourceAccessor_methods(root_module, root_module['ns3::TraceSourceAccessor'])
    register_Ns3Trailer_methods(root_module, root_module['ns3::Trailer'])
    register_Ns3TriangularRandomVariable_methods(root_module, root_module['ns3::TriangularRandomVariable'])
    register_Ns3TwoRayGroundPropagationLossModel_methods(root_module, root_module['ns3::TwoRayGroundPropagationLossModel'])
    register_Ns3UniformRandomVariable_methods(root_module, root_module['ns3::UniformRandomVariable'])
    register_Ns3WeibullRandomVariable_methods(root_module, root_module['ns3::WeibullRandomVariable'])
    register_Ns3ZetaRandomVariable_methods(root_module, root_module['ns3::ZetaRandomVariable'])
    register_Ns3ZipfRandomVariable_methods(root_module, root_module['ns3::ZipfRandomVariable'])
    register_Ns3Application_methods(root_module, root_module['ns3::Application'])
    register_Ns3AttributeAccessor_methods(root_module, root_module['ns3::AttributeAccessor'])
    register_Ns3AttributeChecker_methods(root_module, root_module['ns3::AttributeChecker'])
    register_Ns3AttributeValue_methods(root_module, root_module['ns3::AttributeValue'])
    register_Ns3BooleanChecker_methods(root_module, root_module['ns3::BooleanChecker'])
    register_Ns3BooleanValue_methods(root_module, root_module['ns3::BooleanValue'])
    register_Ns3CallbackChecker_methods(root_module, root_module['ns3::CallbackChecker'])
    register_Ns3CallbackImplBase_methods(root_module, root_module['ns3::CallbackImplBase'])
    register_Ns3CallbackValue_methods(root_module, root_module['ns3::CallbackValue'])
    register_Ns3Channel_methods(root_module, root_module['ns3::Channel'])
    register_Ns3ConstantRandomVariable_methods(root_module, root_module['ns3::ConstantRandomVariable'])
    register_Ns3ConstantSpeedPropagationDelayModel_methods(root_module, root_module['ns3::ConstantSpeedPropagationDelayModel'])
    register_Ns3DeterministicRandomVariable_methods(root_module, root_module['ns3::DeterministicRandomVariable'])
    register_Ns3DeviceEnergyModel_methods(root_module, root_module['ns3::DeviceEnergyModel'])
    register_Ns3DoubleValue_methods(root_module, root_module['ns3::DoubleValue'])
    register_Ns3EmpiricalRandomVariable_methods(root_module, root_module['ns3::EmpiricalRandomVariable'])
    register_Ns3EmptyAttributeAccessor_methods(root_module, root_module['ns3::EmptyAttributeAccessor'])
    register_Ns3EmptyAttributeChecker_methods(root_module, root_module['ns3::EmptyAttributeChecker'])
    register_Ns3EmptyAttributeValue_methods(root_module, root_module['ns3::EmptyAttributeValue'])
    register_Ns3EnergyHarvester_methods(root_module, root_module['ns3::EnergyHarvester'])
    register_Ns3EnergySource_methods(root_module, root_module['ns3::EnergySource'])
    register_Ns3EnergySourceContainer_methods(root_module, root_module['ns3::EnergySourceContainer'])
    register_Ns3EnumChecker_methods(root_module, root_module['ns3::EnumChecker'])
    register_Ns3EnumValue_methods(root_module, root_module['ns3::EnumValue'])
    register_Ns3ErlangRandomVariable_methods(root_module, root_module['ns3::ErlangRandomVariable'])
    register_Ns3EventImpl_methods(root_module, root_module['ns3::EventImpl'])
    register_Ns3ExponentialRandomVariable_methods(root_module, root_module['ns3::ExponentialRandomVariable'])
    register_Ns3FixedRssLossModel_methods(root_module, root_module['ns3::FixedRssLossModel'])
    register_Ns3FriisPropagationLossModel_methods(root_module, root_module['ns3::FriisPropagationLossModel'])
    register_Ns3GammaRandomVariable_methods(root_module, root_module['ns3::GammaRandomVariable'])
    register_Ns3GwTrailer_methods(root_module, root_module['ns3::GwTrailer'])
    register_Ns3IntegerValue_methods(root_module, root_module['ns3::IntegerValue'])
    register_Ns3Ipv4AddressChecker_methods(root_module, root_module['ns3::Ipv4AddressChecker'])
    register_Ns3Ipv4AddressValue_methods(root_module, root_module['ns3::Ipv4AddressValue'])
    register_Ns3Ipv4MaskChecker_methods(root_module, root_module['ns3::Ipv4MaskChecker'])
    register_Ns3Ipv4MaskValue_methods(root_module, root_module['ns3::Ipv4MaskValue'])
    register_Ns3Ipv6AddressChecker_methods(root_module, root_module['ns3::Ipv6AddressChecker'])
    register_Ns3Ipv6AddressValue_methods(root_module, root_module['ns3::Ipv6AddressValue'])
    register_Ns3Ipv6PrefixChecker_methods(root_module, root_module['ns3::Ipv6PrefixChecker'])
    register_Ns3Ipv6PrefixValue_methods(root_module, root_module['ns3::Ipv6PrefixValue'])
    register_Ns3LoRaApplication_methods(root_module, root_module['ns3::LoRaApplication'])
    register_Ns3LoRaErrorModel_methods(root_module, root_module['ns3::LoRaErrorModel'])
    register_Ns3LoRaMacCommand_methods(root_module, root_module['ns3::LoRaMacCommand'])
    register_Ns3LoRaMacTrailer_methods(root_module, root_module['ns3::LoRaMacTrailer'])
    register_Ns3LoRaNetwork_methods(root_module, root_module['ns3::LoRaNetwork'])
    register_Ns3LoRaNetworkApplication_methods(root_module, root_module['ns3::LoRaNetworkApplication'])
    register_Ns3LoRaNetworkTrailer_methods(root_module, root_module['ns3::LoRaNetworkTrailer'])
    register_Ns3LoRaNoPowerApplication_methods(root_module, root_module['ns3::LoRaNoPowerApplication'])
    register_Ns3LoRaPhy_methods(root_module, root_module['ns3::LoRaPhy'])
    register_Ns3LoRaPowerApplication_methods(root_module, root_module['ns3::LoRaPowerApplication'])
    register_Ns3LoRaRadioEnergyModel_methods(root_module, root_module['ns3::LoRaRadioEnergyModel'])
    register_Ns3LoRaSinkApplication_methods(root_module, root_module['ns3::LoRaSinkApplication'])
    register_Ns3LoRaSpectrumSignalParameters_methods(root_module, root_module['ns3::LoRaSpectrumSignalParameters'])
    register_Ns3LoRaTestApplication_methods(root_module, root_module['ns3::LoRaTestApplication'])
    register_Ns3LogDistancePropagationLossModel_methods(root_module, root_module['ns3::LogDistancePropagationLossModel'])
    register_Ns3LogNormalRandomVariable_methods(root_module, root_module['ns3::LogNormalRandomVariable'])
    register_Ns3Mac32AddressChecker_methods(root_module, root_module['ns3::Mac32AddressChecker'])
    register_Ns3Mac32AddressValue_methods(root_module, root_module['ns3::Mac32AddressValue'])
    register_Ns3Mac48AddressChecker_methods(root_module, root_module['ns3::Mac48AddressChecker'])
    register_Ns3Mac48AddressValue_methods(root_module, root_module['ns3::Mac48AddressValue'])
    register_Ns3MatrixPropagationLossModel_methods(root_module, root_module['ns3::MatrixPropagationLossModel'])
    register_Ns3MobilityModel_methods(root_module, root_module['ns3::MobilityModel'])
    register_Ns3NakagamiPropagationLossModel_methods(root_module, root_module['ns3::NakagamiPropagationLossModel'])
    register_Ns3NetDevice_methods(root_module, root_module['ns3::NetDevice'])
    register_Ns3NewChannelAns_methods(root_module, root_module['ns3::NewChannelAns'])
    register_Ns3NewChannelReq_methods(root_module, root_module['ns3::NewChannelReq'])
    register_Ns3NixVector_methods(root_module, root_module['ns3::NixVector'])
    register_Ns3Node_methods(root_module, root_module['ns3::Node'])
    register_Ns3NormalRandomVariable_methods(root_module, root_module['ns3::NormalRandomVariable'])
    register_Ns3ObjectFactoryChecker_methods(root_module, root_module['ns3::ObjectFactoryChecker'])
    register_Ns3ObjectFactoryValue_methods(root_module, root_module['ns3::ObjectFactoryValue'])
    register_Ns3OutputStreamWrapper_methods(root_module, root_module['ns3::OutputStreamWrapper'])
    register_Ns3Packet_methods(root_module, root_module['ns3::Packet'])
    register_Ns3ParetoRandomVariable_methods(root_module, root_module['ns3::ParetoRandomVariable'])
    register_Ns3QueueItem_methods(root_module, root_module['ns3::QueueItem'])
    register_Ns3RxParamSetupAns_methods(root_module, root_module['ns3::RxParamSetupAns'])
    register_Ns3RxParamSetupReq_methods(root_module, root_module['ns3::RxParamSetupReq'])
    register_Ns3RxTimingSetupAns_methods(root_module, root_module['ns3::RxTimingSetupAns'])
    register_Ns3RxTimingSetupReq_methods(root_module, root_module['ns3::RxTimingSetupReq'])
    register_Ns3SpectrumChannel_methods(root_module, root_module['ns3::SpectrumChannel'])
    register_Ns3TimeValue_methods(root_module, root_module['ns3::TimeValue'])
    register_Ns3TypeIdChecker_methods(root_module, root_module['ns3::TypeIdChecker'])
    register_Ns3TypeIdValue_methods(root_module, root_module['ns3::TypeIdValue'])
    register_Ns3UintegerValue_methods(root_module, root_module['ns3::UintegerValue'])
    register_Ns3Vector2DChecker_methods(root_module, root_module['ns3::Vector2DChecker'])
    register_Ns3Vector2DValue_methods(root_module, root_module['ns3::Vector2DValue'])
    register_Ns3Vector3DChecker_methods(root_module, root_module['ns3::Vector3DChecker'])
    register_Ns3Vector3DValue_methods(root_module, root_module['ns3::Vector3DValue'])
    register_Ns3AddressChecker_methods(root_module, root_module['ns3::AddressChecker'])
    register_Ns3AddressValue_methods(root_module, root_module['ns3::AddressValue'])
    register_Ns3CallbackImpl__Bool_Ns3Ptr__lt__ns3NetDevice__gt___Ns3Ptr__lt__const_ns3Packet__gt___Unsigned_short_Const_ns3Address___amp___Const_ns3Address___amp___Ns3NetDevicePacketType_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Bool_Ns3Ptr__lt__ns3NetDevice__gt___Ns3Ptr__lt__const_ns3Packet__gt___Unsigned_short_Const_ns3Address___amp___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Bool_Ns3Ptr__lt__ns3Packet__gt___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< bool, ns3::Ptr<ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Ns3ObjectBase___star___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Void_Double_Double_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< void, double, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Void_Ns3LoRaPhyState_Ns3LoRaPhyState_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< void, ns3::LoRaPhy::State, ns3::LoRaPhy::State, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Void_Ns3Ptr__lt__const_ns3MobilityModel__gt___Ns3Ptr__lt__const_ns3MobilityModel__gt___Double_Double_Double_Double_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< void, ns3::Ptr<const ns3::MobilityModel>, ns3::Ptr<const ns3::MobilityModel>, double, double, double, double, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Void_Ns3Ptr__lt__const_ns3MobilityModel__gt___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< void, ns3::Ptr<const ns3::MobilityModel>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Void_Ns3Ptr__lt__const_ns3Packet__gt___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< void, ns3::Ptr<const ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Void_Ns3Ptr__lt__const_ns3SpectrumPhy__gt___Ns3Ptr__lt__const_ns3SpectrumPhy__gt___Double_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< void, ns3::Ptr<const ns3::SpectrumPhy>, ns3::Ptr<const ns3::SpectrumPhy>, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Void_Ns3Ptr__lt__ns3NetDevice__gt___Ns3Ptr__lt__const_ns3Packet__gt___Unsigned_short_Const_ns3Address___amp___Const_ns3Address___amp___Ns3NetDevicePacketType_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< void, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Void_Ns3Ptr__lt__ns3NetDevice__gt___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< void, ns3::Ptr<ns3::NetDevice>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Void_Ns3Ptr__lt__ns3SpectrumSignalParameters__gt___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< void, ns3::Ptr<ns3::SpectrumSignalParameters>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Void_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3CallbackImpl__Void_StdBasic_string__lt__char__gt___StdBasic_string__lt__char__gt___Bool_Double_Double_Double_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, root_module['ns3::CallbackImpl< void, std::basic_string<char>, std::basic_string<char>, bool, double, double, double, ns3::empty, ns3::empty, ns3::empty >'])
    register_Ns3DevStatusAns_methods(root_module, root_module['ns3::DevStatusAns'])
    register_Ns3DevStatusReq_methods(root_module, root_module['ns3::DevStatusReq'])
    register_Ns3DutyCycleAns_methods(root_module, root_module['ns3::DutyCycleAns'])
    register_Ns3DutyCycleReq_methods(root_module, root_module['ns3::DutyCycleReq'])
    register_Ns3LinkAdrAns_methods(root_module, root_module['ns3::LinkAdrAns'])
    register_Ns3LinkAdrReq_methods(root_module, root_module['ns3::LinkAdrReq'])
    register_Ns3LinkCheckAns_methods(root_module, root_module['ns3::LinkCheckAns'])
    register_Ns3LinkCheckReq_methods(root_module, root_module['ns3::LinkCheckReq'])
    register_Ns3LoRaGwPhy_methods(root_module, root_module['ns3::LoRaGwPhy'])
    register_Ns3LoRaNetDevice_methods(root_module, root_module['ns3::LoRaNetDevice'])
    register_Ns3LoRaRsNetDevice_methods(root_module, root_module['ns3::LoRaRsNetDevice'])
    register_Ns3QueueDiscItem_methods(root_module, root_module['ns3::QueueDiscItem'])
    register_Ns3LoRaGwNetDevice_methods(root_module, root_module['ns3::LoRaGwNetDevice'])
    register_Ns3LoRaGwNetDeviceDeviceInfo_methods(root_module, root_module['ns3::LoRaGwNetDevice::DeviceInfo'])
    register_Ns3LoRaRsGwNetDevice_methods(root_module, root_module['ns3::LoRaRsGwNetDevice'])
    register_Ns3LoRaRsGwNetDeviceDeviceInfo_methods(root_module, root_module['ns3::LoRaRsGwNetDevice::DeviceInfo'])
    register_Ns3HashImplementation_methods(root_module, root_module['ns3::Hash::Implementation'])
    register_Ns3HashFunctionFnv1a_methods(root_module, root_module['ns3::Hash::Function::Fnv1a'])
    register_Ns3HashFunctionHash32_methods(root_module, root_module['ns3::Hash::Function::Hash32'])
    register_Ns3HashFunctionHash64_methods(root_module, root_module['ns3::Hash::Function::Hash64'])
    register_Ns3HashFunctionMurmur3_methods(root_module, root_module['ns3::Hash::Function::Murmur3'])
    return

def register_Ns3Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    ## address.h (module 'network'): ns3::Address::Address() [constructor]
    cls.add_constructor([])
    ## address.h (module 'network'): ns3::Address::Address(uint8_t type, uint8_t const * buffer, uint8_t len) [constructor]
    cls.add_constructor([param('uint8_t', 'type'), param('uint8_t const *', 'buffer'), param('uint8_t', 'len')])
    ## address.h (module 'network'): ns3::Address::Address(ns3::Address const & address) [constructor]
    cls.add_constructor([param('ns3::Address const &', 'address')])
    ## address.h (module 'network'): bool ns3::Address::CheckCompatible(uint8_t type, uint8_t len) const [member function]
    cls.add_method('CheckCompatible', 
                   'bool', 
                   [param('uint8_t', 'type'), param('uint8_t', 'len')], 
                   is_const=True)
    ## address.h (module 'network'): uint32_t ns3::Address::CopyAllFrom(uint8_t const * buffer, uint8_t len) [member function]
    cls.add_method('CopyAllFrom', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint8_t', 'len')])
    ## address.h (module 'network'): uint32_t ns3::Address::CopyAllTo(uint8_t * buffer, uint8_t len) const [member function]
    cls.add_method('CopyAllTo', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint8_t', 'len')], 
                   is_const=True)
    ## address.h (module 'network'): uint32_t ns3::Address::CopyFrom(uint8_t const * buffer, uint8_t len) [member function]
    cls.add_method('CopyFrom', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint8_t', 'len')])
    ## address.h (module 'network'): uint32_t ns3::Address::CopyTo(uint8_t * buffer) const [member function]
    cls.add_method('CopyTo', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer')], 
                   is_const=True)
    ## address.h (module 'network'): void ns3::Address::Deserialize(ns3::TagBuffer buffer) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'buffer')])
    ## address.h (module 'network'): uint8_t ns3::Address::GetLength() const [member function]
    cls.add_method('GetLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## address.h (module 'network'): uint32_t ns3::Address::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## address.h (module 'network'): bool ns3::Address::IsInvalid() const [member function]
    cls.add_method('IsInvalid', 
                   'bool', 
                   [], 
                   is_const=True)
    ## address.h (module 'network'): bool ns3::Address::IsMatchingType(uint8_t type) const [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('uint8_t', 'type')], 
                   is_const=True)
    ## address.h (module 'network'): static uint8_t ns3::Address::Register() [member function]
    cls.add_method('Register', 
                   'uint8_t', 
                   [], 
                   is_static=True)
    ## address.h (module 'network'): void ns3::Address::Serialize(ns3::TagBuffer buffer) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'buffer')], 
                   is_const=True)
    return

def register_Ns3ApplicationContainer_methods(root_module, cls):
    ## application-container.h (module 'network'): ns3::ApplicationContainer::ApplicationContainer(ns3::ApplicationContainer const & arg0) [constructor]
    cls.add_constructor([param('ns3::ApplicationContainer const &', 'arg0')])
    ## application-container.h (module 'network'): ns3::ApplicationContainer::ApplicationContainer() [constructor]
    cls.add_constructor([])
    ## application-container.h (module 'network'): ns3::ApplicationContainer::ApplicationContainer(ns3::Ptr<ns3::Application> application) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::Application >', 'application')])
    ## application-container.h (module 'network'): ns3::ApplicationContainer::ApplicationContainer(std::string name) [constructor]
    cls.add_constructor([param('std::string', 'name')])
    ## application-container.h (module 'network'): void ns3::ApplicationContainer::Add(ns3::ApplicationContainer other) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::ApplicationContainer', 'other')])
    ## application-container.h (module 'network'): void ns3::ApplicationContainer::Add(ns3::Ptr<ns3::Application> application) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Ptr< ns3::Application >', 'application')])
    ## application-container.h (module 'network'): void ns3::ApplicationContainer::Add(std::string name) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'name')])
    ## application-container.h (module 'network'): ns3::ApplicationContainer::Iterator ns3::ApplicationContainer::Begin() const [member function]
    cls.add_method('Begin', 
                   'ns3::ApplicationContainer::Iterator', 
                   [], 
                   is_const=True)
    ## application-container.h (module 'network'): ns3::ApplicationContainer::Iterator ns3::ApplicationContainer::End() const [member function]
    cls.add_method('End', 
                   'ns3::ApplicationContainer::Iterator', 
                   [], 
                   is_const=True)
    ## application-container.h (module 'network'): ns3::Ptr<ns3::Application> ns3::ApplicationContainer::Get(uint32_t i) const [member function]
    cls.add_method('Get', 
                   'ns3::Ptr< ns3::Application >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## application-container.h (module 'network'): uint32_t ns3::ApplicationContainer::GetN() const [member function]
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## application-container.h (module 'network'): void ns3::ApplicationContainer::Start(ns3::Time start) [member function]
    cls.add_method('Start', 
                   'void', 
                   [param('ns3::Time', 'start')])
    ## application-container.h (module 'network'): void ns3::ApplicationContainer::StartWithJitter(ns3::Time start, ns3::Ptr<ns3::RandomVariableStream> rv) [member function]
    cls.add_method('StartWithJitter', 
                   'void', 
                   [param('ns3::Time', 'start'), param('ns3::Ptr< ns3::RandomVariableStream >', 'rv')])
    ## application-container.h (module 'network'): void ns3::ApplicationContainer::Stop(ns3::Time stop) [member function]
    cls.add_method('Stop', 
                   'void', 
                   [param('ns3::Time', 'stop')])
    return

def register_Ns3AsciiTraceHelper_methods(root_module, cls):
    ## trace-helper.h (module 'network'): ns3::AsciiTraceHelper::AsciiTraceHelper(ns3::AsciiTraceHelper const & arg0) [constructor]
    cls.add_constructor([param('ns3::AsciiTraceHelper const &', 'arg0')])
    ## trace-helper.h (module 'network'): ns3::AsciiTraceHelper::AsciiTraceHelper() [constructor]
    cls.add_constructor([])
    ## trace-helper.h (module 'network'): ns3::Ptr<ns3::OutputStreamWrapper> ns3::AsciiTraceHelper::CreateFileStream(std::string filename, std::ios_base::openmode filemode=std::ios_base::out) [member function]
    cls.add_method('CreateFileStream', 
                   'ns3::Ptr< ns3::OutputStreamWrapper >', 
                   [param('std::string', 'filename'), param('std::ios_base::openmode', 'filemode', default_value='std::ios_base::out')])
    ## trace-helper.h (module 'network'): static void ns3::AsciiTraceHelper::DefaultDequeueSinkWithContext(ns3::Ptr<ns3::OutputStreamWrapper> file, std::string context, ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('DefaultDequeueSinkWithContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('std::string', 'context'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    ## trace-helper.h (module 'network'): static void ns3::AsciiTraceHelper::DefaultDequeueSinkWithoutContext(ns3::Ptr<ns3::OutputStreamWrapper> file, ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('DefaultDequeueSinkWithoutContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    ## trace-helper.h (module 'network'): static void ns3::AsciiTraceHelper::DefaultDropSinkWithContext(ns3::Ptr<ns3::OutputStreamWrapper> file, std::string context, ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('DefaultDropSinkWithContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('std::string', 'context'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    ## trace-helper.h (module 'network'): static void ns3::AsciiTraceHelper::DefaultDropSinkWithoutContext(ns3::Ptr<ns3::OutputStreamWrapper> file, ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('DefaultDropSinkWithoutContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    ## trace-helper.h (module 'network'): static void ns3::AsciiTraceHelper::DefaultEnqueueSinkWithContext(ns3::Ptr<ns3::OutputStreamWrapper> file, std::string context, ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('DefaultEnqueueSinkWithContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('std::string', 'context'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    ## trace-helper.h (module 'network'): static void ns3::AsciiTraceHelper::DefaultEnqueueSinkWithoutContext(ns3::Ptr<ns3::OutputStreamWrapper> file, ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('DefaultEnqueueSinkWithoutContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    ## trace-helper.h (module 'network'): static void ns3::AsciiTraceHelper::DefaultReceiveSinkWithContext(ns3::Ptr<ns3::OutputStreamWrapper> file, std::string context, ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('DefaultReceiveSinkWithContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('std::string', 'context'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    ## trace-helper.h (module 'network'): static void ns3::AsciiTraceHelper::DefaultReceiveSinkWithoutContext(ns3::Ptr<ns3::OutputStreamWrapper> file, ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('DefaultReceiveSinkWithoutContext', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'file'), param('ns3::Ptr< ns3::Packet const >', 'p')], 
                   is_static=True)
    ## trace-helper.h (module 'network'): std::string ns3::AsciiTraceHelper::GetFilenameFromDevice(std::string prefix, ns3::Ptr<ns3::NetDevice> device, bool useObjectNames=true) [member function]
    cls.add_method('GetFilenameFromDevice', 
                   'std::string', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'device'), param('bool', 'useObjectNames', default_value='true')])
    ## trace-helper.h (module 'network'): std::string ns3::AsciiTraceHelper::GetFilenameFromInterfacePair(std::string prefix, ns3::Ptr<ns3::Object> object, uint32_t interface, bool useObjectNames=true) [member function]
    cls.add_method('GetFilenameFromInterfacePair', 
                   'std::string', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::Object >', 'object'), param('uint32_t', 'interface'), param('bool', 'useObjectNames', default_value='true')])
    return

def register_Ns3AsciiTraceHelperForDevice_methods(root_module, cls):
    ## trace-helper.h (module 'network'): ns3::AsciiTraceHelperForDevice::AsciiTraceHelperForDevice(ns3::AsciiTraceHelperForDevice const & arg0) [constructor]
    cls.add_constructor([param('ns3::AsciiTraceHelperForDevice const &', 'arg0')])
    ## trace-helper.h (module 'network'): ns3::AsciiTraceHelperForDevice::AsciiTraceHelperForDevice() [constructor]
    cls.add_constructor([])
    ## trace-helper.h (module 'network'): void ns3::AsciiTraceHelperForDevice::EnableAscii(std::string prefix, ns3::Ptr<ns3::NetDevice> nd, bool explicitFilename=false) [member function]
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'nd'), param('bool', 'explicitFilename', default_value='false')])
    ## trace-helper.h (module 'network'): void ns3::AsciiTraceHelperForDevice::EnableAscii(ns3::Ptr<ns3::OutputStreamWrapper> stream, ns3::Ptr<ns3::NetDevice> nd) [member function]
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('ns3::Ptr< ns3::NetDevice >', 'nd')])
    ## trace-helper.h (module 'network'): void ns3::AsciiTraceHelperForDevice::EnableAscii(std::string prefix, std::string ndName, bool explicitFilename=false) [member function]
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('std::string', 'prefix'), param('std::string', 'ndName'), param('bool', 'explicitFilename', default_value='false')])
    ## trace-helper.h (module 'network'): void ns3::AsciiTraceHelperForDevice::EnableAscii(ns3::Ptr<ns3::OutputStreamWrapper> stream, std::string ndName) [member function]
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('std::string', 'ndName')])
    ## trace-helper.h (module 'network'): void ns3::AsciiTraceHelperForDevice::EnableAscii(std::string prefix, ns3::NetDeviceContainer d) [member function]
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::NetDeviceContainer', 'd')])
    ## trace-helper.h (module 'network'): void ns3::AsciiTraceHelperForDevice::EnableAscii(ns3::Ptr<ns3::OutputStreamWrapper> stream, ns3::NetDeviceContainer d) [member function]
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('ns3::NetDeviceContainer', 'd')])
    ## trace-helper.h (module 'network'): void ns3::AsciiTraceHelperForDevice::EnableAscii(std::string prefix, ns3::NodeContainer n) [member function]
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::NodeContainer', 'n')])
    ## trace-helper.h (module 'network'): void ns3::AsciiTraceHelperForDevice::EnableAscii(ns3::Ptr<ns3::OutputStreamWrapper> stream, ns3::NodeContainer n) [member function]
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('ns3::NodeContainer', 'n')])
    ## trace-helper.h (module 'network'): void ns3::AsciiTraceHelperForDevice::EnableAscii(std::string prefix, uint32_t nodeid, uint32_t deviceid, bool explicitFilename) [member function]
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('std::string', 'prefix'), param('uint32_t', 'nodeid'), param('uint32_t', 'deviceid'), param('bool', 'explicitFilename')])
    ## trace-helper.h (module 'network'): void ns3::AsciiTraceHelperForDevice::EnableAscii(ns3::Ptr<ns3::OutputStreamWrapper> stream, uint32_t nodeid, uint32_t deviceid) [member function]
    cls.add_method('EnableAscii', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('uint32_t', 'nodeid'), param('uint32_t', 'deviceid')])
    ## trace-helper.h (module 'network'): void ns3::AsciiTraceHelperForDevice::EnableAsciiAll(std::string prefix) [member function]
    cls.add_method('EnableAsciiAll', 
                   'void', 
                   [param('std::string', 'prefix')])
    ## trace-helper.h (module 'network'): void ns3::AsciiTraceHelperForDevice::EnableAsciiAll(ns3::Ptr<ns3::OutputStreamWrapper> stream) [member function]
    cls.add_method('EnableAsciiAll', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream')])
    ## trace-helper.h (module 'network'): void ns3::AsciiTraceHelperForDevice::EnableAsciiInternal(ns3::Ptr<ns3::OutputStreamWrapper> stream, std::string prefix, ns3::Ptr<ns3::NetDevice> nd, bool explicitFilename) [member function]
    cls.add_method('EnableAsciiInternal', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'nd'), param('bool', 'explicitFilename')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3AttributeConstructionList_methods(root_module, cls):
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::AttributeConstructionList(ns3::AttributeConstructionList const & arg0) [constructor]
    cls.add_constructor([param('ns3::AttributeConstructionList const &', 'arg0')])
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::AttributeConstructionList() [constructor]
    cls.add_constructor([])
    ## attribute-construction-list.h (module 'core'): void ns3::AttributeConstructionList::Add(std::string name, ns3::Ptr<const ns3::AttributeChecker> checker, ns3::Ptr<ns3::AttributeValue> value) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker'), param('ns3::Ptr< ns3::AttributeValue >', 'value')])
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::CIterator ns3::AttributeConstructionList::Begin() const [member function]
    cls.add_method('Begin', 
                   'ns3::AttributeConstructionList::CIterator', 
                   [], 
                   is_const=True)
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::CIterator ns3::AttributeConstructionList::End() const [member function]
    cls.add_method('End', 
                   'ns3::AttributeConstructionList::CIterator', 
                   [], 
                   is_const=True)
    ## attribute-construction-list.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::AttributeConstructionList::Find(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('Find', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True)
    return

def register_Ns3AttributeConstructionListItem_methods(root_module, cls):
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::Item() [constructor]
    cls.add_constructor([])
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::Item(ns3::AttributeConstructionList::Item const & arg0) [constructor]
    cls.add_constructor([param('ns3::AttributeConstructionList::Item const &', 'arg0')])
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::checker [variable]
    cls.add_instance_attribute('checker', 'ns3::Ptr< ns3::AttributeChecker const >', is_const=False)
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::name [variable]
    cls.add_instance_attribute('name', 'std::string', is_const=False)
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::value [variable]
    cls.add_instance_attribute('value', 'ns3::Ptr< ns3::AttributeValue >', is_const=False)
    return

def register_Ns3BandInfo_methods(root_module, cls):
    ## spectrum-model.h (module 'spectrum'): ns3::BandInfo::BandInfo() [constructor]
    cls.add_constructor([])
    ## spectrum-model.h (module 'spectrum'): ns3::BandInfo::BandInfo(ns3::BandInfo const & arg0) [constructor]
    cls.add_constructor([param('ns3::BandInfo const &', 'arg0')])
    ## spectrum-model.h (module 'spectrum'): ns3::BandInfo::fc [variable]
    cls.add_instance_attribute('fc', 'double', is_const=False)
    ## spectrum-model.h (module 'spectrum'): ns3::BandInfo::fh [variable]
    cls.add_instance_attribute('fh', 'double', is_const=False)
    ## spectrum-model.h (module 'spectrum'): ns3::BandInfo::fl [variable]
    cls.add_instance_attribute('fl', 'double', is_const=False)
    return

def register_Ns3Buffer_methods(root_module, cls):
    ## buffer.h (module 'network'): ns3::Buffer::Buffer(ns3::Buffer const & o) [constructor]
    cls.add_constructor([param('ns3::Buffer const &', 'o')])
    ## buffer.h (module 'network'): ns3::Buffer::Buffer() [constructor]
    cls.add_constructor([])
    ## buffer.h (module 'network'): ns3::Buffer::Buffer(uint32_t dataSize) [constructor]
    cls.add_constructor([param('uint32_t', 'dataSize')])
    ## buffer.h (module 'network'): ns3::Buffer::Buffer(uint32_t dataSize, bool initialize) [constructor]
    cls.add_constructor([param('uint32_t', 'dataSize'), param('bool', 'initialize')])
    ## buffer.h (module 'network'): void ns3::Buffer::AddAtEnd(uint32_t end) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    ## buffer.h (module 'network'): void ns3::Buffer::AddAtEnd(ns3::Buffer const & o) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('ns3::Buffer const &', 'o')])
    ## buffer.h (module 'network'): void ns3::Buffer::AddAtStart(uint32_t start) [member function]
    cls.add_method('AddAtStart', 
                   'void', 
                   [param('uint32_t', 'start')])
    ## buffer.h (module 'network'): ns3::Buffer::Iterator ns3::Buffer::Begin() const [member function]
    cls.add_method('Begin', 
                   'ns3::Buffer::Iterator', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): void ns3::Buffer::CopyData(std::ostream * os, uint32_t size) const [member function]
    cls.add_method('CopyData', 
                   'void', 
                   [param('std::ostream *', 'os'), param('uint32_t', 'size')], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::CopyData(uint8_t * buffer, uint32_t size) const [member function]
    cls.add_method('CopyData', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')], 
                   is_const=True)
    ## buffer.h (module 'network'): ns3::Buffer ns3::Buffer::CreateFragment(uint32_t start, uint32_t length) const [member function]
    cls.add_method('CreateFragment', 
                   'ns3::Buffer', 
                   [param('uint32_t', 'start'), param('uint32_t', 'length')], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Deserialize(uint8_t const * buffer, uint32_t size) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## buffer.h (module 'network'): ns3::Buffer::Iterator ns3::Buffer::End() const [member function]
    cls.add_method('End', 
                   'ns3::Buffer::Iterator', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): uint8_t const * ns3::Buffer::PeekData() const [member function]
    cls.add_method('PeekData', 
                   'uint8_t const *', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): void ns3::Buffer::RemoveAtEnd(uint32_t end) [member function]
    cls.add_method('RemoveAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    ## buffer.h (module 'network'): void ns3::Buffer::RemoveAtStart(uint32_t start) [member function]
    cls.add_method('RemoveAtStart', 
                   'void', 
                   [param('uint32_t', 'start')])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Serialize(uint8_t * buffer, uint32_t maxSize) const [member function]
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    return

def register_Ns3BufferIterator_methods(root_module, cls):
    ## buffer.h (module 'network'): ns3::Buffer::Iterator::Iterator(ns3::Buffer::Iterator const & arg0) [constructor]
    cls.add_constructor([param('ns3::Buffer::Iterator const &', 'arg0')])
    ## buffer.h (module 'network'): ns3::Buffer::Iterator::Iterator() [constructor]
    cls.add_constructor([])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::CalculateIpChecksum(uint16_t size) [member function]
    cls.add_method('CalculateIpChecksum', 
                   'uint16_t', 
                   [param('uint16_t', 'size')])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::CalculateIpChecksum(uint16_t size, uint32_t initialChecksum) [member function]
    cls.add_method('CalculateIpChecksum', 
                   'uint16_t', 
                   [param('uint16_t', 'size'), param('uint32_t', 'initialChecksum')])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::GetDistanceFrom(ns3::Buffer::Iterator const & o) const [member function]
    cls.add_method('GetDistanceFrom', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator const &', 'o')], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::GetRemainingSize() const [member function]
    cls.add_method('GetRemainingSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): bool ns3::Buffer::Iterator::IsEnd() const [member function]
    cls.add_method('IsEnd', 
                   'bool', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): bool ns3::Buffer::Iterator::IsStart() const [member function]
    cls.add_method('IsStart', 
                   'bool', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Next() [member function]
    cls.add_method('Next', 
                   'void', 
                   [])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Next(uint32_t delta) [member function]
    cls.add_method('Next', 
                   'void', 
                   [param('uint32_t', 'delta')])
    ## buffer.h (module 'network'): uint8_t ns3::Buffer::Iterator::PeekU8() [member function]
    cls.add_method('PeekU8', 
                   'uint8_t', 
                   [])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Prev() [member function]
    cls.add_method('Prev', 
                   'void', 
                   [])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Prev(uint32_t delta) [member function]
    cls.add_method('Prev', 
                   'void', 
                   [param('uint32_t', 'delta')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Read(uint8_t * buffer, uint32_t size) [member function]
    cls.add_method('Read', 
                   'void', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Read(ns3::Buffer::Iterator start, uint32_t size) [member function]
    cls.add_method('Read', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint32_t', 'size')])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::ReadLsbtohU16() [member function]
    cls.add_method('ReadLsbtohU16', 
                   'uint16_t', 
                   [])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::ReadLsbtohU32() [member function]
    cls.add_method('ReadLsbtohU32', 
                   'uint32_t', 
                   [])
    ## buffer.h (module 'network'): uint64_t ns3::Buffer::Iterator::ReadLsbtohU64() [member function]
    cls.add_method('ReadLsbtohU64', 
                   'uint64_t', 
                   [])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::ReadNtohU16() [member function]
    cls.add_method('ReadNtohU16', 
                   'uint16_t', 
                   [])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::ReadNtohU32() [member function]
    cls.add_method('ReadNtohU32', 
                   'uint32_t', 
                   [])
    ## buffer.h (module 'network'): uint64_t ns3::Buffer::Iterator::ReadNtohU64() [member function]
    cls.add_method('ReadNtohU64', 
                   'uint64_t', 
                   [])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::ReadU16() [member function]
    cls.add_method('ReadU16', 
                   'uint16_t', 
                   [])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::ReadU32() [member function]
    cls.add_method('ReadU32', 
                   'uint32_t', 
                   [])
    ## buffer.h (module 'network'): uint64_t ns3::Buffer::Iterator::ReadU64() [member function]
    cls.add_method('ReadU64', 
                   'uint64_t', 
                   [])
    ## buffer.h (module 'network'): uint8_t ns3::Buffer::Iterator::ReadU8() [member function]
    cls.add_method('ReadU8', 
                   'uint8_t', 
                   [])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Write(uint8_t const * buffer, uint32_t size) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Write(ns3::Buffer::Iterator start, ns3::Buffer::Iterator end) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start'), param('ns3::Buffer::Iterator', 'end')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtolsbU16(uint16_t data) [member function]
    cls.add_method('WriteHtolsbU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtolsbU32(uint32_t data) [member function]
    cls.add_method('WriteHtolsbU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtolsbU64(uint64_t data) [member function]
    cls.add_method('WriteHtolsbU64', 
                   'void', 
                   [param('uint64_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtonU16(uint16_t data) [member function]
    cls.add_method('WriteHtonU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtonU32(uint32_t data) [member function]
    cls.add_method('WriteHtonU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtonU64(uint64_t data) [member function]
    cls.add_method('WriteHtonU64', 
                   'void', 
                   [param('uint64_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU16(uint16_t data) [member function]
    cls.add_method('WriteU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU32(uint32_t data) [member function]
    cls.add_method('WriteU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU64(uint64_t data) [member function]
    cls.add_method('WriteU64', 
                   'void', 
                   [param('uint64_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU8(uint8_t data) [member function]
    cls.add_method('WriteU8', 
                   'void', 
                   [param('uint8_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU8(uint8_t data, uint32_t len) [member function]
    cls.add_method('WriteU8', 
                   'void', 
                   [param('uint8_t', 'data'), param('uint32_t', 'len')])
    return

def register_Ns3ByteTagIterator_methods(root_module, cls):
    ## packet.h (module 'network'): ns3::ByteTagIterator::ByteTagIterator(ns3::ByteTagIterator const & arg0) [constructor]
    cls.add_constructor([param('ns3::ByteTagIterator const &', 'arg0')])
    ## packet.h (module 'network'): bool ns3::ByteTagIterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::ByteTagIterator::Item ns3::ByteTagIterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::ByteTagIterator::Item', 
                   [])
    return

def register_Ns3ByteTagIteratorItem_methods(root_module, cls):
    ## packet.h (module 'network'): ns3::ByteTagIterator::Item::Item(ns3::ByteTagIterator::Item const & arg0) [constructor]
    cls.add_constructor([param('ns3::ByteTagIterator::Item const &', 'arg0')])
    ## packet.h (module 'network'): uint32_t ns3::ByteTagIterator::Item::GetEnd() const [member function]
    cls.add_method('GetEnd', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::ByteTagIterator::Item::GetStart() const [member function]
    cls.add_method('GetStart', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::ByteTagIterator::Item::GetTag(ns3::Tag & tag) const [member function]
    cls.add_method('GetTag', 
                   'void', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::TypeId ns3::ByteTagIterator::Item::GetTypeId() const [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    return

def register_Ns3ByteTagList_methods(root_module, cls):
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::ByteTagList() [constructor]
    cls.add_constructor([])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::ByteTagList(ns3::ByteTagList const & o) [constructor]
    cls.add_constructor([param('ns3::ByteTagList const &', 'o')])
    ## byte-tag-list.h (module 'network'): ns3::TagBuffer ns3::ByteTagList::Add(ns3::TypeId tid, uint32_t bufferSize, int32_t start, int32_t end) [member function]
    cls.add_method('Add', 
                   'ns3::TagBuffer', 
                   [param('ns3::TypeId', 'tid'), param('uint32_t', 'bufferSize'), param('int32_t', 'start'), param('int32_t', 'end')])
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::Add(ns3::ByteTagList const & o) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::ByteTagList const &', 'o')])
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::AddAtEnd(int32_t appendOffset) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('int32_t', 'appendOffset')])
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::AddAtStart(int32_t prependOffset) [member function]
    cls.add_method('AddAtStart', 
                   'void', 
                   [param('int32_t', 'prependOffset')])
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::Adjust(int32_t adjustment) [member function]
    cls.add_method('Adjust', 
                   'void', 
                   [param('int32_t', 'adjustment')])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator ns3::ByteTagList::Begin(int32_t offsetStart, int32_t offsetEnd) const [member function]
    cls.add_method('Begin', 
                   'ns3::ByteTagList::Iterator', 
                   [param('int32_t', 'offsetStart'), param('int32_t', 'offsetEnd')], 
                   is_const=True)
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::RemoveAll() [member function]
    cls.add_method('RemoveAll', 
                   'void', 
                   [])
    return

def register_Ns3ByteTagListIterator_methods(root_module, cls):
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Iterator(ns3::ByteTagList::Iterator const & arg0) [constructor]
    cls.add_constructor([param('ns3::ByteTagList::Iterator const &', 'arg0')])
    ## byte-tag-list.h (module 'network'): uint32_t ns3::ByteTagList::Iterator::GetOffsetStart() const [member function]
    cls.add_method('GetOffsetStart', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## byte-tag-list.h (module 'network'): bool ns3::ByteTagList::Iterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item ns3::ByteTagList::Iterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::ByteTagList::Iterator::Item', 
                   [])
    return

def register_Ns3ByteTagListIteratorItem_methods(root_module, cls):
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::Item(ns3::ByteTagList::Iterator::Item const & arg0) [constructor]
    cls.add_constructor([param('ns3::ByteTagList::Iterator::Item const &', 'arg0')])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::Item(ns3::TagBuffer buf) [constructor]
    cls.add_constructor([param('ns3::TagBuffer', 'buf')])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::buf [variable]
    cls.add_instance_attribute('buf', 'ns3::TagBuffer', is_const=False)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::end [variable]
    cls.add_instance_attribute('end', 'int32_t', is_const=False)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::size [variable]
    cls.add_instance_attribute('size', 'uint32_t', is_const=False)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::start [variable]
    cls.add_instance_attribute('start', 'int32_t', is_const=False)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::tid [variable]
    cls.add_instance_attribute('tid', 'ns3::TypeId', is_const=False)
    return

def register_Ns3CallbackBase_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackBase::CallbackBase(ns3::CallbackBase const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackBase const &', 'arg0')])
    ## callback.h (module 'core'): ns3::CallbackBase::CallbackBase() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::Ptr<ns3::CallbackImplBase> ns3::CallbackBase::GetImpl() const [member function]
    cls.add_method('GetImpl', 
                   'ns3::Ptr< ns3::CallbackImplBase >', 
                   [], 
                   is_const=True)
    ## callback.h (module 'core'): ns3::CallbackBase::CallbackBase(ns3::Ptr<ns3::CallbackImplBase> impl) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::CallbackImplBase >', 'impl')], 
                        visibility='protected')
    return

def register_Ns3DefaultDeleter__Ns3AttributeAccessor_methods(root_module, cls):
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::AttributeAccessor>::DefaultDeleter() [constructor]
    cls.add_constructor([])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::AttributeAccessor>::DefaultDeleter(ns3::DefaultDeleter<ns3::AttributeAccessor> const & arg0) [constructor]
    cls.add_constructor([param('ns3::DefaultDeleter< ns3::AttributeAccessor > const &', 'arg0')])
    ## default-deleter.h (module 'core'): static void ns3::DefaultDeleter<ns3::AttributeAccessor>::Delete(ns3::AttributeAccessor * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::AttributeAccessor *', 'object')], 
                   is_static=True)
    return

def register_Ns3DefaultDeleter__Ns3AttributeChecker_methods(root_module, cls):
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::AttributeChecker>::DefaultDeleter() [constructor]
    cls.add_constructor([])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::AttributeChecker>::DefaultDeleter(ns3::DefaultDeleter<ns3::AttributeChecker> const & arg0) [constructor]
    cls.add_constructor([param('ns3::DefaultDeleter< ns3::AttributeChecker > const &', 'arg0')])
    ## default-deleter.h (module 'core'): static void ns3::DefaultDeleter<ns3::AttributeChecker>::Delete(ns3::AttributeChecker * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::AttributeChecker *', 'object')], 
                   is_static=True)
    return

def register_Ns3DefaultDeleter__Ns3AttributeValue_methods(root_module, cls):
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::AttributeValue>::DefaultDeleter() [constructor]
    cls.add_constructor([])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::AttributeValue>::DefaultDeleter(ns3::DefaultDeleter<ns3::AttributeValue> const & arg0) [constructor]
    cls.add_constructor([param('ns3::DefaultDeleter< ns3::AttributeValue > const &', 'arg0')])
    ## default-deleter.h (module 'core'): static void ns3::DefaultDeleter<ns3::AttributeValue>::Delete(ns3::AttributeValue * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::AttributeValue *', 'object')], 
                   is_static=True)
    return

def register_Ns3DefaultDeleter__Ns3CallbackImplBase_methods(root_module, cls):
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::CallbackImplBase>::DefaultDeleter() [constructor]
    cls.add_constructor([])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::CallbackImplBase>::DefaultDeleter(ns3::DefaultDeleter<ns3::CallbackImplBase> const & arg0) [constructor]
    cls.add_constructor([param('ns3::DefaultDeleter< ns3::CallbackImplBase > const &', 'arg0')])
    ## default-deleter.h (module 'core'): static void ns3::DefaultDeleter<ns3::CallbackImplBase>::Delete(ns3::CallbackImplBase * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::CallbackImplBase *', 'object')], 
                   is_static=True)
    return

def register_Ns3DefaultDeleter__Ns3EventImpl_methods(root_module, cls):
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::EventImpl>::DefaultDeleter() [constructor]
    cls.add_constructor([])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::EventImpl>::DefaultDeleter(ns3::DefaultDeleter<ns3::EventImpl> const & arg0) [constructor]
    cls.add_constructor([param('ns3::DefaultDeleter< ns3::EventImpl > const &', 'arg0')])
    ## default-deleter.h (module 'core'): static void ns3::DefaultDeleter<ns3::EventImpl>::Delete(ns3::EventImpl * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::EventImpl *', 'object')], 
                   is_static=True)
    return

def register_Ns3DefaultDeleter__Ns3HashImplementation_methods(root_module, cls):
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::Hash::Implementation>::DefaultDeleter() [constructor]
    cls.add_constructor([])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::Hash::Implementation>::DefaultDeleter(ns3::DefaultDeleter<ns3::Hash::Implementation> const & arg0) [constructor]
    cls.add_constructor([param('ns3::DefaultDeleter< ns3::Hash::Implementation > const &', 'arg0')])
    ## default-deleter.h (module 'core'): static void ns3::DefaultDeleter<ns3::Hash::Implementation>::Delete(ns3::Hash::Implementation * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::Hash::Implementation *', 'object')], 
                   is_static=True)
    return

def register_Ns3DefaultDeleter__Ns3NixVector_methods(root_module, cls):
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::NixVector>::DefaultDeleter() [constructor]
    cls.add_constructor([])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::NixVector>::DefaultDeleter(ns3::DefaultDeleter<ns3::NixVector> const & arg0) [constructor]
    cls.add_constructor([param('ns3::DefaultDeleter< ns3::NixVector > const &', 'arg0')])
    ## default-deleter.h (module 'core'): static void ns3::DefaultDeleter<ns3::NixVector>::Delete(ns3::NixVector * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::NixVector *', 'object')], 
                   is_static=True)
    return

def register_Ns3DefaultDeleter__Ns3OutputStreamWrapper_methods(root_module, cls):
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::OutputStreamWrapper>::DefaultDeleter() [constructor]
    cls.add_constructor([])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::OutputStreamWrapper>::DefaultDeleter(ns3::DefaultDeleter<ns3::OutputStreamWrapper> const & arg0) [constructor]
    cls.add_constructor([param('ns3::DefaultDeleter< ns3::OutputStreamWrapper > const &', 'arg0')])
    ## default-deleter.h (module 'core'): static void ns3::DefaultDeleter<ns3::OutputStreamWrapper>::Delete(ns3::OutputStreamWrapper * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::OutputStreamWrapper *', 'object')], 
                   is_static=True)
    return

def register_Ns3DefaultDeleter__Ns3Packet_methods(root_module, cls):
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::Packet>::DefaultDeleter() [constructor]
    cls.add_constructor([])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::Packet>::DefaultDeleter(ns3::DefaultDeleter<ns3::Packet> const & arg0) [constructor]
    cls.add_constructor([param('ns3::DefaultDeleter< ns3::Packet > const &', 'arg0')])
    ## default-deleter.h (module 'core'): static void ns3::DefaultDeleter<ns3::Packet>::Delete(ns3::Packet * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::Packet *', 'object')], 
                   is_static=True)
    return

def register_Ns3DefaultDeleter__Ns3SpectrumModel_methods(root_module, cls):
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::SpectrumModel>::DefaultDeleter() [constructor]
    cls.add_constructor([])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::SpectrumModel>::DefaultDeleter(ns3::DefaultDeleter<ns3::SpectrumModel> const & arg0) [constructor]
    cls.add_constructor([param('ns3::DefaultDeleter< ns3::SpectrumModel > const &', 'arg0')])
    ## default-deleter.h (module 'core'): static void ns3::DefaultDeleter<ns3::SpectrumModel>::Delete(ns3::SpectrumModel * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::SpectrumModel *', 'object')], 
                   is_static=True)
    return

def register_Ns3DefaultDeleter__Ns3SpectrumSignalParameters_methods(root_module, cls):
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::SpectrumSignalParameters>::DefaultDeleter() [constructor]
    cls.add_constructor([])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::SpectrumSignalParameters>::DefaultDeleter(ns3::DefaultDeleter<ns3::SpectrumSignalParameters> const & arg0) [constructor]
    cls.add_constructor([param('ns3::DefaultDeleter< ns3::SpectrumSignalParameters > const &', 'arg0')])
    ## default-deleter.h (module 'core'): static void ns3::DefaultDeleter<ns3::SpectrumSignalParameters>::Delete(ns3::SpectrumSignalParameters * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::SpectrumSignalParameters *', 'object')], 
                   is_static=True)
    return

def register_Ns3DefaultDeleter__Ns3SpectrumValue_methods(root_module, cls):
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::SpectrumValue>::DefaultDeleter() [constructor]
    cls.add_constructor([])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::SpectrumValue>::DefaultDeleter(ns3::DefaultDeleter<ns3::SpectrumValue> const & arg0) [constructor]
    cls.add_constructor([param('ns3::DefaultDeleter< ns3::SpectrumValue > const &', 'arg0')])
    ## default-deleter.h (module 'core'): static void ns3::DefaultDeleter<ns3::SpectrumValue>::Delete(ns3::SpectrumValue * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::SpectrumValue *', 'object')], 
                   is_static=True)
    return

def register_Ns3DefaultDeleter__Ns3TraceSourceAccessor_methods(root_module, cls):
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::TraceSourceAccessor>::DefaultDeleter() [constructor]
    cls.add_constructor([])
    ## default-deleter.h (module 'core'): ns3::DefaultDeleter<ns3::TraceSourceAccessor>::DefaultDeleter(ns3::DefaultDeleter<ns3::TraceSourceAccessor> const & arg0) [constructor]
    cls.add_constructor([param('ns3::DefaultDeleter< ns3::TraceSourceAccessor > const &', 'arg0')])
    ## default-deleter.h (module 'core'): static void ns3::DefaultDeleter<ns3::TraceSourceAccessor>::Delete(ns3::TraceSourceAccessor * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::TraceSourceAccessor *', 'object')], 
                   is_static=True)
    return

def register_Ns3DeviceEnergyModelContainer_methods(root_module, cls):
    ## device-energy-model-container.h (module 'energy'): ns3::DeviceEnergyModelContainer::DeviceEnergyModelContainer(ns3::DeviceEnergyModelContainer const & arg0) [constructor]
    cls.add_constructor([param('ns3::DeviceEnergyModelContainer const &', 'arg0')])
    ## device-energy-model-container.h (module 'energy'): ns3::DeviceEnergyModelContainer::DeviceEnergyModelContainer() [constructor]
    cls.add_constructor([])
    ## device-energy-model-container.h (module 'energy'): ns3::DeviceEnergyModelContainer::DeviceEnergyModelContainer(ns3::Ptr<ns3::DeviceEnergyModel> model) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::DeviceEnergyModel >', 'model')])
    ## device-energy-model-container.h (module 'energy'): ns3::DeviceEnergyModelContainer::DeviceEnergyModelContainer(std::string modelName) [constructor]
    cls.add_constructor([param('std::string', 'modelName')])
    ## device-energy-model-container.h (module 'energy'): ns3::DeviceEnergyModelContainer::DeviceEnergyModelContainer(ns3::DeviceEnergyModelContainer const & a, ns3::DeviceEnergyModelContainer const & b) [constructor]
    cls.add_constructor([param('ns3::DeviceEnergyModelContainer const &', 'a'), param('ns3::DeviceEnergyModelContainer const &', 'b')])
    ## device-energy-model-container.h (module 'energy'): void ns3::DeviceEnergyModelContainer::Add(ns3::DeviceEnergyModelContainer container) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::DeviceEnergyModelContainer', 'container')])
    ## device-energy-model-container.h (module 'energy'): void ns3::DeviceEnergyModelContainer::Add(ns3::Ptr<ns3::DeviceEnergyModel> model) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Ptr< ns3::DeviceEnergyModel >', 'model')])
    ## device-energy-model-container.h (module 'energy'): void ns3::DeviceEnergyModelContainer::Add(std::string modelName) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'modelName')])
    ## device-energy-model-container.h (module 'energy'): ns3::DeviceEnergyModelContainer::Iterator ns3::DeviceEnergyModelContainer::Begin() const [member function]
    cls.add_method('Begin', 
                   'ns3::DeviceEnergyModelContainer::Iterator', 
                   [], 
                   is_const=True)
    ## device-energy-model-container.h (module 'energy'): void ns3::DeviceEnergyModelContainer::Clear() [member function]
    cls.add_method('Clear', 
                   'void', 
                   [])
    ## device-energy-model-container.h (module 'energy'): ns3::DeviceEnergyModelContainer::Iterator ns3::DeviceEnergyModelContainer::End() const [member function]
    cls.add_method('End', 
                   'ns3::DeviceEnergyModelContainer::Iterator', 
                   [], 
                   is_const=True)
    ## device-energy-model-container.h (module 'energy'): ns3::Ptr<ns3::DeviceEnergyModel> ns3::DeviceEnergyModelContainer::Get(uint32_t i) const [member function]
    cls.add_method('Get', 
                   'ns3::Ptr< ns3::DeviceEnergyModel >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## device-energy-model-container.h (module 'energy'): uint32_t ns3::DeviceEnergyModelContainer::GetN() const [member function]
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    return

def register_Ns3DeviceEnergyModelHelper_methods(root_module, cls):
    ## energy-model-helper.h (module 'energy'): ns3::DeviceEnergyModelHelper::DeviceEnergyModelHelper() [constructor]
    cls.add_constructor([])
    ## energy-model-helper.h (module 'energy'): ns3::DeviceEnergyModelHelper::DeviceEnergyModelHelper(ns3::DeviceEnergyModelHelper const & arg0) [constructor]
    cls.add_constructor([param('ns3::DeviceEnergyModelHelper const &', 'arg0')])
    ## energy-model-helper.h (module 'energy'): ns3::DeviceEnergyModelContainer ns3::DeviceEnergyModelHelper::Install(ns3::Ptr<ns3::NetDevice> device, ns3::Ptr<ns3::EnergySource> source) const [member function]
    cls.add_method('Install', 
                   'ns3::DeviceEnergyModelContainer', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device'), param('ns3::Ptr< ns3::EnergySource >', 'source')], 
                   is_const=True)
    ## energy-model-helper.h (module 'energy'): ns3::DeviceEnergyModelContainer ns3::DeviceEnergyModelHelper::Install(ns3::NetDeviceContainer deviceContainer, ns3::EnergySourceContainer sourceContainer) const [member function]
    cls.add_method('Install', 
                   'ns3::DeviceEnergyModelContainer', 
                   [param('ns3::NetDeviceContainer', 'deviceContainer'), param('ns3::EnergySourceContainer', 'sourceContainer')], 
                   is_const=True)
    ## energy-model-helper.h (module 'energy'): void ns3::DeviceEnergyModelHelper::Set(std::string name, ns3::AttributeValue const & v) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'v')], 
                   is_pure_virtual=True, is_virtual=True)
    ## energy-model-helper.h (module 'energy'): ns3::Ptr<ns3::DeviceEnergyModel> ns3::DeviceEnergyModelHelper::DoInstall(ns3::Ptr<ns3::NetDevice> device, ns3::Ptr<ns3::EnergySource> source) const [member function]
    cls.add_method('DoInstall', 
                   'ns3::Ptr< ns3::DeviceEnergyModel >', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device'), param('ns3::Ptr< ns3::EnergySource >', 'source')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3DeviceRxSettings_methods(root_module, cls):
    ## lora-network.h (module 'lora'): ns3::DeviceRxSettings::DeviceRxSettings() [constructor]
    cls.add_constructor([])
    ## lora-network.h (module 'lora'): ns3::DeviceRxSettings::DeviceRxSettings(ns3::DeviceRxSettings const & arg0) [constructor]
    cls.add_constructor([param('ns3::DeviceRxSettings const &', 'arg0')])
    ## lora-network.h (module 'lora'): ns3::DeviceRxSettings::delay [variable]
    cls.add_instance_attribute('delay', 'uint8_t', is_const=False)
    ## lora-network.h (module 'lora'): ns3::DeviceRxSettings::dr1Offset [variable]
    cls.add_instance_attribute('dr1Offset', 'uint8_t', is_const=False)
    ## lora-network.h (module 'lora'): ns3::DeviceRxSettings::dr2 [variable]
    cls.add_instance_attribute('dr2', 'uint8_t', is_const=False)
    ## lora-network.h (module 'lora'): ns3::DeviceRxSettings::frequency [variable]
    cls.add_instance_attribute('frequency', 'uint32_t', is_const=False)
    return

def register_Ns3EnergySourceHelper_methods(root_module, cls):
    ## energy-model-helper.h (module 'energy'): ns3::EnergySourceHelper::EnergySourceHelper() [constructor]
    cls.add_constructor([])
    ## energy-model-helper.h (module 'energy'): ns3::EnergySourceHelper::EnergySourceHelper(ns3::EnergySourceHelper const & arg0) [constructor]
    cls.add_constructor([param('ns3::EnergySourceHelper const &', 'arg0')])
    ## energy-model-helper.h (module 'energy'): ns3::EnergySourceContainer ns3::EnergySourceHelper::Install(ns3::Ptr<ns3::Node> node) const [member function]
    cls.add_method('Install', 
                   'ns3::EnergySourceContainer', 
                   [param('ns3::Ptr< ns3::Node >', 'node')], 
                   is_const=True)
    ## energy-model-helper.h (module 'energy'): ns3::EnergySourceContainer ns3::EnergySourceHelper::Install(ns3::NodeContainer c) const [member function]
    cls.add_method('Install', 
                   'ns3::EnergySourceContainer', 
                   [param('ns3::NodeContainer', 'c')], 
                   is_const=True)
    ## energy-model-helper.h (module 'energy'): ns3::EnergySourceContainer ns3::EnergySourceHelper::Install(std::string nodeName) const [member function]
    cls.add_method('Install', 
                   'ns3::EnergySourceContainer', 
                   [param('std::string', 'nodeName')], 
                   is_const=True)
    ## energy-model-helper.h (module 'energy'): ns3::EnergySourceContainer ns3::EnergySourceHelper::InstallAll() const [member function]
    cls.add_method('InstallAll', 
                   'ns3::EnergySourceContainer', 
                   [], 
                   is_const=True)
    ## energy-model-helper.h (module 'energy'): void ns3::EnergySourceHelper::Set(std::string name, ns3::AttributeValue const & v) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'v')], 
                   is_pure_virtual=True, is_virtual=True)
    ## energy-model-helper.h (module 'energy'): ns3::Ptr<ns3::EnergySource> ns3::EnergySourceHelper::DoInstall(ns3::Ptr<ns3::Node> node) const [member function]
    cls.add_method('DoInstall', 
                   'ns3::Ptr< ns3::EnergySource >', 
                   [param('ns3::Ptr< ns3::Node >', 'node')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3EventId_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    ## event-id.h (module 'core'): ns3::EventId::EventId(ns3::EventId const & arg0) [constructor]
    cls.add_constructor([param('ns3::EventId const &', 'arg0')])
    ## event-id.h (module 'core'): ns3::EventId::EventId() [constructor]
    cls.add_constructor([])
    ## event-id.h (module 'core'): ns3::EventId::EventId(ns3::Ptr<ns3::EventImpl> const & impl, uint64_t ts, uint32_t context, uint32_t uid) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::EventImpl > const &', 'impl'), param('uint64_t', 'ts'), param('uint32_t', 'context'), param('uint32_t', 'uid')])
    ## event-id.h (module 'core'): void ns3::EventId::Cancel() [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [])
    ## event-id.h (module 'core'): uint32_t ns3::EventId::GetContext() const [member function]
    cls.add_method('GetContext', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): uint64_t ns3::EventId::GetTs() const [member function]
    cls.add_method('GetTs', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): uint32_t ns3::EventId::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): bool ns3::EventId::IsExpired() const [member function]
    cls.add_method('IsExpired', 
                   'bool', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): bool ns3::EventId::IsRunning() const [member function]
    cls.add_method('IsRunning', 
                   'bool', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): ns3::EventImpl * ns3::EventId::PeekEventImpl() const [member function]
    cls.add_method('PeekEventImpl', 
                   'ns3::EventImpl *', 
                   [], 
                   is_const=True)
    return

def register_Ns3Hasher_methods(root_module, cls):
    ## hash.h (module 'core'): ns3::Hasher::Hasher(ns3::Hasher const & arg0) [constructor]
    cls.add_constructor([param('ns3::Hasher const &', 'arg0')])
    ## hash.h (module 'core'): ns3::Hasher::Hasher() [constructor]
    cls.add_constructor([])
    ## hash.h (module 'core'): ns3::Hasher::Hasher(ns3::Ptr<ns3::Hash::Implementation> hp) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::Hash::Implementation >', 'hp')])
    ## hash.h (module 'core'): uint32_t ns3::Hasher::GetHash32(char const * buffer, std::size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('std::size_t const', 'size')])
    ## hash.h (module 'core'): uint32_t ns3::Hasher::GetHash32(std::string const s) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('std::string const', 's')])
    ## hash.h (module 'core'): uint64_t ns3::Hasher::GetHash64(char const * buffer, std::size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('std::size_t const', 'size')])
    ## hash.h (module 'core'): uint64_t ns3::Hasher::GetHash64(std::string const s) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('std::string const', 's')])
    ## hash.h (module 'core'): ns3::Hasher & ns3::Hasher::clear() [member function]
    cls.add_method('clear', 
                   'ns3::Hasher &', 
                   [])
    return

def register_Ns3Ipv4Address_methods(root_module, cls):
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address::Ipv4Address(ns3::Ipv4Address const & arg0) [constructor]
    cls.add_constructor([param('ns3::Ipv4Address const &', 'arg0')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address::Ipv4Address() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address::Ipv4Address(uint32_t address) [constructor]
    cls.add_constructor([param('uint32_t', 'address')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address::Ipv4Address(char const * address) [constructor]
    cls.add_constructor([param('char const *', 'address')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address ns3::Ipv4Address::CombineMask(ns3::Ipv4Mask const & mask) const [member function]
    cls.add_method('CombineMask', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Ipv4Mask const &', 'mask')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::ConvertFrom(ns3::Address const & address) [member function]
    cls.add_method('ConvertFrom', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::Deserialize(uint8_t const * buf) [member function]
    cls.add_method('Deserialize', 
                   'ns3::Ipv4Address', 
                   [param('uint8_t const *', 'buf')], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): uint32_t ns3::Ipv4Address::Get() const [member function]
    cls.add_method('Get', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::GetAny() [member function]
    cls.add_method('GetAny', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::GetBroadcast() [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::GetLoopback() [member function]
    cls.add_method('GetLoopback', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address ns3::Ipv4Address::GetSubnetDirectedBroadcast(ns3::Ipv4Mask const & mask) const [member function]
    cls.add_method('GetSubnetDirectedBroadcast', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Ipv4Mask const &', 'mask')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::GetZero() [member function]
    cls.add_method('GetZero', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsAny() const [member function]
    cls.add_method('IsAny', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsEqual(ns3::Ipv4Address const & other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv4Address const &', 'other')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsLocalMulticast() const [member function]
    cls.add_method('IsLocalMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsLocalhost() const [member function]
    cls.add_method('IsLocalhost', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static bool ns3::Ipv4Address::IsMatchingType(ns3::Address const & address) [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsMulticast() const [member function]
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsSubnetDirectedBroadcast(ns3::Ipv4Mask const & mask) const [member function]
    cls.add_method('IsSubnetDirectedBroadcast', 
                   'bool', 
                   [param('ns3::Ipv4Mask const &', 'mask')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Address::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Address::Serialize(uint8_t * buf) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Address::Set(uint32_t address) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('uint32_t', 'address')])
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Address::Set(char const * address) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('char const *', 'address')])
    return

def register_Ns3Ipv4Mask_methods(root_module, cls):
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask::Ipv4Mask(ns3::Ipv4Mask const & arg0) [constructor]
    cls.add_constructor([param('ns3::Ipv4Mask const &', 'arg0')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask::Ipv4Mask() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask::Ipv4Mask(uint32_t mask) [constructor]
    cls.add_constructor([param('uint32_t', 'mask')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask::Ipv4Mask(char const * mask) [constructor]
    cls.add_constructor([param('char const *', 'mask')])
    ## ipv4-address.h (module 'network'): uint32_t ns3::Ipv4Mask::Get() const [member function]
    cls.add_method('Get', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): uint32_t ns3::Ipv4Mask::GetInverse() const [member function]
    cls.add_method('GetInverse', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Mask ns3::Ipv4Mask::GetLoopback() [member function]
    cls.add_method('GetLoopback', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Mask ns3::Ipv4Mask::GetOnes() [member function]
    cls.add_method('GetOnes', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): uint16_t ns3::Ipv4Mask::GetPrefixLength() const [member function]
    cls.add_method('GetPrefixLength', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Mask ns3::Ipv4Mask::GetZero() [member function]
    cls.add_method('GetZero', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Mask::IsEqual(ns3::Ipv4Mask other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv4Mask', 'other')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Mask::IsMatch(ns3::Ipv4Address a, ns3::Ipv4Address b) const [member function]
    cls.add_method('IsMatch', 
                   'bool', 
                   [param('ns3::Ipv4Address', 'a'), param('ns3::Ipv4Address', 'b')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Mask::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Mask::Set(uint32_t mask) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('uint32_t', 'mask')])
    return

def register_Ns3Ipv6Address_methods(root_module, cls):
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address(char const * address) [constructor]
    cls.add_constructor([param('char const *', 'address')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address(uint8_t * address) [constructor]
    cls.add_constructor([param('uint8_t *', 'address')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address(ns3::Ipv6Address const & addr) [constructor]
    cls.add_constructor([param('ns3::Ipv6Address const &', 'addr')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address(ns3::Ipv6Address const * addr) [constructor]
    cls.add_constructor([param('ns3::Ipv6Address const *', 'addr')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address ns3::Ipv6Address::CombinePrefix(ns3::Ipv6Prefix const & prefix) [member function]
    cls.add_method('CombinePrefix', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Ipv6Prefix const &', 'prefix')])
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::ConvertFrom(ns3::Address const & address) [member function]
    cls.add_method('ConvertFrom', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::Deserialize(uint8_t const * buf) [member function]
    cls.add_method('Deserialize', 
                   'ns3::Ipv6Address', 
                   [param('uint8_t const *', 'buf')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetAllHostsMulticast() [member function]
    cls.add_method('GetAllHostsMulticast', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetAllNodesMulticast() [member function]
    cls.add_method('GetAllNodesMulticast', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetAllRoutersMulticast() [member function]
    cls.add_method('GetAllRoutersMulticast', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetAny() [member function]
    cls.add_method('GetAny', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::GetBytes(uint8_t * buf) const [member function]
    cls.add_method('GetBytes', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): ns3::Ipv4Address ns3::Ipv6Address::GetIpv4MappedAddress() const [member function]
    cls.add_method('GetIpv4MappedAddress', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetLoopback() [member function]
    cls.add_method('GetLoopback', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetOnes() [member function]
    cls.add_method('GetOnes', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetZero() [member function]
    cls.add_method('GetZero', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsAllHostsMulticast() const [member function]
    cls.add_method('IsAllHostsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsAllNodesMulticast() const [member function]
    cls.add_method('IsAllNodesMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsAllRoutersMulticast() const [member function]
    cls.add_method('IsAllRoutersMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsAny() const [member function]
    cls.add_method('IsAny', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsDocumentation() const [member function]
    cls.add_method('IsDocumentation', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsEqual(ns3::Ipv6Address const & other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv6Address const &', 'other')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsIpv4MappedAddress() const [member function]
    cls.add_method('IsIpv4MappedAddress', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsLinkLocal() const [member function]
    cls.add_method('IsLinkLocal', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsLinkLocalMulticast() const [member function]
    cls.add_method('IsLinkLocalMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsLocalhost() const [member function]
    cls.add_method('IsLocalhost', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static bool ns3::Ipv6Address::IsMatchingType(ns3::Address const & address) [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsMulticast() const [member function]
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsSolicitedMulticast() const [member function]
    cls.add_method('IsSolicitedMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredAddress(ns3::Mac16Address addr, ns3::Ipv6Address prefix) [member function]
    cls.add_method('MakeAutoconfiguredAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac16Address', 'addr'), param('ns3::Ipv6Address', 'prefix')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredAddress(ns3::Mac48Address addr, ns3::Ipv6Address prefix) [member function]
    cls.add_method('MakeAutoconfiguredAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac48Address', 'addr'), param('ns3::Ipv6Address', 'prefix')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredAddress(ns3::Mac64Address addr, ns3::Ipv6Address prefix) [member function]
    cls.add_method('MakeAutoconfiguredAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac64Address', 'addr'), param('ns3::Ipv6Address', 'prefix')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredAddress(ns3::Mac8Address addr, ns3::Ipv6Address prefix) [member function]
    cls.add_method('MakeAutoconfiguredAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac8Address', 'addr'), param('ns3::Ipv6Address', 'prefix')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredLinkLocalAddress(ns3::Mac16Address mac) [member function]
    cls.add_method('MakeAutoconfiguredLinkLocalAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac16Address', 'mac')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredLinkLocalAddress(ns3::Mac48Address mac) [member function]
    cls.add_method('MakeAutoconfiguredLinkLocalAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac48Address', 'mac')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredLinkLocalAddress(ns3::Mac64Address mac) [member function]
    cls.add_method('MakeAutoconfiguredLinkLocalAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac64Address', 'mac')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredLinkLocalAddress(ns3::Mac8Address mac) [member function]
    cls.add_method('MakeAutoconfiguredLinkLocalAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac8Address', 'mac')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeIpv4MappedAddress(ns3::Ipv4Address addr) [member function]
    cls.add_method('MakeIpv4MappedAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Ipv4Address', 'addr')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeSolicitedAddress(ns3::Ipv6Address addr) [member function]
    cls.add_method('MakeSolicitedAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Ipv6Address', 'addr')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::Serialize(uint8_t * buf) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::Set(char const * address) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('char const *', 'address')])
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::Set(uint8_t * address) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('uint8_t *', 'address')])
    return

def register_Ns3Ipv6Prefix_methods(root_module, cls):
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(uint8_t * prefix) [constructor]
    cls.add_constructor([param('uint8_t *', 'prefix')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(char const * prefix) [constructor]
    cls.add_constructor([param('char const *', 'prefix')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(uint8_t prefix) [constructor]
    cls.add_constructor([param('uint8_t', 'prefix')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(ns3::Ipv6Prefix const & prefix) [constructor]
    cls.add_constructor([param('ns3::Ipv6Prefix const &', 'prefix')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(ns3::Ipv6Prefix const * prefix) [constructor]
    cls.add_constructor([param('ns3::Ipv6Prefix const *', 'prefix')])
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Prefix::GetBytes(uint8_t * buf) const [member function]
    cls.add_method('GetBytes', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Prefix ns3::Ipv6Prefix::GetLoopback() [member function]
    cls.add_method('GetLoopback', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Prefix ns3::Ipv6Prefix::GetOnes() [member function]
    cls.add_method('GetOnes', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): uint8_t ns3::Ipv6Prefix::GetPrefixLength() const [member function]
    cls.add_method('GetPrefixLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Prefix ns3::Ipv6Prefix::GetZero() [member function]
    cls.add_method('GetZero', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Prefix::IsEqual(ns3::Ipv6Prefix const & other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv6Prefix const &', 'other')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Prefix::IsMatch(ns3::Ipv6Address a, ns3::Ipv6Address b) const [member function]
    cls.add_method('IsMatch', 
                   'bool', 
                   [param('ns3::Ipv6Address', 'a'), param('ns3::Ipv6Address', 'b')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Prefix::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    return

def register_Ns3LoRaEnergySourceHelper_methods(root_module, cls):
    ## lora-energy-source-helper.h (module 'lora'): ns3::LoRaEnergySourceHelper::LoRaEnergySourceHelper(ns3::LoRaEnergySourceHelper const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaEnergySourceHelper const &', 'arg0')])
    ## lora-energy-source-helper.h (module 'lora'): ns3::LoRaEnergySourceHelper::LoRaEnergySourceHelper() [constructor]
    cls.add_constructor([])
    ## lora-energy-source-helper.h (module 'lora'): void ns3::LoRaEnergySourceHelper::Set(std::string name, ns3::AttributeValue const & v) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'v')], 
                   is_virtual=True)
    ## lora-energy-source-helper.h (module 'lora'): ns3::Ptr<ns3::EnergySource> ns3::LoRaEnergySourceHelper::DoInstall(ns3::Ptr<ns3::Node> node) const [member function]
    cls.add_method('DoInstall', 
                   'ns3::Ptr< ns3::EnergySource >', 
                   [param('ns3::Ptr< ns3::Node >', 'node')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3LoRaRadioEnergyModelHelper_methods(root_module, cls):
    ## lora-radio-energy-model-helper.h (module 'lora'): ns3::LoRaRadioEnergyModelHelper::LoRaRadioEnergyModelHelper(ns3::LoRaRadioEnergyModelHelper const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaRadioEnergyModelHelper const &', 'arg0')])
    ## lora-radio-energy-model-helper.h (module 'lora'): ns3::LoRaRadioEnergyModelHelper::LoRaRadioEnergyModelHelper() [constructor]
    cls.add_constructor([])
    ## lora-radio-energy-model-helper.h (module 'lora'): void ns3::LoRaRadioEnergyModelHelper::Set(std::string name, ns3::AttributeValue const & v) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'v')], 
                   is_virtual=True)
    ## lora-radio-energy-model-helper.h (module 'lora'): ns3::Ptr<ns3::DeviceEnergyModel> ns3::LoRaRadioEnergyModelHelper::DoInstall(ns3::Ptr<ns3::NetDevice> device, ns3::Ptr<ns3::EnergySource> source) const [member function]
    cls.add_method('DoInstall', 
                   'ns3::Ptr< ns3::DeviceEnergyModel >', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device'), param('ns3::Ptr< ns3::EnergySource >', 'source')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3Mac32Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    ## mac32-address.h (module 'lora'): ns3::Mac32Address::Mac32Address(ns3::Mac32Address const & arg0) [constructor]
    cls.add_constructor([param('ns3::Mac32Address const &', 'arg0')])
    ## mac32-address.h (module 'lora'): ns3::Mac32Address::Mac32Address() [constructor]
    cls.add_constructor([])
    ## mac32-address.h (module 'lora'): ns3::Mac32Address::Mac32Address(char const * str) [constructor]
    cls.add_constructor([param('char const *', 'str')])
    ## mac32-address.h (module 'lora'): static ns3::Mac32Address ns3::Mac32Address::Allocate() [member function]
    cls.add_method('Allocate', 
                   'ns3::Mac32Address', 
                   [], 
                   is_static=True)
    ## mac32-address.h (module 'lora'): static ns3::Mac32Address ns3::Mac32Address::ConvertFrom(ns3::Address const & address) [member function]
    cls.add_method('ConvertFrom', 
                   'ns3::Mac32Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## mac32-address.h (module 'lora'): void ns3::Mac32Address::CopyFrom(uint8_t const * buffer) [member function]
    cls.add_method('CopyFrom', 
                   'void', 
                   [param('uint8_t const *', 'buffer')])
    ## mac32-address.h (module 'lora'): void ns3::Mac32Address::CopyTo(uint8_t * buffer) const [member function]
    cls.add_method('CopyTo', 
                   'void', 
                   [param('uint8_t *', 'buffer')], 
                   is_const=True)
    ## mac32-address.h (module 'lora'): static ns3::Mac32Address ns3::Mac32Address::GetBroadcast() [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Mac32Address', 
                   [], 
                   is_static=True)
    ## mac32-address.h (module 'lora'): static ns3::Mac32Address ns3::Mac32Address::GetMulticast(ns3::Ipv4Address address) [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Mac32Address', 
                   [param('ns3::Ipv4Address', 'address')], 
                   is_static=True)
    ## mac32-address.h (module 'lora'): static ns3::Mac32Address ns3::Mac32Address::GetMulticast(ns3::Ipv6Address address) [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Mac32Address', 
                   [param('ns3::Ipv6Address', 'address')], 
                   is_static=True)
    ## mac32-address.h (module 'lora'): static ns3::Mac32Address ns3::Mac32Address::GetMulticast6Prefix() [member function]
    cls.add_method('GetMulticast6Prefix', 
                   'ns3::Mac32Address', 
                   [], 
                   is_static=True)
    ## mac32-address.h (module 'lora'): static ns3::Mac32Address ns3::Mac32Address::GetMulticastPrefix() [member function]
    cls.add_method('GetMulticastPrefix', 
                   'ns3::Mac32Address', 
                   [], 
                   is_static=True)
    ## mac32-address.h (module 'lora'): uint32_t ns3::Mac32Address::GetUInt() [member function]
    cls.add_method('GetUInt', 
                   'uint32_t', 
                   [])
    ## mac32-address.h (module 'lora'): bool ns3::Mac32Address::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac32-address.h (module 'lora'): bool ns3::Mac32Address::IsGroup() const [member function]
    cls.add_method('IsGroup', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac32-address.h (module 'lora'): static bool ns3::Mac32Address::IsMatchingType(ns3::Address const & address) [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    return

def register_Ns3Mac48Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    ## mac48-address.h (module 'network'): ns3::Mac48Address::Mac48Address(ns3::Mac48Address const & arg0) [constructor]
    cls.add_constructor([param('ns3::Mac48Address const &', 'arg0')])
    ## mac48-address.h (module 'network'): ns3::Mac48Address::Mac48Address() [constructor]
    cls.add_constructor([])
    ## mac48-address.h (module 'network'): ns3::Mac48Address::Mac48Address(char const * str) [constructor]
    cls.add_constructor([param('char const *', 'str')])
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::Allocate() [member function]
    cls.add_method('Allocate', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::ConvertFrom(ns3::Address const & address) [member function]
    cls.add_method('ConvertFrom', 
                   'ns3::Mac48Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## mac48-address.h (module 'network'): void ns3::Mac48Address::CopyFrom(uint8_t const * buffer) [member function]
    cls.add_method('CopyFrom', 
                   'void', 
                   [param('uint8_t const *', 'buffer')])
    ## mac48-address.h (module 'network'): void ns3::Mac48Address::CopyTo(uint8_t * buffer) const [member function]
    cls.add_method('CopyTo', 
                   'void', 
                   [param('uint8_t *', 'buffer')], 
                   is_const=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetBroadcast() [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetMulticast(ns3::Ipv4Address address) [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Mac48Address', 
                   [param('ns3::Ipv4Address', 'address')], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetMulticast(ns3::Ipv6Address address) [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Mac48Address', 
                   [param('ns3::Ipv6Address', 'address')], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetMulticast6Prefix() [member function]
    cls.add_method('GetMulticast6Prefix', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetMulticastPrefix() [member function]
    cls.add_method('GetMulticastPrefix', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    ## mac48-address.h (module 'network'): bool ns3::Mac48Address::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac48-address.h (module 'network'): bool ns3::Mac48Address::IsGroup() const [member function]
    cls.add_method('IsGroup', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac48-address.h (module 'network'): static bool ns3::Mac48Address::IsMatchingType(ns3::Address const & address) [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    return

def register_Ns3Mac8Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_output_stream_operator()
    ## mac8-address.h (module 'network'): ns3::Mac8Address::Mac8Address(ns3::Mac8Address const & arg0) [constructor]
    cls.add_constructor([param('ns3::Mac8Address const &', 'arg0')])
    ## mac8-address.h (module 'network'): ns3::Mac8Address::Mac8Address() [constructor]
    cls.add_constructor([])
    ## mac8-address.h (module 'network'): ns3::Mac8Address::Mac8Address(uint8_t addr) [constructor]
    cls.add_constructor([param('uint8_t', 'addr')])
    ## mac8-address.h (module 'network'): static ns3::Mac8Address ns3::Mac8Address::Allocate() [member function]
    cls.add_method('Allocate', 
                   'ns3::Mac8Address', 
                   [], 
                   is_static=True)
    ## mac8-address.h (module 'network'): static ns3::Mac8Address ns3::Mac8Address::ConvertFrom(ns3::Address const & address) [member function]
    cls.add_method('ConvertFrom', 
                   'ns3::Mac8Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## mac8-address.h (module 'network'): void ns3::Mac8Address::CopyFrom(uint8_t const * pBuffer) [member function]
    cls.add_method('CopyFrom', 
                   'void', 
                   [param('uint8_t const *', 'pBuffer')])
    ## mac8-address.h (module 'network'): void ns3::Mac8Address::CopyTo(uint8_t * pBuffer) const [member function]
    cls.add_method('CopyTo', 
                   'void', 
                   [param('uint8_t *', 'pBuffer')], 
                   is_const=True)
    ## mac8-address.h (module 'network'): static ns3::Mac8Address ns3::Mac8Address::GetBroadcast() [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Mac8Address', 
                   [], 
                   is_static=True)
    ## mac8-address.h (module 'network'): static bool ns3::Mac8Address::IsMatchingType(ns3::Address const & address) [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    return

def register_Ns3NetDeviceContainer_methods(root_module, cls):
    ## net-device-container.h (module 'network'): ns3::NetDeviceContainer::NetDeviceContainer(ns3::NetDeviceContainer const & arg0) [constructor]
    cls.add_constructor([param('ns3::NetDeviceContainer const &', 'arg0')])
    ## net-device-container.h (module 'network'): ns3::NetDeviceContainer::NetDeviceContainer() [constructor]
    cls.add_constructor([])
    ## net-device-container.h (module 'network'): ns3::NetDeviceContainer::NetDeviceContainer(ns3::Ptr<ns3::NetDevice> dev) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::NetDevice >', 'dev')])
    ## net-device-container.h (module 'network'): ns3::NetDeviceContainer::NetDeviceContainer(std::string devName) [constructor]
    cls.add_constructor([param('std::string', 'devName')])
    ## net-device-container.h (module 'network'): ns3::NetDeviceContainer::NetDeviceContainer(ns3::NetDeviceContainer const & a, ns3::NetDeviceContainer const & b) [constructor]
    cls.add_constructor([param('ns3::NetDeviceContainer const &', 'a'), param('ns3::NetDeviceContainer const &', 'b')])
    ## net-device-container.h (module 'network'): void ns3::NetDeviceContainer::Add(ns3::NetDeviceContainer other) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::NetDeviceContainer', 'other')])
    ## net-device-container.h (module 'network'): void ns3::NetDeviceContainer::Add(ns3::Ptr<ns3::NetDevice> device) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device')])
    ## net-device-container.h (module 'network'): void ns3::NetDeviceContainer::Add(std::string deviceName) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'deviceName')])
    ## net-device-container.h (module 'network'): ns3::NetDeviceContainer::Iterator ns3::NetDeviceContainer::Begin() const [member function]
    cls.add_method('Begin', 
                   'ns3::NetDeviceContainer::Iterator', 
                   [], 
                   is_const=True)
    ## net-device-container.h (module 'network'): ns3::NetDeviceContainer::Iterator ns3::NetDeviceContainer::End() const [member function]
    cls.add_method('End', 
                   'ns3::NetDeviceContainer::Iterator', 
                   [], 
                   is_const=True)
    ## net-device-container.h (module 'network'): ns3::Ptr<ns3::NetDevice> ns3::NetDeviceContainer::Get(uint32_t i) const [member function]
    cls.add_method('Get', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## net-device-container.h (module 'network'): uint32_t ns3::NetDeviceContainer::GetN() const [member function]
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    return

def register_Ns3NodeContainer_methods(root_module, cls):
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & arg0) [constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'arg0')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer() [constructor]
    cls.add_constructor([])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::Ptr<ns3::Node> node) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::Node >', 'node')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(std::string nodeName) [constructor]
    cls.add_constructor([param('std::string', 'nodeName')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & a, ns3::NodeContainer const & b) [constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & a, ns3::NodeContainer const & b, ns3::NodeContainer const & c) [constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b'), param('ns3::NodeContainer const &', 'c')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & a, ns3::NodeContainer const & b, ns3::NodeContainer const & c, ns3::NodeContainer const & d) [constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b'), param('ns3::NodeContainer const &', 'c'), param('ns3::NodeContainer const &', 'd')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & a, ns3::NodeContainer const & b, ns3::NodeContainer const & c, ns3::NodeContainer const & d, ns3::NodeContainer const & e) [constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b'), param('ns3::NodeContainer const &', 'c'), param('ns3::NodeContainer const &', 'd'), param('ns3::NodeContainer const &', 'e')])
    ## node-container.h (module 'network'): void ns3::NodeContainer::Add(ns3::NodeContainer other) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::NodeContainer', 'other')])
    ## node-container.h (module 'network'): void ns3::NodeContainer::Add(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')])
    ## node-container.h (module 'network'): void ns3::NodeContainer::Add(std::string nodeName) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'nodeName')])
    ## node-container.h (module 'network'): ns3::NodeContainer::Iterator ns3::NodeContainer::Begin() const [member function]
    cls.add_method('Begin', 
                   'ns3::NodeContainer::Iterator', 
                   [], 
                   is_const=True)
    ## node-container.h (module 'network'): bool ns3::NodeContainer::Contains(uint32_t id) const [member function]
    cls.add_method('Contains', 
                   'bool', 
                   [param('uint32_t', 'id')], 
                   is_const=True)
    ## node-container.h (module 'network'): void ns3::NodeContainer::Create(uint32_t n) [member function]
    cls.add_method('Create', 
                   'void', 
                   [param('uint32_t', 'n')])
    ## node-container.h (module 'network'): void ns3::NodeContainer::Create(uint32_t n, uint32_t systemId) [member function]
    cls.add_method('Create', 
                   'void', 
                   [param('uint32_t', 'n'), param('uint32_t', 'systemId')])
    ## node-container.h (module 'network'): ns3::NodeContainer::Iterator ns3::NodeContainer::End() const [member function]
    cls.add_method('End', 
                   'ns3::NodeContainer::Iterator', 
                   [], 
                   is_const=True)
    ## node-container.h (module 'network'): ns3::Ptr<ns3::Node> ns3::NodeContainer::Get(uint32_t i) const [member function]
    cls.add_method('Get', 
                   'ns3::Ptr< ns3::Node >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## node-container.h (module 'network'): static ns3::NodeContainer ns3::NodeContainer::GetGlobal() [member function]
    cls.add_method('GetGlobal', 
                   'ns3::NodeContainer', 
                   [], 
                   is_static=True)
    ## node-container.h (module 'network'): uint32_t ns3::NodeContainer::GetN() const [member function]
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    return

def register_Ns3ObjectBase_methods(root_module, cls):
    ## object-base.h (module 'core'): ns3::ObjectBase::ObjectBase() [constructor]
    cls.add_constructor([])
    ## object-base.h (module 'core'): ns3::ObjectBase::ObjectBase(ns3::ObjectBase const & arg0) [constructor]
    cls.add_constructor([param('ns3::ObjectBase const &', 'arg0')])
    ## object-base.h (module 'core'): void ns3::ObjectBase::GetAttribute(std::string name, ns3::AttributeValue & value) const [member function]
    cls.add_method('GetAttribute', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue &', 'value')], 
                   is_const=True)
    ## object-base.h (module 'core'): bool ns3::ObjectBase::GetAttributeFailSafe(std::string name, ns3::AttributeValue & value) const [member function]
    cls.add_method('GetAttributeFailSafe', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::AttributeValue &', 'value')], 
                   is_const=True)
    ## object-base.h (module 'core'): ns3::TypeId ns3::ObjectBase::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## object-base.h (module 'core'): static ns3::TypeId ns3::ObjectBase::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## object-base.h (module 'core'): void ns3::ObjectBase::SetAttribute(std::string name, ns3::AttributeValue const & value) [member function]
    cls.add_method('SetAttribute', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::SetAttributeFailSafe(std::string name, ns3::AttributeValue const & value) [member function]
    cls.add_method('SetAttributeFailSafe', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::TraceConnect(std::string name, std::string context, ns3::CallbackBase const & cb) [member function]
    cls.add_method('TraceConnect', 
                   'bool', 
                   [param('std::string', 'name'), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::TraceConnectWithoutContext(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('TraceConnectWithoutContext', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::TraceDisconnect(std::string name, std::string context, ns3::CallbackBase const & cb) [member function]
    cls.add_method('TraceDisconnect', 
                   'bool', 
                   [param('std::string', 'name'), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::TraceDisconnectWithoutContext(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('TraceDisconnectWithoutContext', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## object-base.h (module 'core'): void ns3::ObjectBase::ConstructSelf(ns3::AttributeConstructionList const & attributes) [member function]
    cls.add_method('ConstructSelf', 
                   'void', 
                   [param('ns3::AttributeConstructionList const &', 'attributes')], 
                   visibility='protected')
    ## object-base.h (module 'core'): void ns3::ObjectBase::NotifyConstructionCompleted() [member function]
    cls.add_method('NotifyConstructionCompleted', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3ObjectDeleter_methods(root_module, cls):
    ## object.h (module 'core'): ns3::ObjectDeleter::ObjectDeleter() [constructor]
    cls.add_constructor([])
    ## object.h (module 'core'): ns3::ObjectDeleter::ObjectDeleter(ns3::ObjectDeleter const & arg0) [constructor]
    cls.add_constructor([param('ns3::ObjectDeleter const &', 'arg0')])
    ## object.h (module 'core'): static void ns3::ObjectDeleter::Delete(ns3::Object * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::Object *', 'object')], 
                   is_static=True)
    return

def register_Ns3ObjectFactory_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## object-factory.h (module 'core'): ns3::ObjectFactory::ObjectFactory(ns3::ObjectFactory const & arg0) [constructor]
    cls.add_constructor([param('ns3::ObjectFactory const &', 'arg0')])
    ## object-factory.h (module 'core'): ns3::ObjectFactory::ObjectFactory() [constructor]
    cls.add_constructor([])
    ## object-factory.h (module 'core'): ns3::ObjectFactory::ObjectFactory(std::string typeId) [constructor]
    cls.add_constructor([param('std::string', 'typeId')])
    ## object-factory.h (module 'core'): ns3::Ptr<ns3::Object> ns3::ObjectFactory::Create() const [member function]
    cls.add_method('Create', 
                   'ns3::Ptr< ns3::Object >', 
                   [], 
                   is_const=True)
    ## object-factory.h (module 'core'): ns3::TypeId ns3::ObjectFactory::GetTypeId() const [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    ## object-factory.h (module 'core'): void ns3::ObjectFactory::Set(std::string name, ns3::AttributeValue const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    ## object-factory.h (module 'core'): void ns3::ObjectFactory::SetTypeId(ns3::TypeId tid) [member function]
    cls.add_method('SetTypeId', 
                   'void', 
                   [param('ns3::TypeId', 'tid')])
    ## object-factory.h (module 'core'): void ns3::ObjectFactory::SetTypeId(char const * tid) [member function]
    cls.add_method('SetTypeId', 
                   'void', 
                   [param('char const *', 'tid')])
    ## object-factory.h (module 'core'): void ns3::ObjectFactory::SetTypeId(std::string tid) [member function]
    cls.add_method('SetTypeId', 
                   'void', 
                   [param('std::string', 'tid')])
    return

def register_Ns3PacketId_methods(root_module, cls):
    ## lora-network.h (module 'lora'): ns3::PacketId::PacketId() [constructor]
    cls.add_constructor([])
    ## lora-network.h (module 'lora'): ns3::PacketId::PacketId(ns3::PacketId const & arg0) [constructor]
    cls.add_constructor([param('ns3::PacketId const &', 'arg0')])
    ## lora-network.h (module 'lora'): ns3::PacketId::address [variable]
    cls.add_instance_attribute('address', 'ns3::Address', is_const=False)
    ## lora-network.h (module 'lora'): ns3::PacketId::packetCounter [variable]
    cls.add_instance_attribute('packetCounter', 'uint32_t', is_const=False)
    return

def register_Ns3PacketMetadata_methods(root_module, cls):
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::PacketMetadata(uint64_t uid, uint32_t size) [constructor]
    cls.add_constructor([param('uint64_t', 'uid'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::PacketMetadata(ns3::PacketMetadata const & o) [constructor]
    cls.add_constructor([param('ns3::PacketMetadata const &', 'o')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::AddAtEnd(ns3::PacketMetadata const & o) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('ns3::PacketMetadata const &', 'o')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::AddHeader(ns3::Header const & header, uint32_t size) [member function]
    cls.add_method('AddHeader', 
                   'void', 
                   [param('ns3::Header const &', 'header'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::AddPaddingAtEnd(uint32_t end) [member function]
    cls.add_method('AddPaddingAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::AddTrailer(ns3::Trailer const & trailer, uint32_t size) [member function]
    cls.add_method('AddTrailer', 
                   'void', 
                   [param('ns3::Trailer const &', 'trailer'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::ItemIterator ns3::PacketMetadata::BeginItem(ns3::Buffer buffer) const [member function]
    cls.add_method('BeginItem', 
                   'ns3::PacketMetadata::ItemIterator', 
                   [param('ns3::Buffer', 'buffer')], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata ns3::PacketMetadata::CreateFragment(uint32_t start, uint32_t end) const [member function]
    cls.add_method('CreateFragment', 
                   'ns3::PacketMetadata', 
                   [param('uint32_t', 'start'), param('uint32_t', 'end')], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): uint32_t ns3::PacketMetadata::Deserialize(uint8_t const * buffer, uint32_t size) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): static void ns3::PacketMetadata::Enable() [member function]
    cls.add_method('Enable', 
                   'void', 
                   [], 
                   is_static=True)
    ## packet-metadata.h (module 'network'): static void ns3::PacketMetadata::EnableChecking() [member function]
    cls.add_method('EnableChecking', 
                   'void', 
                   [], 
                   is_static=True)
    ## packet-metadata.h (module 'network'): uint32_t ns3::PacketMetadata::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): uint64_t ns3::PacketMetadata::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::RemoveAtEnd(uint32_t end) [member function]
    cls.add_method('RemoveAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::RemoveAtStart(uint32_t start) [member function]
    cls.add_method('RemoveAtStart', 
                   'void', 
                   [param('uint32_t', 'start')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::RemoveHeader(ns3::Header const & header, uint32_t size) [member function]
    cls.add_method('RemoveHeader', 
                   'void', 
                   [param('ns3::Header const &', 'header'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::RemoveTrailer(ns3::Trailer const & trailer, uint32_t size) [member function]
    cls.add_method('RemoveTrailer', 
                   'void', 
                   [param('ns3::Trailer const &', 'trailer'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): uint32_t ns3::PacketMetadata::Serialize(uint8_t * buffer, uint32_t maxSize) const [member function]
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    return

def register_Ns3PacketMetadataItem_methods(root_module, cls):
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::Item() [constructor]
    cls.add_constructor([])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::Item(ns3::PacketMetadata::Item const & arg0) [constructor]
    cls.add_constructor([param('ns3::PacketMetadata::Item const &', 'arg0')])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::current [variable]
    cls.add_instance_attribute('current', 'ns3::Buffer::Iterator', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::currentSize [variable]
    cls.add_instance_attribute('currentSize', 'uint32_t', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::currentTrimedFromEnd [variable]
    cls.add_instance_attribute('currentTrimedFromEnd', 'uint32_t', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::currentTrimedFromStart [variable]
    cls.add_instance_attribute('currentTrimedFromStart', 'uint32_t', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::isFragment [variable]
    cls.add_instance_attribute('isFragment', 'bool', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::tid [variable]
    cls.add_instance_attribute('tid', 'ns3::TypeId', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::type [variable]
    cls.add_instance_attribute('type', 'ns3::PacketMetadata::Item::ItemType', is_const=False)
    return

def register_Ns3PacketMetadataItemIterator_methods(root_module, cls):
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::ItemIterator::ItemIterator(ns3::PacketMetadata::ItemIterator const & arg0) [constructor]
    cls.add_constructor([param('ns3::PacketMetadata::ItemIterator const &', 'arg0')])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::ItemIterator::ItemIterator(ns3::PacketMetadata const * metadata, ns3::Buffer buffer) [constructor]
    cls.add_constructor([param('ns3::PacketMetadata const *', 'metadata'), param('ns3::Buffer', 'buffer')])
    ## packet-metadata.h (module 'network'): bool ns3::PacketMetadata::ItemIterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item ns3::PacketMetadata::ItemIterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::PacketMetadata::Item', 
                   [])
    return

def register_Ns3PacketStats_methods(root_module, cls):
    ## lora-network.h (module 'lora'): ns3::PacketStats::PacketStats() [constructor]
    cls.add_constructor([])
    ## lora-network.h (module 'lora'): ns3::PacketStats::PacketStats(ns3::PacketStats const & arg0) [constructor]
    cls.add_constructor([param('ns3::PacketStats const &', 'arg0')])
    ## lora-network.h (module 'lora'): ns3::PacketStats::gwCount [variable]
    cls.add_instance_attribute('gwCount', 'uint32_t', is_const=False)
    ## lora-network.h (module 'lora'): ns3::PacketStats::maxRssi [variable]
    cls.add_instance_attribute('maxRssi', 'double', is_const=False)
    ## lora-network.h (module 'lora'): ns3::PacketStats::strongestGateway [variable]
    cls.add_instance_attribute('strongestGateway', 'ns3::Address', is_const=False)
    return

def register_Ns3PacketTagIterator_methods(root_module, cls):
    ## packet.h (module 'network'): ns3::PacketTagIterator::PacketTagIterator(ns3::PacketTagIterator const & arg0) [constructor]
    cls.add_constructor([param('ns3::PacketTagIterator const &', 'arg0')])
    ## packet.h (module 'network'): bool ns3::PacketTagIterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::PacketTagIterator::Item ns3::PacketTagIterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::PacketTagIterator::Item', 
                   [])
    return

def register_Ns3PacketTagIteratorItem_methods(root_module, cls):
    ## packet.h (module 'network'): ns3::PacketTagIterator::Item::Item(ns3::PacketTagIterator::Item const & arg0) [constructor]
    cls.add_constructor([param('ns3::PacketTagIterator::Item const &', 'arg0')])
    ## packet.h (module 'network'): void ns3::PacketTagIterator::Item::GetTag(ns3::Tag & tag) const [member function]
    cls.add_method('GetTag', 
                   'void', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::TypeId ns3::PacketTagIterator::Item::GetTypeId() const [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    return

def register_Ns3PacketTagList_methods(root_module, cls):
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::PacketTagList() [constructor]
    cls.add_constructor([])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::PacketTagList(ns3::PacketTagList const & o) [constructor]
    cls.add_constructor([param('ns3::PacketTagList const &', 'o')])
    ## packet-tag-list.h (module 'network'): void ns3::PacketTagList::Add(ns3::Tag const & tag) const [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Tag const &', 'tag')], 
                   is_const=True)
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData const * ns3::PacketTagList::Head() const [member function]
    cls.add_method('Head', 
                   'ns3::PacketTagList::TagData const *', 
                   [], 
                   is_const=True)
    ## packet-tag-list.h (module 'network'): bool ns3::PacketTagList::Peek(ns3::Tag & tag) const [member function]
    cls.add_method('Peek', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet-tag-list.h (module 'network'): bool ns3::PacketTagList::Remove(ns3::Tag & tag) [member function]
    cls.add_method('Remove', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    ## packet-tag-list.h (module 'network'): void ns3::PacketTagList::RemoveAll() [member function]
    cls.add_method('RemoveAll', 
                   'void', 
                   [])
    ## packet-tag-list.h (module 'network'): bool ns3::PacketTagList::Replace(ns3::Tag & tag) [member function]
    cls.add_method('Replace', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    return

def register_Ns3PacketTagListTagData_methods(root_module, cls):
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::TagData() [constructor]
    cls.add_constructor([])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::TagData(ns3::PacketTagList::TagData const & arg0) [constructor]
    cls.add_constructor([param('ns3::PacketTagList::TagData const &', 'arg0')])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::count [variable]
    cls.add_instance_attribute('count', 'uint32_t', is_const=False)
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::data [variable]
    cls.add_instance_attribute('data', 'uint8_t [ 1 ]', is_const=False)
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::next [variable]
    cls.add_instance_attribute('next', 'ns3::PacketTagList::TagData *', is_const=False)
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::size [variable]
    cls.add_instance_attribute('size', 'uint32_t', is_const=False)
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::tid [variable]
    cls.add_instance_attribute('tid', 'ns3::TypeId', is_const=False)
    return

def register_Ns3PcapFile_methods(root_module, cls):
    ## pcap-file.h (module 'network'): ns3::PcapFile::PcapFile() [constructor]
    cls.add_constructor([])
    ## pcap-file.h (module 'network'): void ns3::PcapFile::Clear() [member function]
    cls.add_method('Clear', 
                   'void', 
                   [])
    ## pcap-file.h (module 'network'): void ns3::PcapFile::Close() [member function]
    cls.add_method('Close', 
                   'void', 
                   [])
    ## pcap-file.h (module 'network'): static bool ns3::PcapFile::Diff(std::string const & f1, std::string const & f2, uint32_t & sec, uint32_t & usec, uint32_t & packets, uint32_t snapLen=ns3::PcapFile::SNAPLEN_DEFAULT) [member function]
    cls.add_method('Diff', 
                   'bool', 
                   [param('std::string const &', 'f1'), param('std::string const &', 'f2'), param('uint32_t &', 'sec'), param('uint32_t &', 'usec'), param('uint32_t &', 'packets'), param('uint32_t', 'snapLen', default_value='ns3::PcapFile::SNAPLEN_DEFAULT')], 
                   is_static=True)
    ## pcap-file.h (module 'network'): bool ns3::PcapFile::Eof() const [member function]
    cls.add_method('Eof', 
                   'bool', 
                   [], 
                   is_const=True)
    ## pcap-file.h (module 'network'): bool ns3::PcapFile::Fail() const [member function]
    cls.add_method('Fail', 
                   'bool', 
                   [], 
                   is_const=True)
    ## pcap-file.h (module 'network'): uint32_t ns3::PcapFile::GetDataLinkType() [member function]
    cls.add_method('GetDataLinkType', 
                   'uint32_t', 
                   [])
    ## pcap-file.h (module 'network'): uint32_t ns3::PcapFile::GetMagic() [member function]
    cls.add_method('GetMagic', 
                   'uint32_t', 
                   [])
    ## pcap-file.h (module 'network'): uint32_t ns3::PcapFile::GetSigFigs() [member function]
    cls.add_method('GetSigFigs', 
                   'uint32_t', 
                   [])
    ## pcap-file.h (module 'network'): uint32_t ns3::PcapFile::GetSnapLen() [member function]
    cls.add_method('GetSnapLen', 
                   'uint32_t', 
                   [])
    ## pcap-file.h (module 'network'): bool ns3::PcapFile::GetSwapMode() [member function]
    cls.add_method('GetSwapMode', 
                   'bool', 
                   [])
    ## pcap-file.h (module 'network'): int32_t ns3::PcapFile::GetTimeZoneOffset() [member function]
    cls.add_method('GetTimeZoneOffset', 
                   'int32_t', 
                   [])
    ## pcap-file.h (module 'network'): uint16_t ns3::PcapFile::GetVersionMajor() [member function]
    cls.add_method('GetVersionMajor', 
                   'uint16_t', 
                   [])
    ## pcap-file.h (module 'network'): uint16_t ns3::PcapFile::GetVersionMinor() [member function]
    cls.add_method('GetVersionMinor', 
                   'uint16_t', 
                   [])
    ## pcap-file.h (module 'network'): void ns3::PcapFile::Init(uint32_t dataLinkType, uint32_t snapLen=ns3::PcapFile::SNAPLEN_DEFAULT, int32_t timeZoneCorrection=ns3::PcapFile::ZONE_DEFAULT, bool swapMode=false, bool nanosecMode=false) [member function]
    cls.add_method('Init', 
                   'void', 
                   [param('uint32_t', 'dataLinkType'), param('uint32_t', 'snapLen', default_value='ns3::PcapFile::SNAPLEN_DEFAULT'), param('int32_t', 'timeZoneCorrection', default_value='ns3::PcapFile::ZONE_DEFAULT'), param('bool', 'swapMode', default_value='false'), param('bool', 'nanosecMode', default_value='false')])
    ## pcap-file.h (module 'network'): bool ns3::PcapFile::IsNanoSecMode() [member function]
    cls.add_method('IsNanoSecMode', 
                   'bool', 
                   [])
    ## pcap-file.h (module 'network'): void ns3::PcapFile::Open(std::string const & filename, std::ios_base::openmode mode) [member function]
    cls.add_method('Open', 
                   'void', 
                   [param('std::string const &', 'filename'), param('std::ios_base::openmode', 'mode')])
    ## pcap-file.h (module 'network'): void ns3::PcapFile::Read(uint8_t * const data, uint32_t maxBytes, uint32_t & tsSec, uint32_t & tsUsec, uint32_t & inclLen, uint32_t & origLen, uint32_t & readLen) [member function]
    cls.add_method('Read', 
                   'void', 
                   [param('uint8_t * const', 'data'), param('uint32_t', 'maxBytes'), param('uint32_t &', 'tsSec'), param('uint32_t &', 'tsUsec'), param('uint32_t &', 'inclLen'), param('uint32_t &', 'origLen'), param('uint32_t &', 'readLen')])
    ## pcap-file.h (module 'network'): void ns3::PcapFile::Write(uint32_t tsSec, uint32_t tsUsec, uint8_t const * const data, uint32_t totalLen) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('uint32_t', 'tsSec'), param('uint32_t', 'tsUsec'), param('uint8_t const * const', 'data'), param('uint32_t', 'totalLen')])
    ## pcap-file.h (module 'network'): void ns3::PcapFile::Write(uint32_t tsSec, uint32_t tsUsec, ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('uint32_t', 'tsSec'), param('uint32_t', 'tsUsec'), param('ns3::Ptr< ns3::Packet const >', 'p')])
    ## pcap-file.h (module 'network'): void ns3::PcapFile::Write(uint32_t tsSec, uint32_t tsUsec, ns3::Header const & header, ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('uint32_t', 'tsSec'), param('uint32_t', 'tsUsec'), param('ns3::Header const &', 'header'), param('ns3::Ptr< ns3::Packet const >', 'p')])
    ## pcap-file.h (module 'network'): ns3::PcapFile::SNAPLEN_DEFAULT [variable]
    cls.add_static_attribute('SNAPLEN_DEFAULT', 'uint32_t const', is_const=True)
    ## pcap-file.h (module 'network'): ns3::PcapFile::ZONE_DEFAULT [variable]
    cls.add_static_attribute('ZONE_DEFAULT', 'int32_t const', is_const=True)
    return

def register_Ns3PcapHelper_methods(root_module, cls):
    ## trace-helper.h (module 'network'): ns3::PcapHelper::PcapHelper(ns3::PcapHelper const & arg0) [constructor]
    cls.add_constructor([param('ns3::PcapHelper const &', 'arg0')])
    ## trace-helper.h (module 'network'): ns3::PcapHelper::PcapHelper() [constructor]
    cls.add_constructor([])
    ## trace-helper.h (module 'network'): ns3::Ptr<ns3::PcapFileWrapper> ns3::PcapHelper::CreateFile(std::string filename, std::ios_base::openmode filemode, ns3::PcapHelper::DataLinkType dataLinkType, uint32_t snapLen=std::numeric_limits<unsigned int>::max(), int32_t tzCorrection=0) [member function]
    cls.add_method('CreateFile', 
                   'ns3::Ptr< ns3::PcapFileWrapper >', 
                   [param('std::string', 'filename'), param('std::ios_base::openmode', 'filemode'), param('ns3::PcapHelper::DataLinkType', 'dataLinkType'), param('uint32_t', 'snapLen', default_value='std::numeric_limits<unsigned int>::max()'), param('int32_t', 'tzCorrection', default_value='0')])
    ## trace-helper.h (module 'network'): std::string ns3::PcapHelper::GetFilenameFromDevice(std::string prefix, ns3::Ptr<ns3::NetDevice> device, bool useObjectNames=true) [member function]
    cls.add_method('GetFilenameFromDevice', 
                   'std::string', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'device'), param('bool', 'useObjectNames', default_value='true')])
    ## trace-helper.h (module 'network'): std::string ns3::PcapHelper::GetFilenameFromInterfacePair(std::string prefix, ns3::Ptr<ns3::Object> object, uint32_t interface, bool useObjectNames=true) [member function]
    cls.add_method('GetFilenameFromInterfacePair', 
                   'std::string', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::Object >', 'object'), param('uint32_t', 'interface'), param('bool', 'useObjectNames', default_value='true')])
    return

def register_Ns3PcapHelperForDevice_methods(root_module, cls):
    ## trace-helper.h (module 'network'): ns3::PcapHelperForDevice::PcapHelperForDevice(ns3::PcapHelperForDevice const & arg0) [constructor]
    cls.add_constructor([param('ns3::PcapHelperForDevice const &', 'arg0')])
    ## trace-helper.h (module 'network'): ns3::PcapHelperForDevice::PcapHelperForDevice() [constructor]
    cls.add_constructor([])
    ## trace-helper.h (module 'network'): void ns3::PcapHelperForDevice::EnablePcap(std::string prefix, ns3::Ptr<ns3::NetDevice> nd, bool promiscuous=false, bool explicitFilename=false) [member function]
    cls.add_method('EnablePcap', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'nd'), param('bool', 'promiscuous', default_value='false'), param('bool', 'explicitFilename', default_value='false')])
    ## trace-helper.h (module 'network'): void ns3::PcapHelperForDevice::EnablePcap(std::string prefix, std::string ndName, bool promiscuous=false, bool explicitFilename=false) [member function]
    cls.add_method('EnablePcap', 
                   'void', 
                   [param('std::string', 'prefix'), param('std::string', 'ndName'), param('bool', 'promiscuous', default_value='false'), param('bool', 'explicitFilename', default_value='false')])
    ## trace-helper.h (module 'network'): void ns3::PcapHelperForDevice::EnablePcap(std::string prefix, ns3::NetDeviceContainer d, bool promiscuous=false) [member function]
    cls.add_method('EnablePcap', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::NetDeviceContainer', 'd'), param('bool', 'promiscuous', default_value='false')])
    ## trace-helper.h (module 'network'): void ns3::PcapHelperForDevice::EnablePcap(std::string prefix, ns3::NodeContainer n, bool promiscuous=false) [member function]
    cls.add_method('EnablePcap', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::NodeContainer', 'n'), param('bool', 'promiscuous', default_value='false')])
    ## trace-helper.h (module 'network'): void ns3::PcapHelperForDevice::EnablePcap(std::string prefix, uint32_t nodeid, uint32_t deviceid, bool promiscuous=false) [member function]
    cls.add_method('EnablePcap', 
                   'void', 
                   [param('std::string', 'prefix'), param('uint32_t', 'nodeid'), param('uint32_t', 'deviceid'), param('bool', 'promiscuous', default_value='false')])
    ## trace-helper.h (module 'network'): void ns3::PcapHelperForDevice::EnablePcapAll(std::string prefix, bool promiscuous=false) [member function]
    cls.add_method('EnablePcapAll', 
                   'void', 
                   [param('std::string', 'prefix'), param('bool', 'promiscuous', default_value='false')])
    ## trace-helper.h (module 'network'): void ns3::PcapHelperForDevice::EnablePcapInternal(std::string prefix, ns3::Ptr<ns3::NetDevice> nd, bool promiscuous, bool explicitFilename) [member function]
    cls.add_method('EnablePcapInternal', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'nd'), param('bool', 'promiscuous'), param('bool', 'explicitFilename')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3SimpleRefCount__Ns3Object_Ns3ObjectBase_Ns3ObjectDeleter_methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter>::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter>::SimpleRefCount(ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter> const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter > const &', 'o')])
    return

def register_Ns3Simulator_methods(root_module, cls):
    ## simulator.h (module 'core'): ns3::Simulator::Simulator(ns3::Simulator const & arg0) [constructor]
    cls.add_constructor([param('ns3::Simulator const &', 'arg0')])
    ## simulator.h (module 'core'): static void ns3::Simulator::Cancel(ns3::EventId const & id) [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::Destroy() [member function]
    cls.add_method('Destroy', 
                   'void', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static uint32_t ns3::Simulator::GetContext() [member function]
    cls.add_method('GetContext', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static ns3::Time ns3::Simulator::GetDelayLeft(ns3::EventId const & id) [member function]
    cls.add_method('GetDelayLeft', 
                   'ns3::Time', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    ## simulator.h (module 'core'): static ns3::Ptr<ns3::SimulatorImpl> ns3::Simulator::GetImplementation() [member function]
    cls.add_method('GetImplementation', 
                   'ns3::Ptr< ns3::SimulatorImpl >', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static ns3::Time ns3::Simulator::GetMaximumSimulationTime() [member function]
    cls.add_method('GetMaximumSimulationTime', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static uint32_t ns3::Simulator::GetSystemId() [member function]
    cls.add_method('GetSystemId', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static bool ns3::Simulator::IsExpired(ns3::EventId const & id) [member function]
    cls.add_method('IsExpired', 
                   'bool', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    ## simulator.h (module 'core'): static bool ns3::Simulator::IsFinished() [member function]
    cls.add_method('IsFinished', 
                   'bool', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static ns3::Time ns3::Simulator::Now() [member function]
    cls.add_method('Now', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::Remove(ns3::EventId const & id) [member function]
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::SetImplementation(ns3::Ptr<ns3::SimulatorImpl> impl) [member function]
    cls.add_method('SetImplementation', 
                   'void', 
                   [param('ns3::Ptr< ns3::SimulatorImpl >', 'impl')], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::SetScheduler(ns3::ObjectFactory schedulerFactory) [member function]
    cls.add_method('SetScheduler', 
                   'void', 
                   [param('ns3::ObjectFactory', 'schedulerFactory')], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::Stop() [member function]
    cls.add_method('Stop', 
                   'void', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::Stop(ns3::Time const & delay) [member function]
    cls.add_method('Stop', 
                   'void', 
                   [param('ns3::Time const &', 'delay')], 
                   is_static=True)
    return

def register_Ns3Tag_methods(root_module, cls):
    ## tag.h (module 'network'): ns3::Tag::Tag() [constructor]
    cls.add_constructor([])
    ## tag.h (module 'network'): ns3::Tag::Tag(ns3::Tag const & arg0) [constructor]
    cls.add_constructor([param('ns3::Tag const &', 'arg0')])
    ## tag.h (module 'network'): void ns3::Tag::Deserialize(ns3::TagBuffer i) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_pure_virtual=True, is_virtual=True)
    ## tag.h (module 'network'): uint32_t ns3::Tag::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## tag.h (module 'network'): static ns3::TypeId ns3::Tag::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## tag.h (module 'network'): void ns3::Tag::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## tag.h (module 'network'): void ns3::Tag::Serialize(ns3::TagBuffer i) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3TagBuffer_methods(root_module, cls):
    ## tag-buffer.h (module 'network'): ns3::TagBuffer::TagBuffer(ns3::TagBuffer const & arg0) [constructor]
    cls.add_constructor([param('ns3::TagBuffer const &', 'arg0')])
    ## tag-buffer.h (module 'network'): ns3::TagBuffer::TagBuffer(uint8_t * start, uint8_t * end) [constructor]
    cls.add_constructor([param('uint8_t *', 'start'), param('uint8_t *', 'end')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::CopyFrom(ns3::TagBuffer o) [member function]
    cls.add_method('CopyFrom', 
                   'void', 
                   [param('ns3::TagBuffer', 'o')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::Read(uint8_t * buffer, uint32_t size) [member function]
    cls.add_method('Read', 
                   'void', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')])
    ## tag-buffer.h (module 'network'): double ns3::TagBuffer::ReadDouble() [member function]
    cls.add_method('ReadDouble', 
                   'double', 
                   [])
    ## tag-buffer.h (module 'network'): uint16_t ns3::TagBuffer::ReadU16() [member function]
    cls.add_method('ReadU16', 
                   'uint16_t', 
                   [])
    ## tag-buffer.h (module 'network'): uint32_t ns3::TagBuffer::ReadU32() [member function]
    cls.add_method('ReadU32', 
                   'uint32_t', 
                   [])
    ## tag-buffer.h (module 'network'): uint64_t ns3::TagBuffer::ReadU64() [member function]
    cls.add_method('ReadU64', 
                   'uint64_t', 
                   [])
    ## tag-buffer.h (module 'network'): uint8_t ns3::TagBuffer::ReadU8() [member function]
    cls.add_method('ReadU8', 
                   'uint8_t', 
                   [])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::TrimAtEnd(uint32_t trim) [member function]
    cls.add_method('TrimAtEnd', 
                   'void', 
                   [param('uint32_t', 'trim')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::Write(uint8_t const * buffer, uint32_t size) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteDouble(double v) [member function]
    cls.add_method('WriteDouble', 
                   'void', 
                   [param('double', 'v')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteU16(uint16_t v) [member function]
    cls.add_method('WriteU16', 
                   'void', 
                   [param('uint16_t', 'v')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteU32(uint32_t v) [member function]
    cls.add_method('WriteU32', 
                   'void', 
                   [param('uint32_t', 'v')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteU64(uint64_t v) [member function]
    cls.add_method('WriteU64', 
                   'void', 
                   [param('uint64_t', 'v')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteU8(uint8_t v) [member function]
    cls.add_method('WriteU8', 
                   'void', 
                   [param('uint8_t', 'v')])
    return

def register_Ns3TimeWithUnit_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## nstime.h (module 'core'): ns3::TimeWithUnit::TimeWithUnit(ns3::TimeWithUnit const & arg0) [constructor]
    cls.add_constructor([param('ns3::TimeWithUnit const &', 'arg0')])
    ## nstime.h (module 'core'): ns3::TimeWithUnit::TimeWithUnit(ns3::Time const time, ns3::Time::Unit const unit) [constructor]
    cls.add_constructor([param('ns3::Time const', 'time'), param('ns3::Time::Unit const', 'unit')])
    return

def register_Ns3TracedValue__Double_methods(root_module, cls):
    ## traced-value.h (module 'core'): ns3::TracedValue<double>::TracedValue() [constructor]
    cls.add_constructor([])
    ## traced-value.h (module 'core'): ns3::TracedValue<double>::TracedValue(ns3::TracedValue<double> const & o) [constructor]
    cls.add_constructor([param('ns3::TracedValue< double > const &', 'o')])
    ## traced-value.h (module 'core'): ns3::TracedValue<double>::TracedValue(double const & v) [constructor]
    cls.add_constructor([param('double const &', 'v')])
    ## traced-value.h (module 'core'): ns3::TracedValue<double>::TracedValue(ns3::TracedValue<double> const & other) [constructor]
    cls.add_constructor([param('ns3::TracedValue< double > const &', 'other')])
    ## traced-value.h (module 'core'): ns3::TracedValue<double>::TracedValue(ns3::TracedValue<double> const & other) [constructor]
    cls.add_constructor([param('ns3::TracedValue< double > const &', 'other')])
    ## traced-value.h (module 'core'): void ns3::TracedValue<double>::Connect(ns3::CallbackBase const & cb, std::string path) [member function]
    cls.add_method('Connect', 
                   'void', 
                   [param('ns3::CallbackBase const &', 'cb'), param('std::string', 'path')])
    ## traced-value.h (module 'core'): void ns3::TracedValue<double>::ConnectWithoutContext(ns3::CallbackBase const & cb) [member function]
    cls.add_method('ConnectWithoutContext', 
                   'void', 
                   [param('ns3::CallbackBase const &', 'cb')])
    ## traced-value.h (module 'core'): void ns3::TracedValue<double>::Disconnect(ns3::CallbackBase const & cb, std::string path) [member function]
    cls.add_method('Disconnect', 
                   'void', 
                   [param('ns3::CallbackBase const &', 'cb'), param('std::string', 'path')])
    ## traced-value.h (module 'core'): void ns3::TracedValue<double>::DisconnectWithoutContext(ns3::CallbackBase const & cb) [member function]
    cls.add_method('DisconnectWithoutContext', 
                   'void', 
                   [param('ns3::CallbackBase const &', 'cb')])
    ## traced-value.h (module 'core'): double ns3::TracedValue<double>::Get() const [member function]
    cls.add_method('Get', 
                   'double', 
                   [], 
                   is_const=True)
    ## traced-value.h (module 'core'): void ns3::TracedValue<double>::Set(double const & v) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('double const &', 'v')])
    return

def register_Ns3TracedValue__Ns3LoRaPhyState_methods(root_module, cls):
    ## traced-value.h (module 'core'): ns3::TracedValue<ns3::LoRaPhy::State>::TracedValue() [constructor]
    cls.add_constructor([])
    ## traced-value.h (module 'core'): ns3::TracedValue<ns3::LoRaPhy::State>::TracedValue(ns3::TracedValue<ns3::LoRaPhy::State> const & o) [constructor]
    cls.add_constructor([param('ns3::TracedValue< ns3::LoRaPhy::State > const &', 'o')])
    ## traced-value.h (module 'core'): ns3::TracedValue<ns3::LoRaPhy::State>::TracedValue(ns3::LoRaPhy::State const & v) [constructor]
    cls.add_constructor([param('ns3::LoRaPhy::State const &', 'v')])
    ## traced-value.h (module 'core'): void ns3::TracedValue<ns3::LoRaPhy::State>::Connect(ns3::CallbackBase const & cb, std::string path) [member function]
    cls.add_method('Connect', 
                   'void', 
                   [param('ns3::CallbackBase const &', 'cb'), param('std::string', 'path')])
    ## traced-value.h (module 'core'): void ns3::TracedValue<ns3::LoRaPhy::State>::ConnectWithoutContext(ns3::CallbackBase const & cb) [member function]
    cls.add_method('ConnectWithoutContext', 
                   'void', 
                   [param('ns3::CallbackBase const &', 'cb')])
    ## traced-value.h (module 'core'): void ns3::TracedValue<ns3::LoRaPhy::State>::Disconnect(ns3::CallbackBase const & cb, std::string path) [member function]
    cls.add_method('Disconnect', 
                   'void', 
                   [param('ns3::CallbackBase const &', 'cb'), param('std::string', 'path')])
    ## traced-value.h (module 'core'): void ns3::TracedValue<ns3::LoRaPhy::State>::DisconnectWithoutContext(ns3::CallbackBase const & cb) [member function]
    cls.add_method('DisconnectWithoutContext', 
                   'void', 
                   [param('ns3::CallbackBase const &', 'cb')])
    ## traced-value.h (module 'core'): ns3::LoRaPhy::State ns3::TracedValue<ns3::LoRaPhy::State>::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::LoRaPhy::State', 
                   [], 
                   is_const=True)
    ## traced-value.h (module 'core'): void ns3::TracedValue<ns3::LoRaPhy::State>::Set(ns3::LoRaPhy::State const & v) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::LoRaPhy::State const &', 'v')])
    return

def register_Ns3TypeId_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('<')
    ## type-id.h (module 'core'): ns3::TypeId::TypeId(char const * name) [constructor]
    cls.add_constructor([param('char const *', 'name')])
    ## type-id.h (module 'core'): ns3::TypeId::TypeId() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeId::TypeId(ns3::TypeId const & o) [constructor]
    cls.add_constructor([param('ns3::TypeId const &', 'o')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::AddAttribute(std::string name, std::string help, ns3::AttributeValue const & initialValue, ns3::Ptr<const ns3::AttributeAccessor> accessor, ns3::Ptr<const ns3::AttributeChecker> checker, ns3::TypeId::SupportLevel supportLevel=::ns3::TypeId::SupportLevel::SUPPORTED, std::string const & supportMsg="") [member function]
    cls.add_method('AddAttribute', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('ns3::AttributeValue const &', 'initialValue'), param('ns3::Ptr< ns3::AttributeAccessor const >', 'accessor'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker'), param('ns3::TypeId::SupportLevel', 'supportLevel', default_value='::ns3::TypeId::SupportLevel::SUPPORTED'), param('std::string const &', 'supportMsg', default_value='""')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::AddAttribute(std::string name, std::string help, uint32_t flags, ns3::AttributeValue const & initialValue, ns3::Ptr<const ns3::AttributeAccessor> accessor, ns3::Ptr<const ns3::AttributeChecker> checker, ns3::TypeId::SupportLevel supportLevel=::ns3::TypeId::SupportLevel::SUPPORTED, std::string const & supportMsg="") [member function]
    cls.add_method('AddAttribute', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('uint32_t', 'flags'), param('ns3::AttributeValue const &', 'initialValue'), param('ns3::Ptr< ns3::AttributeAccessor const >', 'accessor'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker'), param('ns3::TypeId::SupportLevel', 'supportLevel', default_value='::ns3::TypeId::SupportLevel::SUPPORTED'), param('std::string const &', 'supportMsg', default_value='""')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::AddTraceSource(std::string name, std::string help, ns3::Ptr<const ns3::TraceSourceAccessor> accessor) [member function]
    cls.add_method('AddTraceSource', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('ns3::Ptr< ns3::TraceSourceAccessor const >', 'accessor')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::AddTraceSource(std::string name, std::string help, ns3::Ptr<const ns3::TraceSourceAccessor> accessor, std::string callback, ns3::TypeId::SupportLevel supportLevel=::ns3::TypeId::SupportLevel::SUPPORTED, std::string const & supportMsg="") [member function]
    cls.add_method('AddTraceSource', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('ns3::Ptr< ns3::TraceSourceAccessor const >', 'accessor'), param('std::string', 'callback'), param('ns3::TypeId::SupportLevel', 'supportLevel', default_value='::ns3::TypeId::SupportLevel::SUPPORTED'), param('std::string const &', 'supportMsg', default_value='""')])
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation ns3::TypeId::GetAttribute(std::size_t i) const [member function]
    cls.add_method('GetAttribute', 
                   'ns3::TypeId::AttributeInformation', 
                   [param('std::size_t', 'i')], 
                   is_const=True)
    ## type-id.h (module 'core'): std::string ns3::TypeId::GetAttributeFullName(std::size_t i) const [member function]
    cls.add_method('GetAttributeFullName', 
                   'std::string', 
                   [param('std::size_t', 'i')], 
                   is_const=True)
    ## type-id.h (module 'core'): std::size_t ns3::TypeId::GetAttributeN() const [member function]
    cls.add_method('GetAttributeN', 
                   'std::size_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::Callback<ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> ns3::TypeId::GetConstructor() const [member function]
    cls.add_method('GetConstructor', 
                   'ns3::Callback< ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): std::string ns3::TypeId::GetGroupName() const [member function]
    cls.add_method('GetGroupName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::TypeId::hash_t ns3::TypeId::GetHash() const [member function]
    cls.add_method('GetHash', 
                   'ns3::TypeId::hash_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): std::string ns3::TypeId::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::GetParent() const [member function]
    cls.add_method('GetParent', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): static ns3::TypeId ns3::TypeId::GetRegistered(uint16_t i) [member function]
    cls.add_method('GetRegistered', 
                   'ns3::TypeId', 
                   [param('uint16_t', 'i')], 
                   is_static=True)
    ## type-id.h (module 'core'): static uint16_t ns3::TypeId::GetRegisteredN() [member function]
    cls.add_method('GetRegisteredN', 
                   'uint16_t', 
                   [], 
                   is_static=True)
    ## type-id.h (module 'core'): std::size_t ns3::TypeId::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'std::size_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation ns3::TypeId::GetTraceSource(std::size_t i) const [member function]
    cls.add_method('GetTraceSource', 
                   'ns3::TypeId::TraceSourceInformation', 
                   [param('std::size_t', 'i')], 
                   is_const=True)
    ## type-id.h (module 'core'): std::size_t ns3::TypeId::GetTraceSourceN() const [member function]
    cls.add_method('GetTraceSourceN', 
                   'std::size_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): uint16_t ns3::TypeId::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::HasConstructor() const [member function]
    cls.add_method('HasConstructor', 
                   'bool', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::HasParent() const [member function]
    cls.add_method('HasParent', 
                   'bool', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::HideFromDocumentation() [member function]
    cls.add_method('HideFromDocumentation', 
                   'ns3::TypeId', 
                   [])
    ## type-id.h (module 'core'): bool ns3::TypeId::IsChildOf(ns3::TypeId other) const [member function]
    cls.add_method('IsChildOf', 
                   'bool', 
                   [param('ns3::TypeId', 'other')], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::LookupAttributeByName(std::string name, ns3::TypeId::AttributeInformation * info) const [member function]
    cls.add_method('LookupAttributeByName', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::TypeId::AttributeInformation *', 'info', transfer_ownership=False)], 
                   is_const=True)
    ## type-id.h (module 'core'): static ns3::TypeId ns3::TypeId::LookupByHash(ns3::TypeId::hash_t hash) [member function]
    cls.add_method('LookupByHash', 
                   'ns3::TypeId', 
                   [param('uint32_t', 'hash')], 
                   is_static=True)
    ## type-id.h (module 'core'): static bool ns3::TypeId::LookupByHashFailSafe(ns3::TypeId::hash_t hash, ns3::TypeId * tid) [member function]
    cls.add_method('LookupByHashFailSafe', 
                   'bool', 
                   [param('uint32_t', 'hash'), param('ns3::TypeId *', 'tid')], 
                   is_static=True)
    ## type-id.h (module 'core'): static ns3::TypeId ns3::TypeId::LookupByName(std::string name) [member function]
    cls.add_method('LookupByName', 
                   'ns3::TypeId', 
                   [param('std::string', 'name')], 
                   is_static=True)
    ## type-id.h (module 'core'): ns3::Ptr<const ns3::TraceSourceAccessor> ns3::TypeId::LookupTraceSourceByName(std::string name) const [member function]
    cls.add_method('LookupTraceSourceByName', 
                   'ns3::Ptr< ns3::TraceSourceAccessor const >', 
                   [param('std::string', 'name')], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::Ptr<const ns3::TraceSourceAccessor> ns3::TypeId::LookupTraceSourceByName(std::string name, ns3::TypeId::TraceSourceInformation * info) const [member function]
    cls.add_method('LookupTraceSourceByName', 
                   'ns3::Ptr< ns3::TraceSourceAccessor const >', 
                   [param('std::string', 'name'), param('ns3::TypeId::TraceSourceInformation *', 'info')], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::MustHideFromDocumentation() const [member function]
    cls.add_method('MustHideFromDocumentation', 
                   'bool', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::SetAttributeInitialValue(std::size_t i, ns3::Ptr<const ns3::AttributeValue> initialValue) [member function]
    cls.add_method('SetAttributeInitialValue', 
                   'bool', 
                   [param('std::size_t', 'i'), param('ns3::Ptr< ns3::AttributeValue const >', 'initialValue')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::SetGroupName(std::string groupName) [member function]
    cls.add_method('SetGroupName', 
                   'ns3::TypeId', 
                   [param('std::string', 'groupName')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::SetParent(ns3::TypeId tid) [member function]
    cls.add_method('SetParent', 
                   'ns3::TypeId', 
                   [param('ns3::TypeId', 'tid')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::SetSize(std::size_t size) [member function]
    cls.add_method('SetSize', 
                   'ns3::TypeId', 
                   [param('std::size_t', 'size')])
    ## type-id.h (module 'core'): void ns3::TypeId::SetUid(uint16_t uid) [member function]
    cls.add_method('SetUid', 
                   'void', 
                   [param('uint16_t', 'uid')])
    return

def register_Ns3TypeIdAttributeInformation_methods(root_module, cls):
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::AttributeInformation() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::AttributeInformation(ns3::TypeId::AttributeInformation const & arg0) [constructor]
    cls.add_constructor([param('ns3::TypeId::AttributeInformation const &', 'arg0')])
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::accessor [variable]
    cls.add_instance_attribute('accessor', 'ns3::Ptr< ns3::AttributeAccessor const >', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::checker [variable]
    cls.add_instance_attribute('checker', 'ns3::Ptr< ns3::AttributeChecker const >', is_const=False)
    cls.add_instance_attribute('flags', 'uint32_t', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::help [variable]
    cls.add_instance_attribute('help', 'std::string', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::initialValue [variable]
    cls.add_instance_attribute('initialValue', 'ns3::Ptr< ns3::AttributeValue const >', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::name [variable]
    cls.add_instance_attribute('name', 'std::string', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::originalInitialValue [variable]
    cls.add_instance_attribute('originalInitialValue', 'ns3::Ptr< ns3::AttributeValue const >', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::supportLevel [variable]
    cls.add_instance_attribute('supportLevel', 'ns3::TypeId::SupportLevel', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::supportMsg [variable]
    cls.add_instance_attribute('supportMsg', 'std::string', is_const=False)
    return

def register_Ns3TypeIdTraceSourceInformation_methods(root_module, cls):
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::TraceSourceInformation() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::TraceSourceInformation(ns3::TypeId::TraceSourceInformation const & arg0) [constructor]
    cls.add_constructor([param('ns3::TypeId::TraceSourceInformation const &', 'arg0')])
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::accessor [variable]
    cls.add_instance_attribute('accessor', 'ns3::Ptr< ns3::TraceSourceAccessor const >', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::callback [variable]
    cls.add_instance_attribute('callback', 'std::string', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::help [variable]
    cls.add_instance_attribute('help', 'std::string', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::name [variable]
    cls.add_instance_attribute('name', 'std::string', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::supportLevel [variable]
    cls.add_instance_attribute('supportLevel', 'ns3::TypeId::SupportLevel', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::supportMsg [variable]
    cls.add_instance_attribute('supportMsg', 'std::string', is_const=False)
    return

def register_Ns3Vector2D_methods(root_module, cls):
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('<')
    cls.add_binary_numeric_operator('-', root_module['ns3::Vector2D'], root_module['ns3::Vector2D'], param('ns3::Vector2D const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::Vector2D'], root_module['ns3::Vector2D'], param('ns3::Vector2D const &', u'right'))
    ## vector.h (module 'core'): ns3::Vector2D::Vector2D(ns3::Vector2D const & arg0) [constructor]
    cls.add_constructor([param('ns3::Vector2D const &', 'arg0')])
    ## vector.h (module 'core'): ns3::Vector2D::Vector2D(double _x, double _y) [constructor]
    cls.add_constructor([param('double', '_x'), param('double', '_y')])
    ## vector.h (module 'core'): ns3::Vector2D::Vector2D() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): double ns3::Vector2D::GetLength() const [member function]
    cls.add_method('GetLength', 
                   'double', 
                   [], 
                   is_const=True)
    ## vector.h (module 'core'): ns3::Vector2D::x [variable]
    cls.add_instance_attribute('x', 'double', is_const=False)
    ## vector.h (module 'core'): ns3::Vector2D::y [variable]
    cls.add_instance_attribute('y', 'double', is_const=False)
    return

def register_Ns3Vector3D_methods(root_module, cls):
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('<')
    cls.add_binary_numeric_operator('-', root_module['ns3::Vector3D'], root_module['ns3::Vector3D'], param('ns3::Vector3D const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::Vector3D'], root_module['ns3::Vector3D'], param('ns3::Vector3D const &', u'right'))
    ## vector.h (module 'core'): ns3::Vector3D::Vector3D(ns3::Vector3D const & arg0) [constructor]
    cls.add_constructor([param('ns3::Vector3D const &', 'arg0')])
    ## vector.h (module 'core'): ns3::Vector3D::Vector3D(double _x, double _y, double _z) [constructor]
    cls.add_constructor([param('double', '_x'), param('double', '_y'), param('double', '_z')])
    ## vector.h (module 'core'): ns3::Vector3D::Vector3D() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): double ns3::Vector3D::GetLength() const [member function]
    cls.add_method('GetLength', 
                   'double', 
                   [], 
                   is_const=True)
    ## vector.h (module 'core'): ns3::Vector3D::x [variable]
    cls.add_instance_attribute('x', 'double', is_const=False)
    ## vector.h (module 'core'): ns3::Vector3D::y [variable]
    cls.add_instance_attribute('y', 'double', is_const=False)
    ## vector.h (module 'core'): ns3::Vector3D::z [variable]
    cls.add_instance_attribute('z', 'double', is_const=False)
    return

def register_Ns3Empty_methods(root_module, cls):
    ## empty.h (module 'core'): ns3::empty::empty() [constructor]
    cls.add_constructor([])
    ## empty.h (module 'core'): ns3::empty::empty(ns3::empty const & arg0) [constructor]
    cls.add_constructor([param('ns3::empty const &', 'arg0')])
    return

def register_Ns3Int64x64_t_methods(root_module, cls):
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', u'right'))
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('>=')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_inplace_numeric_operator('+=', param('ns3::int64x64_t const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ns3::int64x64_t const &', u'right'))
    cls.add_inplace_numeric_operator('*=', param('ns3::int64x64_t const &', u'right'))
    cls.add_inplace_numeric_operator('/=', param('ns3::int64x64_t const &', u'right'))
    cls.add_unary_numeric_operator('-')
    ## int64x64-128.h (module 'core'): ns3::int64x64_t::int64x64_t() [constructor]
    cls.add_constructor([])
    ## int64x64-128.h (module 'core'): ns3::int64x64_t::int64x64_t(double const value) [constructor]
    cls.add_constructor([param('double const', 'value')])
    ## int64x64-128.h (module 'core'): ns3::int64x64_t::int64x64_t(long double const value) [constructor]
    cls.add_constructor([param('long double const', 'value')])
    ## int64x64-128.h (module 'core'): ns3::int64x64_t::int64x64_t(int const v) [constructor]
    cls.add_constructor([param('int const', 'v')])
    ## int64x64-128.h (module 'core'): ns3::int64x64_t::int64x64_t(long int const v) [constructor]
    cls.add_constructor([param('long int const', 'v')])
    ## int64x64-128.h (module 'core'): ns3::int64x64_t::int64x64_t(long long int const v) [constructor]
    cls.add_constructor([param('long long int const', 'v')])
    ## int64x64-128.h (module 'core'): ns3::int64x64_t::int64x64_t(unsigned int const v) [constructor]
    cls.add_constructor([param('unsigned int const', 'v')])
    ## int64x64-128.h (module 'core'): ns3::int64x64_t::int64x64_t(long unsigned int const v) [constructor]
    cls.add_constructor([param('long unsigned int const', 'v')])
    ## int64x64-128.h (module 'core'): ns3::int64x64_t::int64x64_t(long long unsigned int const v) [constructor]
    cls.add_constructor([param('long long unsigned int const', 'v')])
    ## int64x64-128.h (module 'core'): ns3::int64x64_t::int64x64_t(int64_t const hi, uint64_t const lo) [constructor]
    cls.add_constructor([param('int64_t const', 'hi'), param('uint64_t const', 'lo')])
    ## int64x64-128.h (module 'core'): ns3::int64x64_t::int64x64_t(ns3::int64x64_t const & o) [constructor]
    cls.add_constructor([param('ns3::int64x64_t const &', 'o')])
    ## int64x64-128.h (module 'core'): double ns3::int64x64_t::GetDouble() const [member function]
    cls.add_method('GetDouble', 
                   'double', 
                   [], 
                   is_const=True)
    ## int64x64-128.h (module 'core'): int64_t ns3::int64x64_t::GetHigh() const [member function]
    cls.add_method('GetHigh', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## int64x64-128.h (module 'core'): uint64_t ns3::int64x64_t::GetLow() const [member function]
    cls.add_method('GetLow', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## int64x64-128.h (module 'core'): static ns3::int64x64_t ns3::int64x64_t::Invert(uint64_t const v) [member function]
    cls.add_method('Invert', 
                   'ns3::int64x64_t', 
                   [param('uint64_t const', 'v')], 
                   is_static=True)
    ## int64x64-128.h (module 'core'): void ns3::int64x64_t::MulByInvert(ns3::int64x64_t const & o) [member function]
    cls.add_method('MulByInvert', 
                   'void', 
                   [param('ns3::int64x64_t const &', 'o')])
    ## int64x64-128.h (module 'core'): ns3::int64x64_t::implementation [variable]
    cls.add_static_attribute('implementation', 'ns3::int64x64_t::impl_type const', is_const=True)
    return

def register_Ns3Chunk_methods(root_module, cls):
    ## chunk.h (module 'network'): ns3::Chunk::Chunk() [constructor]
    cls.add_constructor([])
    ## chunk.h (module 'network'): ns3::Chunk::Chunk(ns3::Chunk const & arg0) [constructor]
    cls.add_constructor([param('ns3::Chunk const &', 'arg0')])
    ## chunk.h (module 'network'): uint32_t ns3::Chunk::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_virtual=True)
    ## chunk.h (module 'network'): uint32_t ns3::Chunk::Deserialize(ns3::Buffer::Iterator start, ns3::Buffer::Iterator end) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('ns3::Buffer::Iterator', 'end')], 
                   is_virtual=True)
    ## chunk.h (module 'network'): static ns3::TypeId ns3::Chunk::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## chunk.h (module 'network'): void ns3::Chunk::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3Header_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## header.h (module 'network'): ns3::Header::Header() [constructor]
    cls.add_constructor([])
    ## header.h (module 'network'): ns3::Header::Header(ns3::Header const & arg0) [constructor]
    cls.add_constructor([param('ns3::Header const &', 'arg0')])
    ## header.h (module 'network'): uint32_t ns3::Header::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_virtual=True)
    ## header.h (module 'network'): uint32_t ns3::Header::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## header.h (module 'network'): static ns3::TypeId ns3::Header::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## header.h (module 'network'): void ns3::Header::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## header.h (module 'network'): void ns3::Header::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3LoRaHelper_methods(root_module, cls):
    ## lora-helper.h (module 'lora'): ns3::Ptr<ns3::LoRaNetwork> ns3::LoRaHelper::InstallBackend(ns3::Ptr<ns3::Node> node, ns3::NetDeviceContainer devices) [member function]
    cls.add_method('InstallBackend', 
                   'ns3::Ptr< ns3::LoRaNetwork >', 
                   [param('ns3::Ptr< ns3::Node >', 'node'), param('ns3::NetDeviceContainer', 'devices')])
    ## lora-helper.h (module 'lora'): ns3::ApplicationContainer ns3::LoRaHelper::GenerateTraffic(ns3::Ptr<ns3::RandomVariableStream> var, ns3::NodeContainer nodes, int packet_size, double start, double duration, double interval) [member function]
    cls.add_method('GenerateTraffic', 
                   'ns3::ApplicationContainer', 
                   [param('ns3::Ptr< ns3::RandomVariableStream >', 'var'), param('ns3::NodeContainer', 'nodes'), param('int', 'packet_size'), param('double', 'start'), param('double', 'duration'), param('double', 'interval')])
    ## lora-helper.h (module 'lora'): ns3::Ptr<ns3::Application> ns3::LoRaHelper::GenerateTraffic(ns3::Ptr<ns3::RandomVariableStream> var, ns3::Ptr<ns3::Node> node, int packet_size, double start, double duration, double interval) [member function]
    cls.add_method('GenerateTraffic', 
                   'ns3::Ptr< ns3::Application >', 
                   [param('ns3::Ptr< ns3::RandomVariableStream >', 'var'), param('ns3::Ptr< ns3::Node >', 'node'), param('int', 'packet_size'), param('double', 'start'), param('double', 'duration'), param('double', 'interval')])
    ## lora-helper.h (module 'lora'): ns3::ApplicationContainer ns3::LoRaHelper::FinishGateways(ns3::NodeContainer nodes, ns3::NetDeviceContainer devices, ns3::Address const & address) [member function]
    cls.add_method('FinishGateways', 
                   'ns3::ApplicationContainer', 
                   [param('ns3::NodeContainer', 'nodes'), param('ns3::NetDeviceContainer', 'devices'), param('ns3::Address const &', 'address')])
    ## lora-helper.h (module 'lora'): ns3::Ptr<ns3::Application> ns3::LoRaHelper::FinishGateway(ns3::Ptr<ns3::Node> node, ns3::Ptr<ns3::NetDevice> device, ns3::Address const & address) [member function]
    cls.add_method('FinishGateway', 
                   'ns3::Ptr< ns3::Application >', 
                   [param('ns3::Ptr< ns3::Node >', 'node'), param('ns3::Ptr< ns3::NetDevice >', 'device'), param('ns3::Address const &', 'address')])
    ## lora-helper.h (module 'lora'): ns3::LoRaHelper::LoRaHelper() [constructor]
    cls.add_constructor([])
    ## lora-helper.h (module 'lora'): ns3::Ptr<ns3::SpectrumChannel> ns3::LoRaHelper::GetChannel() [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::SpectrumChannel >', 
                   [])
    ## lora-helper.h (module 'lora'): void ns3::LoRaHelper::SetChannel(ns3::Ptr<ns3::SpectrumChannel> channel) [member function]
    cls.add_method('SetChannel', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumChannel >', 'channel')])
    ## lora-helper.h (module 'lora'): void ns3::LoRaHelper::SetChannel(std::string channelName) [member function]
    cls.add_method('SetChannel', 
                   'void', 
                   [param('std::string', 'channelName')])
    ## lora-helper.h (module 'lora'): void ns3::LoRaHelper::AddMobility(ns3::Ptr<ns3::LoRaPhy> phy, ns3::Ptr<ns3::MobilityModel> m) [member function]
    cls.add_method('AddMobility', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaPhy >', 'phy'), param('ns3::Ptr< ns3::MobilityModel >', 'm')])
    ## lora-helper.h (module 'lora'): ns3::NetDeviceContainer ns3::LoRaHelper::Install(ns3::NodeContainer c) [member function]
    cls.add_method('Install', 
                   'ns3::NetDeviceContainer', 
                   [param('ns3::NodeContainer', 'c')])
    ## lora-helper.h (module 'lora'): ns3::NetDeviceContainer ns3::LoRaHelper::InstallRs(ns3::NodeContainer c) [member function]
    cls.add_method('InstallRs', 
                   'ns3::NetDeviceContainer', 
                   [param('ns3::NodeContainer', 'c')])
    ## lora-helper.h (module 'lora'): ns3::NetDeviceContainer ns3::LoRaHelper::InstallGateways(ns3::NodeContainer c) [member function]
    cls.add_method('InstallGateways', 
                   'ns3::NetDeviceContainer', 
                   [param('ns3::NodeContainer', 'c')])
    ## lora-helper.h (module 'lora'): ns3::NetDeviceContainer ns3::LoRaHelper::InstallRsGateways(ns3::NodeContainer c) [member function]
    cls.add_method('InstallRsGateways', 
                   'ns3::NetDeviceContainer', 
                   [param('ns3::NodeContainer', 'c')])
    ## lora-helper.h (module 'lora'): void ns3::LoRaHelper::AddCallbacks(std::string traceSource, ns3::CallbackBase callback) [member function]
    cls.add_method('AddCallbacks', 
                   'void', 
                   [param('std::string', 'traceSource'), param('ns3::CallbackBase', 'callback')])
    ## lora-helper.h (module 'lora'): void ns3::LoRaHelper::AddCallbacksGateway(std::string traceSource, ns3::CallbackBase callback) [member function]
    cls.add_method('AddCallbacksGateway', 
                   'void', 
                   [param('std::string', 'traceSource'), param('ns3::CallbackBase', 'callback')])
    ## lora-helper.h (module 'lora'): void ns3::LoRaHelper::EnableLogComponents() [member function]
    cls.add_method('EnableLogComponents', 
                   'void', 
                   [])
    ## lora-helper.h (module 'lora'): int64_t ns3::LoRaHelper::AssignStreams(ns3::NetDeviceContainer c, int64_t stream) [member function]
    cls.add_method('AssignStreams', 
                   'int64_t', 
                   [param('ns3::NetDeviceContainer', 'c'), param('int64_t', 'stream')])
    ## lora-helper.h (module 'lora'): void ns3::LoRaHelper::InstallNetworkApplication(std::string type, std::string n0="", ns3::AttributeValue const & v0=ns3::EmptyAttributeValue(), std::string n1="", ns3::AttributeValue const & v1=ns3::EmptyAttributeValue(), std::string n2="", ns3::AttributeValue const & v2=ns3::EmptyAttributeValue(), std::string n3="", ns3::AttributeValue const & v3=ns3::EmptyAttributeValue(), std::string n4="", ns3::AttributeValue const & v4=ns3::EmptyAttributeValue(), std::string n5="", ns3::AttributeValue const & v5=ns3::EmptyAttributeValue(), std::string n6="", ns3::AttributeValue const & v6=ns3::EmptyAttributeValue(), std::string n7="", ns3::AttributeValue const & v7=ns3::EmptyAttributeValue()) [member function]
    cls.add_method('InstallNetworkApplication', 
                   'void', 
                   [param('std::string', 'type'), param('std::string', 'n0', default_value='""'), param('ns3::AttributeValue const &', 'v0', default_value='ns3::EmptyAttributeValue()'), param('std::string', 'n1', default_value='""'), param('ns3::AttributeValue const &', 'v1', default_value='ns3::EmptyAttributeValue()'), param('std::string', 'n2', default_value='""'), param('ns3::AttributeValue const &', 'v2', default_value='ns3::EmptyAttributeValue()'), param('std::string', 'n3', default_value='""'), param('ns3::AttributeValue const &', 'v3', default_value='ns3::EmptyAttributeValue()'), param('std::string', 'n4', default_value='""'), param('ns3::AttributeValue const &', 'v4', default_value='ns3::EmptyAttributeValue()'), param('std::string', 'n5', default_value='""'), param('ns3::AttributeValue const &', 'v5', default_value='ns3::EmptyAttributeValue()'), param('std::string', 'n6', default_value='""'), param('ns3::AttributeValue const &', 'v6', default_value='ns3::EmptyAttributeValue()'), param('std::string', 'n7', default_value='""'), param('ns3::AttributeValue const &', 'v7', default_value='ns3::EmptyAttributeValue()')])
    ## lora-helper.h (module 'lora'): void ns3::LoRaHelper::EnablePcapInternal(std::string prefix, ns3::Ptr<ns3::NetDevice> nd, bool promiscuous, bool explicitFilename) [member function]
    cls.add_method('EnablePcapInternal', 
                   'void', 
                   [param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'nd'), param('bool', 'promiscuous'), param('bool', 'explicitFilename')], 
                   visibility='private', is_virtual=True)
    ## lora-helper.h (module 'lora'): void ns3::LoRaHelper::EnableAsciiInternal(ns3::Ptr<ns3::OutputStreamWrapper> stream, std::string prefix, ns3::Ptr<ns3::NetDevice> nd, bool explicitFilename) [member function]
    cls.add_method('EnableAsciiInternal', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream'), param('std::string', 'prefix'), param('ns3::Ptr< ns3::NetDevice >', 'nd'), param('bool', 'explicitFilename')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3LoRaMacHeader_methods(root_module, cls):
    ## lora-mac-header.h (module 'lora'): ns3::LoRaMacHeader::LoRaMacHeader(ns3::LoRaMacHeader const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaMacHeader const &', 'arg0')])
    ## lora-mac-header.h (module 'lora'): ns3::LoRaMacHeader::LoRaMacHeader() [constructor]
    cls.add_constructor([])
    ## lora-mac-header.h (module 'lora'): ns3::LoRaMacHeader::LoRaMacHeader(ns3::LoRaMacHeader::LoRaMacType loraMacType, uint16_t seqNum) [constructor]
    cls.add_constructor([param('ns3::LoRaMacHeader::LoRaMacType', 'loraMacType'), param('uint16_t', 'seqNum')])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::AddChannel(uint8_t rssi, uint8_t sf) [member function]
    cls.add_method('AddChannel', 
                   'void', 
                   [param('uint8_t', 'rssi'), param('uint8_t', 'sf')])
    ## lora-mac-header.h (module 'lora'): uint32_t ns3::LoRaMacHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## lora-mac-header.h (module 'lora'): ns3::Mac32Address ns3::LoRaMacHeader::GetAddr() const [member function]
    cls.add_method('GetAddr', 
                   'ns3::Mac32Address', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): std::list<std::tuple<unsigned char, unsigned char>, std::allocator<std::tuple<unsigned char, unsigned char> > > ns3::LoRaMacHeader::GetChannels() [member function]
    cls.add_method('GetChannels', 
                   'std::list< std::tuple< unsigned char, unsigned char > >', 
                   [])
    ## lora-mac-header.h (module 'lora'): std::list<ns3::Ptr<ns3::LoRaMacCommand>, std::allocator<ns3::Ptr<ns3::LoRaMacCommand> > > ns3::LoRaMacHeader::GetCommandList() [member function]
    cls.add_method('GetCommandList', 
                   'std::list< ns3::Ptr< ns3::LoRaMacCommand > >', 
                   [])
    ## lora-mac-header.h (module 'lora'): uint8_t ns3::LoRaMacHeader::GetCommandsLength() const [member function]
    cls.add_method('GetCommandsLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): ns3::LoRaMacCommandDirection ns3::LoRaMacHeader::GetDirection() [member function]
    cls.add_method('GetDirection', 
                   'ns3::LoRaMacCommandDirection', 
                   [])
    ## lora-mac-header.h (module 'lora'): uint8_t ns3::LoRaMacHeader::GetFrameControl() const [member function]
    cls.add_method('GetFrameControl', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): uint8_t ns3::LoRaMacHeader::GetFrameVer() const [member function]
    cls.add_method('GetFrameVer', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): uint16_t ns3::LoRaMacHeader::GetFrmCounter() const [member function]
    cls.add_method('GetFrmCounter', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): uint8_t ns3::LoRaMacHeader::GetFrmCtrlRes() const [member function]
    cls.add_method('GetFrmCtrlRes', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): ns3::TypeId ns3::LoRaMacHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-mac-header.h (module 'lora'): uint8_t ns3::LoRaMacHeader::GetMacHeader() const [member function]
    cls.add_method('GetMacHeader', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): std::string ns3::LoRaMacHeader::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): uint8_t ns3::LoRaMacHeader::GetPort() const [member function]
    cls.add_method('GetPort', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): uint32_t ns3::LoRaMacHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-mac-header.h (module 'lora'): ns3::LoRaMacHeader::LoRaMacType ns3::LoRaMacHeader::GetType() const [member function]
    cls.add_method('GetType', 
                   'ns3::LoRaMacHeader::LoRaMacType', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): static ns3::TypeId ns3::LoRaMacHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-mac-header.h (module 'lora'): bool ns3::LoRaMacHeader::IsAck() const [member function]
    cls.add_method('IsAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): bool ns3::LoRaMacHeader::IsAcknowledgment() const [member function]
    cls.add_method('IsAcknowledgment', 
                   'bool', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): bool ns3::LoRaMacHeader::IsAdaptiveSupported() const [member function]
    cls.add_method('IsAdaptiveSupported', 
                   'bool', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): bool ns3::LoRaMacHeader::IsAdrAck() const [member function]
    cls.add_method('IsAdrAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): bool ns3::LoRaMacHeader::IsBeacon() const [member function]
    cls.add_method('IsBeacon', 
                   'bool', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): bool ns3::LoRaMacHeader::IsCommand() const [member function]
    cls.add_method('IsCommand', 
                   'bool', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): bool ns3::LoRaMacHeader::IsData() const [member function]
    cls.add_method('IsData', 
                   'bool', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): bool ns3::LoRaMacHeader::IsFrmPend() const [member function]
    cls.add_method('IsFrmPend', 
                   'bool', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): bool ns3::LoRaMacHeader::IsNoAck() const [member function]
    cls.add_method('IsNoAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): bool ns3::LoRaMacHeader::IsNoFrmPend() const [member function]
    cls.add_method('IsNoFrmPend', 
                   'bool', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::Merge(ns3::LoRaMacHeader header) [member function]
    cls.add_method('Merge', 
                   'void', 
                   [param('ns3::LoRaMacHeader', 'header')])
    ## lora-mac-header.h (module 'lora'): bool ns3::LoRaMacHeader::NeedsAck() const [member function]
    cls.add_method('NeedsAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::PrintFrameControl(std::ostream & os) const [member function]
    cls.add_method('PrintFrameControl', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetAck() [member function]
    cls.add_method('SetAck', 
                   'void', 
                   [])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetAdaptive() [member function]
    cls.add_method('SetAdaptive', 
                   'void', 
                   [])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetAddr(ns3::Mac32Address addr) [member function]
    cls.add_method('SetAddr', 
                   'void', 
                   [param('ns3::Mac32Address', 'addr')])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetAdrAck() [member function]
    cls.add_method('SetAdrAck', 
                   'void', 
                   [])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetDirection(ns3::LoRaMacCommandDirection direction) [member function]
    cls.add_method('SetDirection', 
                   'void', 
                   [param('ns3::LoRaMacCommandDirection', 'direction')])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetFrameControl(uint8_t frameControl) [member function]
    cls.add_method('SetFrameControl', 
                   'void', 
                   [param('uint8_t', 'frameControl')])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetFrameVer(uint8_t ver) [member function]
    cls.add_method('SetFrameVer', 
                   'void', 
                   [param('uint8_t', 'ver')])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetFrmCounter(uint16_t frmCntr) [member function]
    cls.add_method('SetFrmCounter', 
                   'void', 
                   [param('uint16_t', 'frmCntr')])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetFrmCtrlRes(uint8_t res) [member function]
    cls.add_method('SetFrmCtrlRes', 
                   'void', 
                   [param('uint8_t', 'res')])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetFrmPend() [member function]
    cls.add_method('SetFrmPend', 
                   'void', 
                   [])
    ## lora-mac-header.h (module 'lora'): bool ns3::LoRaMacHeader::SetMacCommand(ns3::Ptr<ns3::LoRaMacCommand> command) [member function]
    cls.add_method('SetMacCommand', 
                   'bool', 
                   [param('ns3::Ptr< ns3::LoRaMacCommand >', 'command')])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetMacHeader(uint8_t macHeader) [member function]
    cls.add_method('SetMacHeader', 
                   'void', 
                   [param('uint8_t', 'macHeader')])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetNoAck() [member function]
    cls.add_method('SetNoAck', 
                   'void', 
                   [])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetNoAdrAck() [member function]
    cls.add_method('SetNoAdrAck', 
                   'void', 
                   [])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetNoFrmPend() [member function]
    cls.add_method('SetNoFrmPend', 
                   'void', 
                   [])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetNotAdaptive() [member function]
    cls.add_method('SetNotAdaptive', 
                   'void', 
                   [])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetPort(uint8_t port) [member function]
    cls.add_method('SetPort', 
                   'void', 
                   [param('uint8_t', 'port')])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetSeqNum(uint8_t seqNum) [member function]
    cls.add_method('SetSeqNum', 
                   'void', 
                   [param('uint8_t', 'seqNum')])
    ## lora-mac-header.h (module 'lora'): void ns3::LoRaMacHeader::SetType(ns3::LoRaMacHeader::LoRaMacType loraMacType) [member function]
    cls.add_method('SetType', 
                   'void', 
                   [param('ns3::LoRaMacHeader::LoRaMacType', 'loraMacType')])
    return

def register_Ns3LoRaPhyHeader_methods(root_module, cls):
    ## lora-phy-header.h (module 'lora'): ns3::LoRaPhyHeader::LoRaPhyHeader(ns3::LoRaPhyHeader const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaPhyHeader const &', 'arg0')])
    ## lora-phy-header.h (module 'lora'): ns3::LoRaPhyHeader::LoRaPhyHeader() [constructor]
    cls.add_constructor([])
    ## lora-phy-header.h (module 'lora'): uint32_t ns3::LoRaPhyHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## lora-phy-header.h (module 'lora'): ns3::TypeId ns3::LoRaPhyHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-phy-header.h (module 'lora'): uint16_t ns3::LoRaPhyHeader::GetPreamble() const [member function]
    cls.add_method('GetPreamble', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## lora-phy-header.h (module 'lora'): uint32_t ns3::LoRaPhyHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-phy-header.h (module 'lora'): static ns3::TypeId ns3::LoRaPhyHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-phy-header.h (module 'lora'): bool ns3::LoRaPhyHeader::IsBeacon() [member function]
    cls.add_method('IsBeacon', 
                   'bool', 
                   [])
    ## lora-phy-header.h (module 'lora'): bool ns3::LoRaPhyHeader::IsData() [member function]
    cls.add_method('IsData', 
                   'bool', 
                   [])
    ## lora-phy-header.h (module 'lora'): void ns3::LoRaPhyHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## lora-phy-header.h (module 'lora'): void ns3::LoRaPhyHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## lora-phy-header.h (module 'lora'): void ns3::LoRaPhyHeader::SetBeacon() [member function]
    cls.add_method('SetBeacon', 
                   'void', 
                   [])
    ## lora-phy-header.h (module 'lora'): void ns3::LoRaPhyHeader::SetData() [member function]
    cls.add_method('SetData', 
                   'void', 
                   [])
    ## lora-phy-header.h (module 'lora'): void ns3::LoRaPhyHeader::SetPreamble(uint16_t preamble) [member function]
    cls.add_method('SetPreamble', 
                   'void', 
                   [param('uint16_t', 'preamble')])
    return

def register_Ns3Object_methods(root_module, cls):
    ## object.h (module 'core'): ns3::Object::Object() [constructor]
    cls.add_constructor([])
    ## object.h (module 'core'): void ns3::Object::AggregateObject(ns3::Ptr<ns3::Object> other) [member function]
    cls.add_method('AggregateObject', 
                   'void', 
                   [param('ns3::Ptr< ns3::Object >', 'other')])
    ## object.h (module 'core'): void ns3::Object::Dispose() [member function]
    cls.add_method('Dispose', 
                   'void', 
                   [])
    ## object.h (module 'core'): ns3::Object::AggregateIterator ns3::Object::GetAggregateIterator() const [member function]
    cls.add_method('GetAggregateIterator', 
                   'ns3::Object::AggregateIterator', 
                   [], 
                   is_const=True)
    ## object.h (module 'core'): ns3::TypeId ns3::Object::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## object.h (module 'core'): static ns3::TypeId ns3::Object::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## object.h (module 'core'): void ns3::Object::Initialize() [member function]
    cls.add_method('Initialize', 
                   'void', 
                   [])
    ## object.h (module 'core'): bool ns3::Object::IsInitialized() const [member function]
    cls.add_method('IsInitialized', 
                   'bool', 
                   [], 
                   is_const=True)
    ## object.h (module 'core'): ns3::Object::Object(ns3::Object const & o) [constructor]
    cls.add_constructor([param('ns3::Object const &', 'o')], 
                        visibility='protected')
    ## object.h (module 'core'): void ns3::Object::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## object.h (module 'core'): void ns3::Object::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## object.h (module 'core'): void ns3::Object::NotifyNewAggregate() [member function]
    cls.add_method('NotifyNewAggregate', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3ObjectAggregateIterator_methods(root_module, cls):
    ## object.h (module 'core'): ns3::Object::AggregateIterator::AggregateIterator(ns3::Object::AggregateIterator const & arg0) [constructor]
    cls.add_constructor([param('ns3::Object::AggregateIterator const &', 'arg0')])
    ## object.h (module 'core'): ns3::Object::AggregateIterator::AggregateIterator() [constructor]
    cls.add_constructor([])
    ## object.h (module 'core'): bool ns3::Object::AggregateIterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## object.h (module 'core'): ns3::Ptr<const ns3::Object> ns3::Object::AggregateIterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::Ptr< ns3::Object const >', 
                   [])
    return

def register_Ns3PcapFileWrapper_methods(root_module, cls):
    ## pcap-file-wrapper.h (module 'network'): static ns3::TypeId ns3::PcapFileWrapper::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## pcap-file-wrapper.h (module 'network'): ns3::PcapFileWrapper::PcapFileWrapper() [constructor]
    cls.add_constructor([])
    ## pcap-file-wrapper.h (module 'network'): bool ns3::PcapFileWrapper::Fail() const [member function]
    cls.add_method('Fail', 
                   'bool', 
                   [], 
                   is_const=True)
    ## pcap-file-wrapper.h (module 'network'): bool ns3::PcapFileWrapper::Eof() const [member function]
    cls.add_method('Eof', 
                   'bool', 
                   [], 
                   is_const=True)
    ## pcap-file-wrapper.h (module 'network'): void ns3::PcapFileWrapper::Clear() [member function]
    cls.add_method('Clear', 
                   'void', 
                   [])
    ## pcap-file-wrapper.h (module 'network'): void ns3::PcapFileWrapper::Open(std::string const & filename, std::ios_base::openmode mode) [member function]
    cls.add_method('Open', 
                   'void', 
                   [param('std::string const &', 'filename'), param('std::ios_base::openmode', 'mode')])
    ## pcap-file-wrapper.h (module 'network'): void ns3::PcapFileWrapper::Close() [member function]
    cls.add_method('Close', 
                   'void', 
                   [])
    ## pcap-file-wrapper.h (module 'network'): void ns3::PcapFileWrapper::Init(uint32_t dataLinkType, uint32_t snapLen=std::numeric_limits<unsigned int>::max(), int32_t tzCorrection=ns3::PcapFile::ZONE_DEFAULT) [member function]
    cls.add_method('Init', 
                   'void', 
                   [param('uint32_t', 'dataLinkType'), param('uint32_t', 'snapLen', default_value='std::numeric_limits<unsigned int>::max()'), param('int32_t', 'tzCorrection', default_value='ns3::PcapFile::ZONE_DEFAULT')])
    ## pcap-file-wrapper.h (module 'network'): void ns3::PcapFileWrapper::Write(ns3::Time t, ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('ns3::Time', 't'), param('ns3::Ptr< ns3::Packet const >', 'p')])
    ## pcap-file-wrapper.h (module 'network'): void ns3::PcapFileWrapper::Write(ns3::Time t, ns3::Header const & header, ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('ns3::Time', 't'), param('ns3::Header const &', 'header'), param('ns3::Ptr< ns3::Packet const >', 'p')])
    ## pcap-file-wrapper.h (module 'network'): void ns3::PcapFileWrapper::Write(ns3::Time t, uint8_t const * buffer, uint32_t length) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('ns3::Time', 't'), param('uint8_t const *', 'buffer'), param('uint32_t', 'length')])
    ## pcap-file-wrapper.h (module 'network'): ns3::Ptr<ns3::Packet> ns3::PcapFileWrapper::Read(ns3::Time & t) [member function]
    cls.add_method('Read', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::Time &', 't')])
    ## pcap-file-wrapper.h (module 'network'): uint32_t ns3::PcapFileWrapper::GetMagic() [member function]
    cls.add_method('GetMagic', 
                   'uint32_t', 
                   [])
    ## pcap-file-wrapper.h (module 'network'): uint16_t ns3::PcapFileWrapper::GetVersionMajor() [member function]
    cls.add_method('GetVersionMajor', 
                   'uint16_t', 
                   [])
    ## pcap-file-wrapper.h (module 'network'): uint16_t ns3::PcapFileWrapper::GetVersionMinor() [member function]
    cls.add_method('GetVersionMinor', 
                   'uint16_t', 
                   [])
    ## pcap-file-wrapper.h (module 'network'): int32_t ns3::PcapFileWrapper::GetTimeZoneOffset() [member function]
    cls.add_method('GetTimeZoneOffset', 
                   'int32_t', 
                   [])
    ## pcap-file-wrapper.h (module 'network'): uint32_t ns3::PcapFileWrapper::GetSigFigs() [member function]
    cls.add_method('GetSigFigs', 
                   'uint32_t', 
                   [])
    ## pcap-file-wrapper.h (module 'network'): uint32_t ns3::PcapFileWrapper::GetSnapLen() [member function]
    cls.add_method('GetSnapLen', 
                   'uint32_t', 
                   [])
    ## pcap-file-wrapper.h (module 'network'): uint32_t ns3::PcapFileWrapper::GetDataLinkType() [member function]
    cls.add_method('GetDataLinkType', 
                   'uint32_t', 
                   [])
    return

def register_Ns3PropagationDelayModel_methods(root_module, cls):
    ## propagation-delay-model.h (module 'propagation'): ns3::PropagationDelayModel::PropagationDelayModel() [constructor]
    cls.add_constructor([])
    ## propagation-delay-model.h (module 'propagation'): ns3::PropagationDelayModel::PropagationDelayModel(ns3::PropagationDelayModel const & arg0) [constructor]
    cls.add_constructor([param('ns3::PropagationDelayModel const &', 'arg0')])
    ## propagation-delay-model.h (module 'propagation'): int64_t ns3::PropagationDelayModel::AssignStreams(int64_t stream) [member function]
    cls.add_method('AssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')])
    ## propagation-delay-model.h (module 'propagation'): ns3::Time ns3::PropagationDelayModel::GetDelay(ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('GetDelay', 
                   'ns3::Time', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## propagation-delay-model.h (module 'propagation'): static ns3::TypeId ns3::PropagationDelayModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-delay-model.h (module 'propagation'): int64_t ns3::PropagationDelayModel::DoAssignStreams(int64_t stream) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    return

def register_Ns3PropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h (module 'propagation'): static ns3::TypeId ns3::PropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h (module 'propagation'): ns3::PropagationLossModel::PropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h (module 'propagation'): void ns3::PropagationLossModel::SetNext(ns3::Ptr<ns3::PropagationLossModel> next) [member function]
    cls.add_method('SetNext', 
                   'void', 
                   [param('ns3::Ptr< ns3::PropagationLossModel >', 'next')])
    ## propagation-loss-model.h (module 'propagation'): ns3::Ptr<ns3::PropagationLossModel> ns3::PropagationLossModel::GetNext() [member function]
    cls.add_method('GetNext', 
                   'ns3::Ptr< ns3::PropagationLossModel >', 
                   [])
    ## propagation-loss-model.h (module 'propagation'): double ns3::PropagationLossModel::CalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('CalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True)
    ## propagation-loss-model.h (module 'propagation'): int64_t ns3::PropagationLossModel::AssignStreams(int64_t stream) [member function]
    cls.add_method('AssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')])
    ## propagation-loss-model.h (module 'propagation'): double ns3::PropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    ## propagation-loss-model.h (module 'propagation'): int64_t ns3::PropagationLossModel::DoAssignStreams(int64_t stream) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    return

def register_Ns3RandomPropagationDelayModel_methods(root_module, cls):
    ## propagation-delay-model.h (module 'propagation'): ns3::RandomPropagationDelayModel::RandomPropagationDelayModel(ns3::RandomPropagationDelayModel const & arg0) [constructor]
    cls.add_constructor([param('ns3::RandomPropagationDelayModel const &', 'arg0')])
    ## propagation-delay-model.h (module 'propagation'): ns3::RandomPropagationDelayModel::RandomPropagationDelayModel() [constructor]
    cls.add_constructor([])
    ## propagation-delay-model.h (module 'propagation'): ns3::Time ns3::RandomPropagationDelayModel::GetDelay(ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('GetDelay', 
                   'ns3::Time', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, is_virtual=True)
    ## propagation-delay-model.h (module 'propagation'): static ns3::TypeId ns3::RandomPropagationDelayModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-delay-model.h (module 'propagation'): int64_t ns3::RandomPropagationDelayModel::DoAssignStreams(int64_t stream) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3RandomPropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h (module 'propagation'): static ns3::TypeId ns3::RandomPropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h (module 'propagation'): ns3::RandomPropagationLossModel::RandomPropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h (module 'propagation'): double ns3::RandomPropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    ## propagation-loss-model.h (module 'propagation'): int64_t ns3::RandomPropagationLossModel::DoAssignStreams(int64_t stream) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3RandomVariableStream_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::RandomVariableStream::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::RandomVariableStream::RandomVariableStream() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): void ns3::RandomVariableStream::SetStream(int64_t stream) [member function]
    cls.add_method('SetStream', 
                   'void', 
                   [param('int64_t', 'stream')])
    ## random-variable-stream.h (module 'core'): int64_t ns3::RandomVariableStream::GetStream() const [member function]
    cls.add_method('GetStream', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): void ns3::RandomVariableStream::SetAntithetic(bool isAntithetic) [member function]
    cls.add_method('SetAntithetic', 
                   'void', 
                   [param('bool', 'isAntithetic')])
    ## random-variable-stream.h (module 'core'): bool ns3::RandomVariableStream::IsAntithetic() const [member function]
    cls.add_method('IsAntithetic', 
                   'bool', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::RandomVariableStream::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::RandomVariableStream::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## random-variable-stream.h (module 'core'): ns3::RngStream * ns3::RandomVariableStream::Peek() const [member function]
    cls.add_method('Peek', 
                   'ns3::RngStream *', 
                   [], 
                   is_const=True, visibility='protected')
    return

def register_Ns3RangePropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h (module 'propagation'): static ns3::TypeId ns3::RangePropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h (module 'propagation'): ns3::RangePropagationLossModel::RangePropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h (module 'propagation'): double ns3::RangePropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    ## propagation-loss-model.h (module 'propagation'): int64_t ns3::RangePropagationLossModel::DoAssignStreams(int64_t stream) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3SequentialRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::SequentialRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::SequentialRandomVariable::SequentialRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::SequentialRandomVariable::GetMin() const [member function]
    cls.add_method('GetMin', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::SequentialRandomVariable::GetMax() const [member function]
    cls.add_method('GetMax', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): ns3::Ptr<ns3::RandomVariableStream> ns3::SequentialRandomVariable::GetIncrement() const [member function]
    cls.add_method('GetIncrement', 
                   'ns3::Ptr< ns3::RandomVariableStream >', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::SequentialRandomVariable::GetConsecutive() const [member function]
    cls.add_method('GetConsecutive', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::SequentialRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::SequentialRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3SimpleRefCount__Ns3AttributeAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeAccessor__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >::SimpleRefCount(ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter< ns3::AttributeAccessor > > const &', 'o')])
    return

def register_Ns3SimpleRefCount__Ns3AttributeChecker_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeChecker__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >::SimpleRefCount(ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter< ns3::AttributeChecker > > const &', 'o')])
    return

def register_Ns3SimpleRefCount__Ns3AttributeValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeValue__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >::SimpleRefCount(ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter< ns3::AttributeValue > > const &', 'o')])
    return

def register_Ns3SimpleRefCount__Ns3CallbackImplBase_Ns3Empty_Ns3DefaultDeleter__lt__ns3CallbackImplBase__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >::SimpleRefCount(ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter< ns3::CallbackImplBase > > const &', 'o')])
    return

def register_Ns3SimpleRefCount__Ns3EventImpl_Ns3Empty_Ns3DefaultDeleter__lt__ns3EventImpl__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >::SimpleRefCount(ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::EventImpl, ns3::empty, ns3::DefaultDeleter< ns3::EventImpl > > const &', 'o')])
    return

def register_Ns3SimpleRefCount__Ns3HashImplementation_Ns3Empty_Ns3DefaultDeleter__lt__ns3HashImplementation__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >::SimpleRefCount(ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter< ns3::Hash::Implementation > > const &', 'o')])
    return

def register_Ns3SimpleRefCount__Ns3NixVector_Ns3Empty_Ns3DefaultDeleter__lt__ns3NixVector__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >::SimpleRefCount(ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::NixVector, ns3::empty, ns3::DefaultDeleter< ns3::NixVector > > const &', 'o')])
    return

def register_Ns3SimpleRefCount__Ns3OutputStreamWrapper_Ns3Empty_Ns3DefaultDeleter__lt__ns3OutputStreamWrapper__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> >::SimpleRefCount(ns3::SimpleRefCount<ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter< ns3::OutputStreamWrapper > > const &', 'o')])
    return

def register_Ns3SimpleRefCount__Ns3Packet_Ns3Empty_Ns3DefaultDeleter__lt__ns3Packet__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >::SimpleRefCount(ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::Packet, ns3::empty, ns3::DefaultDeleter< ns3::Packet > > const &', 'o')])
    return

def register_Ns3SimpleRefCount__Ns3QueueItem_Ns3Empty_Ns3DefaultDeleter__lt__ns3QueueItem__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::QueueItem, ns3::empty, ns3::DefaultDeleter<ns3::QueueItem> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::QueueItem, ns3::empty, ns3::DefaultDeleter<ns3::QueueItem> >::SimpleRefCount(ns3::SimpleRefCount<ns3::QueueItem, ns3::empty, ns3::DefaultDeleter<ns3::QueueItem> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::QueueItem, ns3::empty, ns3::DefaultDeleter< ns3::QueueItem > > const &', 'o')])
    return

def register_Ns3SimpleRefCount__Ns3SpectrumModel_Ns3Empty_Ns3DefaultDeleter__lt__ns3SpectrumModel__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumModel> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumModel> >::SimpleRefCount(ns3::SimpleRefCount<ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumModel> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter< ns3::SpectrumModel > > const &', 'o')])
    return

def register_Ns3SimpleRefCount__Ns3SpectrumSignalParameters_Ns3Empty_Ns3DefaultDeleter__lt__ns3SpectrumSignalParameters__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumSignalParameters> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumSignalParameters> >::SimpleRefCount(ns3::SimpleRefCount<ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumSignalParameters> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter< ns3::SpectrumSignalParameters > > const &', 'o')])
    return

def register_Ns3SimpleRefCount__Ns3SpectrumValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3SpectrumValue__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumValue> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumValue> >::SimpleRefCount(ns3::SimpleRefCount<ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumValue> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter< ns3::SpectrumValue > > const &', 'o')])
    return

def register_Ns3SimpleRefCount__Ns3TraceSourceAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3TraceSourceAccessor__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >::SimpleRefCount(ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> > const & o) [constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter< ns3::TraceSourceAccessor > > const &', 'o')])
    return

def register_Ns3SpectrumModel_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    ## spectrum-model.h (module 'spectrum'): ns3::SpectrumModel::SpectrumModel(ns3::SpectrumModel const & arg0) [constructor]
    cls.add_constructor([param('ns3::SpectrumModel const &', 'arg0')])
    ## spectrum-model.h (module 'spectrum'): ns3::SpectrumModel::SpectrumModel(std::vector<double, std::allocator<double> > centerFreqs) [constructor]
    cls.add_constructor([param('std::vector< double >', 'centerFreqs')])
    ## spectrum-model.h (module 'spectrum'): ns3::SpectrumModel::SpectrumModel(ns3::Bands bands) [constructor]
    cls.add_constructor([param('ns3::Bands', 'bands')])
    ## spectrum-model.h (module 'spectrum'): std::vector<ns3::BandInfo, std::allocator<ns3::BandInfo> >::const_iterator ns3::SpectrumModel::Begin() const [member function]
    cls.add_method('Begin', 
                   'std::vector< ns3::BandInfo > const_iterator', 
                   [], 
                   is_const=True)
    ## spectrum-model.h (module 'spectrum'): std::vector<ns3::BandInfo, std::allocator<ns3::BandInfo> >::const_iterator ns3::SpectrumModel::End() const [member function]
    cls.add_method('End', 
                   'std::vector< ns3::BandInfo > const_iterator', 
                   [], 
                   is_const=True)
    ## spectrum-model.h (module 'spectrum'): size_t ns3::SpectrumModel::GetNumBands() const [member function]
    cls.add_method('GetNumBands', 
                   'size_t', 
                   [], 
                   is_const=True)
    ## spectrum-model.h (module 'spectrum'): ns3::SpectrumModelUid_t ns3::SpectrumModel::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'ns3::SpectrumModelUid_t', 
                   [], 
                   is_const=True)
    ## spectrum-model.h (module 'spectrum'): bool ns3::SpectrumModel::IsOrthogonal(ns3::SpectrumModel const & other) const [member function]
    cls.add_method('IsOrthogonal', 
                   'bool', 
                   [param('ns3::SpectrumModel const &', 'other')], 
                   is_const=True)
    return

def register_Ns3SpectrumPhy_methods(root_module, cls):
    ## spectrum-phy.h (module 'spectrum'): ns3::SpectrumPhy::SpectrumPhy() [constructor]
    cls.add_constructor([])
    ## spectrum-phy.h (module 'spectrum'): static ns3::TypeId ns3::SpectrumPhy::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## spectrum-phy.h (module 'spectrum'): void ns3::SpectrumPhy::SetDevice(ns3::Ptr<ns3::NetDevice> d) [member function]
    cls.add_method('SetDevice', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'd')], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): ns3::Ptr<ns3::NetDevice> ns3::SpectrumPhy::GetDevice() const [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): void ns3::SpectrumPhy::SetMobility(ns3::Ptr<ns3::MobilityModel> m) [member function]
    cls.add_method('SetMobility', 
                   'void', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'm')], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): ns3::Ptr<ns3::MobilityModel> ns3::SpectrumPhy::GetMobility() [member function]
    cls.add_method('GetMobility', 
                   'ns3::Ptr< ns3::MobilityModel >', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): void ns3::SpectrumPhy::SetChannel(ns3::Ptr<ns3::SpectrumChannel> c) [member function]
    cls.add_method('SetChannel', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumChannel >', 'c')], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): ns3::Ptr<const ns3::SpectrumModel> ns3::SpectrumPhy::GetRxSpectrumModel() const [member function]
    cls.add_method('GetRxSpectrumModel', 
                   'ns3::Ptr< ns3::SpectrumModel const >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): ns3::Ptr<ns3::AntennaModel> ns3::SpectrumPhy::GetRxAntenna() [member function]
    cls.add_method('GetRxAntenna', 
                   'ns3::Ptr< ns3::AntennaModel >', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): void ns3::SpectrumPhy::StartRx(ns3::Ptr<ns3::SpectrumSignalParameters> params) [member function]
    cls.add_method('StartRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumSignalParameters >', 'params')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3SpectrumPropagationLossModel_methods(root_module, cls):
    ## spectrum-propagation-loss-model.h (module 'spectrum'): ns3::SpectrumPropagationLossModel::SpectrumPropagationLossModel(ns3::SpectrumPropagationLossModel const & arg0) [constructor]
    cls.add_constructor([param('ns3::SpectrumPropagationLossModel const &', 'arg0')])
    ## spectrum-propagation-loss-model.h (module 'spectrum'): ns3::SpectrumPropagationLossModel::SpectrumPropagationLossModel() [constructor]
    cls.add_constructor([])
    ## spectrum-propagation-loss-model.h (module 'spectrum'): ns3::Ptr<ns3::SpectrumValue> ns3::SpectrumPropagationLossModel::CalcRxPowerSpectralDensity(ns3::Ptr<const ns3::SpectrumValue> txPsd, ns3::Ptr<const ns3::MobilityModel> a, ns3::Ptr<const ns3::MobilityModel> b) const [member function]
    cls.add_method('CalcRxPowerSpectralDensity', 
                   'ns3::Ptr< ns3::SpectrumValue >', 
                   [param('ns3::Ptr< ns3::SpectrumValue const >', 'txPsd'), param('ns3::Ptr< ns3::MobilityModel const >', 'a'), param('ns3::Ptr< ns3::MobilityModel const >', 'b')], 
                   is_const=True)
    ## spectrum-propagation-loss-model.h (module 'spectrum'): static ns3::TypeId ns3::SpectrumPropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## spectrum-propagation-loss-model.h (module 'spectrum'): void ns3::SpectrumPropagationLossModel::SetNext(ns3::Ptr<ns3::SpectrumPropagationLossModel> next) [member function]
    cls.add_method('SetNext', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumPropagationLossModel >', 'next')])
    ## spectrum-propagation-loss-model.h (module 'spectrum'): void ns3::SpectrumPropagationLossModel::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## spectrum-propagation-loss-model.h (module 'spectrum'): ns3::Ptr<ns3::SpectrumValue> ns3::SpectrumPropagationLossModel::DoCalcRxPowerSpectralDensity(ns3::Ptr<const ns3::SpectrumValue> txPsd, ns3::Ptr<const ns3::MobilityModel> a, ns3::Ptr<const ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPowerSpectralDensity', 
                   'ns3::Ptr< ns3::SpectrumValue >', 
                   [param('ns3::Ptr< ns3::SpectrumValue const >', 'txPsd'), param('ns3::Ptr< ns3::MobilityModel const >', 'a'), param('ns3::Ptr< ns3::MobilityModel const >', 'b')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3SpectrumSignalParameters_methods(root_module, cls):
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters::SpectrumSignalParameters() [constructor]
    cls.add_constructor([])
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters::SpectrumSignalParameters(ns3::SpectrumSignalParameters const & p) [constructor]
    cls.add_constructor([param('ns3::SpectrumSignalParameters const &', 'p')])
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::Ptr<ns3::SpectrumSignalParameters> ns3::SpectrumSignalParameters::Copy() [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::SpectrumSignalParameters >', 
                   [], 
                   is_virtual=True)
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters::psd [variable]
    cls.add_instance_attribute('psd', 'ns3::Ptr< ns3::SpectrumValue >', is_const=False)
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters::duration [variable]
    cls.add_instance_attribute('duration', 'ns3::Time', is_const=False)
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters::txPhy [variable]
    cls.add_instance_attribute('txPhy', 'ns3::Ptr< ns3::SpectrumPhy >', is_const=False)
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters::txAntenna [variable]
    cls.add_instance_attribute('txAntenna', 'ns3::Ptr< ns3::AntennaModel >', is_const=False)
    return

def register_Ns3SpectrumValue_methods(root_module, cls):
    cls.add_output_stream_operator()
    cls.add_unary_numeric_operator('-')
    cls.add_binary_numeric_operator('/', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('double', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('ns3::SpectrumValue const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('double', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('ns3::SpectrumValue const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('double', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('ns3::SpectrumValue const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('double', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('ns3::SpectrumValue const &', u'right'))
    cls.add_inplace_numeric_operator('*=', param('ns3::SpectrumValue const &', u'right'))
    cls.add_inplace_numeric_operator('*=', param('double', u'right'))
    cls.add_inplace_numeric_operator('+=', param('ns3::SpectrumValue const &', u'right'))
    cls.add_inplace_numeric_operator('+=', param('double', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ns3::SpectrumValue const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('double', u'right'))
    cls.add_inplace_numeric_operator('/=', param('ns3::SpectrumValue const &', u'right'))
    cls.add_inplace_numeric_operator('/=', param('double', u'right'))
    ## spectrum-value.h (module 'spectrum'): ns3::SpectrumValue::SpectrumValue(ns3::SpectrumValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::SpectrumValue const &', 'arg0')])
    ## spectrum-value.h (module 'spectrum'): ns3::SpectrumValue::SpectrumValue(ns3::Ptr<const ns3::SpectrumModel> sm) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::SpectrumModel const >', 'sm')])
    ## spectrum-value.h (module 'spectrum'): ns3::SpectrumValue::SpectrumValue() [constructor]
    cls.add_constructor([])
    ## spectrum-value.h (module 'spectrum'): std::vector<ns3::BandInfo, std::allocator<ns3::BandInfo> >::const_iterator ns3::SpectrumValue::ConstBandsBegin() const [member function]
    cls.add_method('ConstBandsBegin', 
                   'std::vector< ns3::BandInfo > const_iterator', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): std::vector<ns3::BandInfo, std::allocator<ns3::BandInfo> >::const_iterator ns3::SpectrumValue::ConstBandsEnd() const [member function]
    cls.add_method('ConstBandsEnd', 
                   'std::vector< ns3::BandInfo > const_iterator', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): std::vector<double, std::allocator<double> >::const_iterator ns3::SpectrumValue::ConstValuesBegin() const [member function]
    cls.add_method('ConstValuesBegin', 
                   'std::vector< double > const_iterator', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): std::vector<double, std::allocator<double> >::const_iterator ns3::SpectrumValue::ConstValuesEnd() const [member function]
    cls.add_method('ConstValuesEnd', 
                   'std::vector< double > const_iterator', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): ns3::Ptr<ns3::SpectrumValue> ns3::SpectrumValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::SpectrumValue >', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): ns3::Ptr<const ns3::SpectrumModel> ns3::SpectrumValue::GetSpectrumModel() const [member function]
    cls.add_method('GetSpectrumModel', 
                   'ns3::Ptr< ns3::SpectrumModel const >', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): ns3::SpectrumModelUid_t ns3::SpectrumValue::GetSpectrumModelUid() const [member function]
    cls.add_method('GetSpectrumModelUid', 
                   'ns3::SpectrumModelUid_t', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): std::vector<double, std::allocator<double> >::iterator ns3::SpectrumValue::ValuesBegin() [member function]
    cls.add_method('ValuesBegin', 
                   'std::vector< double > iterator', 
                   [])
    ## spectrum-value.h (module 'spectrum'): std::vector<double, std::allocator<double> >::iterator ns3::SpectrumValue::ValuesEnd() [member function]
    cls.add_method('ValuesEnd', 
                   'std::vector< double > iterator', 
                   [])
    return

def register_Ns3ThreeLogDistancePropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h (module 'propagation'): static ns3::TypeId ns3::ThreeLogDistancePropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h (module 'propagation'): ns3::ThreeLogDistancePropagationLossModel::ThreeLogDistancePropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h (module 'propagation'): double ns3::ThreeLogDistancePropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    ## propagation-loss-model.h (module 'propagation'): int64_t ns3::ThreeLogDistancePropagationLossModel::DoAssignStreams(int64_t stream) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3Time_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('>=')
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_binary_numeric_operator('+', root_module['ns3::Time'], root_module['ns3::Time'], param('ns3::Time const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::Time'], root_module['ns3::Time'], param('ns3::Time const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::Time'], root_module['ns3::Time'], param('int64_t const &', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::Time'], root_module['ns3::Time'], param('int64_t const &', u'right'))
    cls.add_inplace_numeric_operator('+=', param('ns3::Time const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ns3::Time const &', u'right'))
    cls.add_output_stream_operator()
    ## nstime.h (module 'core'): ns3::Time::Time() [constructor]
    cls.add_constructor([])
    ## nstime.h (module 'core'): ns3::Time::Time(ns3::Time const & o) [constructor]
    cls.add_constructor([param('ns3::Time const &', 'o')])
    ## nstime.h (module 'core'): ns3::Time::Time(double v) [constructor]
    cls.add_constructor([param('double', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(int v) [constructor]
    cls.add_constructor([param('int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(long int v) [constructor]
    cls.add_constructor([param('long int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(long long int v) [constructor]
    cls.add_constructor([param('long long int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(unsigned int v) [constructor]
    cls.add_constructor([param('unsigned int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(long unsigned int v) [constructor]
    cls.add_constructor([param('long unsigned int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(long long unsigned int v) [constructor]
    cls.add_constructor([param('long long unsigned int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(ns3::int64x64_t const & v) [constructor]
    cls.add_constructor([param('ns3::int64x64_t const &', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(std::string const & s) [constructor]
    cls.add_constructor([param('std::string const &', 's')])
    ## nstime.h (module 'core'): ns3::TimeWithUnit ns3::Time::As(ns3::Time::Unit const unit) const [member function]
    cls.add_method('As', 
                   'ns3::TimeWithUnit', 
                   [param('ns3::Time::Unit const', 'unit')], 
                   is_const=True)
    ## nstime.h (module 'core'): int ns3::Time::Compare(ns3::Time const & o) const [member function]
    cls.add_method('Compare', 
                   'int', 
                   [param('ns3::Time const &', 'o')], 
                   is_const=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::From(ns3::int64x64_t const & value) [member function]
    cls.add_method('From', 
                   'ns3::Time', 
                   [param('ns3::int64x64_t const &', 'value')], 
                   is_static=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::From(ns3::int64x64_t const & value, ns3::Time::Unit unit) [member function]
    cls.add_method('From', 
                   'ns3::Time', 
                   [param('ns3::int64x64_t const &', 'value'), param('ns3::Time::Unit', 'unit')], 
                   is_static=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::FromDouble(double value, ns3::Time::Unit unit) [member function]
    cls.add_method('FromDouble', 
                   'ns3::Time', 
                   [param('double', 'value'), param('ns3::Time::Unit', 'unit')], 
                   is_static=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::FromInteger(uint64_t value, ns3::Time::Unit unit) [member function]
    cls.add_method('FromInteger', 
                   'ns3::Time', 
                   [param('uint64_t', 'value'), param('ns3::Time::Unit', 'unit')], 
                   is_static=True)
    ## nstime.h (module 'core'): double ns3::Time::GetDays() const [member function]
    cls.add_method('GetDays', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::GetDouble() const [member function]
    cls.add_method('GetDouble', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetFemtoSeconds() const [member function]
    cls.add_method('GetFemtoSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::GetHours() const [member function]
    cls.add_method('GetHours', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetInteger() const [member function]
    cls.add_method('GetInteger', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetMicroSeconds() const [member function]
    cls.add_method('GetMicroSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetMilliSeconds() const [member function]
    cls.add_method('GetMilliSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::GetMinutes() const [member function]
    cls.add_method('GetMinutes', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetNanoSeconds() const [member function]
    cls.add_method('GetNanoSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetPicoSeconds() const [member function]
    cls.add_method('GetPicoSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): static ns3::Time::Unit ns3::Time::GetResolution() [member function]
    cls.add_method('GetResolution', 
                   'ns3::Time::Unit', 
                   [], 
                   is_static=True)
    ## nstime.h (module 'core'): double ns3::Time::GetSeconds() const [member function]
    cls.add_method('GetSeconds', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetTimeStep() const [member function]
    cls.add_method('GetTimeStep', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::GetYears() const [member function]
    cls.add_method('GetYears', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsNegative() const [member function]
    cls.add_method('IsNegative', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsPositive() const [member function]
    cls.add_method('IsPositive', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsStrictlyNegative() const [member function]
    cls.add_method('IsStrictlyNegative', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsStrictlyPositive() const [member function]
    cls.add_method('IsStrictlyPositive', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsZero() const [member function]
    cls.add_method('IsZero', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::Max() [member function]
    cls.add_method('Max', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::Min() [member function]
    cls.add_method('Min', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    ## nstime.h (module 'core'): static void ns3::Time::SetResolution(ns3::Time::Unit resolution) [member function]
    cls.add_method('SetResolution', 
                   'void', 
                   [param('ns3::Time::Unit', 'resolution')], 
                   is_static=True)
    ## nstime.h (module 'core'): static bool ns3::Time::StaticInit() [member function]
    cls.add_method('StaticInit', 
                   'bool', 
                   [], 
                   is_static=True)
    ## nstime.h (module 'core'): ns3::int64x64_t ns3::Time::To(ns3::Time::Unit unit) const [member function]
    cls.add_method('To', 
                   'ns3::int64x64_t', 
                   [param('ns3::Time::Unit', 'unit')], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::ToDouble(ns3::Time::Unit unit) const [member function]
    cls.add_method('ToDouble', 
                   'double', 
                   [param('ns3::Time::Unit', 'unit')], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::ToInteger(ns3::Time::Unit unit) const [member function]
    cls.add_method('ToInteger', 
                   'int64_t', 
                   [param('ns3::Time::Unit', 'unit')], 
                   is_const=True)
    return

def register_Ns3TraceSourceAccessor_methods(root_module, cls):
    ## trace-source-accessor.h (module 'core'): ns3::TraceSourceAccessor::TraceSourceAccessor(ns3::TraceSourceAccessor const & arg0) [constructor]
    cls.add_constructor([param('ns3::TraceSourceAccessor const &', 'arg0')])
    ## trace-source-accessor.h (module 'core'): ns3::TraceSourceAccessor::TraceSourceAccessor() [constructor]
    cls.add_constructor([])
    ## trace-source-accessor.h (module 'core'): bool ns3::TraceSourceAccessor::Connect(ns3::ObjectBase * obj, std::string context, ns3::CallbackBase const & cb) const [member function]
    cls.add_method('Connect', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trace-source-accessor.h (module 'core'): bool ns3::TraceSourceAccessor::ConnectWithoutContext(ns3::ObjectBase * obj, ns3::CallbackBase const & cb) const [member function]
    cls.add_method('ConnectWithoutContext', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trace-source-accessor.h (module 'core'): bool ns3::TraceSourceAccessor::Disconnect(ns3::ObjectBase * obj, std::string context, ns3::CallbackBase const & cb) const [member function]
    cls.add_method('Disconnect', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trace-source-accessor.h (module 'core'): bool ns3::TraceSourceAccessor::DisconnectWithoutContext(ns3::ObjectBase * obj, ns3::CallbackBase const & cb) const [member function]
    cls.add_method('DisconnectWithoutContext', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3Trailer_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## trailer.h (module 'network'): ns3::Trailer::Trailer() [constructor]
    cls.add_constructor([])
    ## trailer.h (module 'network'): ns3::Trailer::Trailer(ns3::Trailer const & arg0) [constructor]
    cls.add_constructor([param('ns3::Trailer const &', 'arg0')])
    ## trailer.h (module 'network'): uint32_t ns3::Trailer::Deserialize(ns3::Buffer::Iterator end) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'end')], 
                   is_pure_virtual=True, is_virtual=True)
    ## trailer.h (module 'network'): uint32_t ns3::Trailer::Deserialize(ns3::Buffer::Iterator start, ns3::Buffer::Iterator end) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('ns3::Buffer::Iterator', 'end')], 
                   is_virtual=True)
    ## trailer.h (module 'network'): uint32_t ns3::Trailer::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trailer.h (module 'network'): static ns3::TypeId ns3::Trailer::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## trailer.h (module 'network'): void ns3::Trailer::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trailer.h (module 'network'): void ns3::Trailer::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3TriangularRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::TriangularRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::TriangularRandomVariable::TriangularRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetMean() const [member function]
    cls.add_method('GetMean', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetMin() const [member function]
    cls.add_method('GetMin', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetMax() const [member function]
    cls.add_method('GetMax', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetValue(double mean, double min, double max) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mean'), param('double', 'min'), param('double', 'max')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::TriangularRandomVariable::GetInteger(uint32_t mean, uint32_t min, uint32_t max) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mean'), param('uint32_t', 'min'), param('uint32_t', 'max')])
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::TriangularRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3TwoRayGroundPropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h (module 'propagation'): static ns3::TypeId ns3::TwoRayGroundPropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h (module 'propagation'): ns3::TwoRayGroundPropagationLossModel::TwoRayGroundPropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h (module 'propagation'): void ns3::TwoRayGroundPropagationLossModel::SetFrequency(double frequency) [member function]
    cls.add_method('SetFrequency', 
                   'void', 
                   [param('double', 'frequency')])
    ## propagation-loss-model.h (module 'propagation'): void ns3::TwoRayGroundPropagationLossModel::SetSystemLoss(double systemLoss) [member function]
    cls.add_method('SetSystemLoss', 
                   'void', 
                   [param('double', 'systemLoss')])
    ## propagation-loss-model.h (module 'propagation'): void ns3::TwoRayGroundPropagationLossModel::SetMinDistance(double minDistance) [member function]
    cls.add_method('SetMinDistance', 
                   'void', 
                   [param('double', 'minDistance')])
    ## propagation-loss-model.h (module 'propagation'): double ns3::TwoRayGroundPropagationLossModel::GetMinDistance() const [member function]
    cls.add_method('GetMinDistance', 
                   'double', 
                   [], 
                   is_const=True)
    ## propagation-loss-model.h (module 'propagation'): double ns3::TwoRayGroundPropagationLossModel::GetFrequency() const [member function]
    cls.add_method('GetFrequency', 
                   'double', 
                   [], 
                   is_const=True)
    ## propagation-loss-model.h (module 'propagation'): double ns3::TwoRayGroundPropagationLossModel::GetSystemLoss() const [member function]
    cls.add_method('GetSystemLoss', 
                   'double', 
                   [], 
                   is_const=True)
    ## propagation-loss-model.h (module 'propagation'): void ns3::TwoRayGroundPropagationLossModel::SetHeightAboveZ(double heightAboveZ) [member function]
    cls.add_method('SetHeightAboveZ', 
                   'void', 
                   [param('double', 'heightAboveZ')])
    ## propagation-loss-model.h (module 'propagation'): double ns3::TwoRayGroundPropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    ## propagation-loss-model.h (module 'propagation'): int64_t ns3::TwoRayGroundPropagationLossModel::DoAssignStreams(int64_t stream) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3UniformRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::UniformRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::UniformRandomVariable::UniformRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::UniformRandomVariable::GetMin() const [member function]
    cls.add_method('GetMin', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::UniformRandomVariable::GetMax() const [member function]
    cls.add_method('GetMax', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::UniformRandomVariable::GetValue(double min, double max) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'min'), param('double', 'max')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::UniformRandomVariable::GetInteger(uint32_t min, uint32_t max) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'min'), param('uint32_t', 'max')])
    ## random-variable-stream.h (module 'core'): double ns3::UniformRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::UniformRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3WeibullRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::WeibullRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::WeibullRandomVariable::WeibullRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetScale() const [member function]
    cls.add_method('GetScale', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetShape() const [member function]
    cls.add_method('GetShape', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetBound() const [member function]
    cls.add_method('GetBound', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetValue(double scale, double shape, double bound) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'scale'), param('double', 'shape'), param('double', 'bound')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::WeibullRandomVariable::GetInteger(uint32_t scale, uint32_t shape, uint32_t bound) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'scale'), param('uint32_t', 'shape'), param('uint32_t', 'bound')])
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::WeibullRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3ZetaRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ZetaRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ZetaRandomVariable::ZetaRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::ZetaRandomVariable::GetAlpha() const [member function]
    cls.add_method('GetAlpha', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ZetaRandomVariable::GetValue(double alpha) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'alpha')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZetaRandomVariable::GetInteger(uint32_t alpha) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'alpha')])
    ## random-variable-stream.h (module 'core'): double ns3::ZetaRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZetaRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3ZipfRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ZipfRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ZipfRandomVariable::ZipfRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZipfRandomVariable::GetN() const [member function]
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ZipfRandomVariable::GetAlpha() const [member function]
    cls.add_method('GetAlpha', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ZipfRandomVariable::GetValue(uint32_t n, double alpha) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('uint32_t', 'n'), param('double', 'alpha')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZipfRandomVariable::GetInteger(uint32_t n, uint32_t alpha) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'n'), param('uint32_t', 'alpha')])
    ## random-variable-stream.h (module 'core'): double ns3::ZipfRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZipfRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3Application_methods(root_module, cls):
    ## application.h (module 'network'): ns3::Application::Application(ns3::Application const & arg0) [constructor]
    cls.add_constructor([param('ns3::Application const &', 'arg0')])
    ## application.h (module 'network'): ns3::Application::Application() [constructor]
    cls.add_constructor([])
    ## application.h (module 'network'): ns3::Ptr<ns3::Node> ns3::Application::GetNode() const [member function]
    cls.add_method('GetNode', 
                   'ns3::Ptr< ns3::Node >', 
                   [], 
                   is_const=True)
    ## application.h (module 'network'): static ns3::TypeId ns3::Application::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## application.h (module 'network'): void ns3::Application::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')])
    ## application.h (module 'network'): void ns3::Application::SetStartTime(ns3::Time start) [member function]
    cls.add_method('SetStartTime', 
                   'void', 
                   [param('ns3::Time', 'start')])
    ## application.h (module 'network'): void ns3::Application::SetStopTime(ns3::Time stop) [member function]
    cls.add_method('SetStopTime', 
                   'void', 
                   [param('ns3::Time', 'stop')])
    ## application.h (module 'network'): void ns3::Application::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## application.h (module 'network'): void ns3::Application::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## application.h (module 'network'): void ns3::Application::StartApplication() [member function]
    cls.add_method('StartApplication', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## application.h (module 'network'): void ns3::Application::StopApplication() [member function]
    cls.add_method('StopApplication', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3AttributeAccessor_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::AttributeAccessor::AttributeAccessor(ns3::AttributeAccessor const & arg0) [constructor]
    cls.add_constructor([param('ns3::AttributeAccessor const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::AttributeAccessor::AttributeAccessor() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): bool ns3::AttributeAccessor::Get(ns3::ObjectBase const * object, ns3::AttributeValue & attribute) const [member function]
    cls.add_method('Get', 
                   'bool', 
                   [param('ns3::ObjectBase const *', 'object'), param('ns3::AttributeValue &', 'attribute')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeAccessor::HasGetter() const [member function]
    cls.add_method('HasGetter', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeAccessor::HasSetter() const [member function]
    cls.add_method('HasSetter', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeAccessor::Set(ns3::ObjectBase * object, ns3::AttributeValue const & value) const [member function]
    cls.add_method('Set', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'object', transfer_ownership=False), param('ns3::AttributeValue const &', 'value')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3AttributeChecker_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::AttributeChecker::AttributeChecker(ns3::AttributeChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::AttributeChecker const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::AttributeChecker::AttributeChecker() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): bool ns3::AttributeChecker::Check(ns3::AttributeValue const & value) const [member function]
    cls.add_method('Check', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'value')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeChecker::Copy(ns3::AttributeValue const & source, ns3::AttributeValue & destination) const [member function]
    cls.add_method('Copy', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'source'), param('ns3::AttributeValue &', 'destination')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::AttributeChecker::Create() const [member function]
    cls.add_method('Create', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::AttributeChecker::CreateValidValue(ns3::AttributeValue const & value) const [member function]
    cls.add_method('CreateValidValue', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [param('ns3::AttributeValue const &', 'value')], 
                   is_const=True)
    ## attribute.h (module 'core'): std::string ns3::AttributeChecker::GetUnderlyingTypeInformation() const [member function]
    cls.add_method('GetUnderlyingTypeInformation', 
                   'std::string', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): std::string ns3::AttributeChecker::GetValueTypeName() const [member function]
    cls.add_method('GetValueTypeName', 
                   'std::string', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeChecker::HasUnderlyingTypeInformation() const [member function]
    cls.add_method('HasUnderlyingTypeInformation', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3AttributeValue_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::AttributeValue::AttributeValue(ns3::AttributeValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::AttributeValue const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::AttributeValue::AttributeValue() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::AttributeValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_pure_virtual=True, is_virtual=True)
    ## attribute.h (module 'core'): std::string ns3::AttributeValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3BooleanChecker_methods(root_module, cls):
    ## boolean.h (module 'core'): ns3::BooleanChecker::BooleanChecker() [constructor]
    cls.add_constructor([])
    ## boolean.h (module 'core'): ns3::BooleanChecker::BooleanChecker(ns3::BooleanChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::BooleanChecker const &', 'arg0')])
    return

def register_Ns3BooleanValue_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## boolean.h (module 'core'): ns3::BooleanValue::BooleanValue(ns3::BooleanValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::BooleanValue const &', 'arg0')])
    ## boolean.h (module 'core'): ns3::BooleanValue::BooleanValue() [constructor]
    cls.add_constructor([])
    ## boolean.h (module 'core'): ns3::BooleanValue::BooleanValue(bool value) [constructor]
    cls.add_constructor([param('bool', 'value')])
    ## boolean.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::BooleanValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## boolean.h (module 'core'): bool ns3::BooleanValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## boolean.h (module 'core'): bool ns3::BooleanValue::Get() const [member function]
    cls.add_method('Get', 
                   'bool', 
                   [], 
                   is_const=True)
    ## boolean.h (module 'core'): std::string ns3::BooleanValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## boolean.h (module 'core'): void ns3::BooleanValue::Set(bool value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('bool', 'value')])
    return

def register_Ns3CallbackChecker_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackChecker::CallbackChecker() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackChecker::CallbackChecker(ns3::CallbackChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackChecker const &', 'arg0')])
    return

def register_Ns3CallbackImplBase_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImplBase::CallbackImplBase() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImplBase::CallbackImplBase(ns3::CallbackImplBase const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImplBase const &', 'arg0')])
    ## callback.h (module 'core'): std::string ns3::CallbackImplBase::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## callback.h (module 'core'): bool ns3::CallbackImplBase::IsEqual(ns3::Ptr<const ns3::CallbackImplBase> other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ptr< ns3::CallbackImplBase const >', 'other')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::Demangle(std::string const & mangled) [member function]
    cls.add_method('Demangle', 
                   'std::string', 
                   [param('std::string const &', 'mangled')], 
                   is_static=True, visibility='protected')
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'ns3::ObjectBase*'])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'void'])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'ns3::LoRaPhy::State'])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'double'])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'ns3::Ptr<ns3::NetDevice> '])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'ns3::Ptr<ns3::Packet const> '])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'unsigned short'])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'ns3::Address const&'])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'ns3::NetDevice::PacketType'])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'bool'])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'ns3::Ptr<ns3::Packet> '])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'ns3::Ptr<ns3::MobilityModel const> '])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'ns3::Ptr<ns3::SpectrumPhy const> '])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'ns3::Ptr<ns3::SpectrumSignalParameters> '])
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::GetCppTypeid() [member function]
    cls.add_method('GetCppTypeid', 
                   'std::string', 
                   [], 
                   is_static=True, visibility='protected', template_parameters=[u'std::__cxx11::basic_string<char', u' std::char_traits<char>', u' std::allocator<char> > '])
    return

def register_Ns3CallbackValue_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackValue::CallbackValue(ns3::CallbackValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackValue const &', 'arg0')])
    ## callback.h (module 'core'): ns3::CallbackValue::CallbackValue() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackValue::CallbackValue(ns3::CallbackBase const & base) [constructor]
    cls.add_constructor([param('ns3::CallbackBase const &', 'base')])
    ## callback.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::CallbackValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): bool ns3::CallbackValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## callback.h (module 'core'): std::string ns3::CallbackValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackValue::Set(ns3::CallbackBase base) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::CallbackBase', 'base')])
    return

def register_Ns3Channel_methods(root_module, cls):
    ## channel.h (module 'network'): ns3::Channel::Channel(ns3::Channel const & arg0) [constructor]
    cls.add_constructor([param('ns3::Channel const &', 'arg0')])
    ## channel.h (module 'network'): ns3::Channel::Channel() [constructor]
    cls.add_constructor([])
    ## channel.h (module 'network'): ns3::Ptr<ns3::NetDevice> ns3::Channel::GetDevice(std::size_t i) const [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('std::size_t', 'i')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## channel.h (module 'network'): uint32_t ns3::Channel::GetId() const [member function]
    cls.add_method('GetId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## channel.h (module 'network'): std::size_t ns3::Channel::GetNDevices() const [member function]
    cls.add_method('GetNDevices', 
                   'std::size_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## channel.h (module 'network'): static ns3::TypeId ns3::Channel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3ConstantRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ConstantRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ConstantRandomVariable::ConstantRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::ConstantRandomVariable::GetConstant() const [member function]
    cls.add_method('GetConstant', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ConstantRandomVariable::GetValue(double constant) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'constant')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ConstantRandomVariable::GetInteger(uint32_t constant) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'constant')])
    ## random-variable-stream.h (module 'core'): double ns3::ConstantRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ConstantRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3ConstantSpeedPropagationDelayModel_methods(root_module, cls):
    ## propagation-delay-model.h (module 'propagation'): ns3::ConstantSpeedPropagationDelayModel::ConstantSpeedPropagationDelayModel(ns3::ConstantSpeedPropagationDelayModel const & arg0) [constructor]
    cls.add_constructor([param('ns3::ConstantSpeedPropagationDelayModel const &', 'arg0')])
    ## propagation-delay-model.h (module 'propagation'): ns3::ConstantSpeedPropagationDelayModel::ConstantSpeedPropagationDelayModel() [constructor]
    cls.add_constructor([])
    ## propagation-delay-model.h (module 'propagation'): ns3::Time ns3::ConstantSpeedPropagationDelayModel::GetDelay(ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('GetDelay', 
                   'ns3::Time', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, is_virtual=True)
    ## propagation-delay-model.h (module 'propagation'): double ns3::ConstantSpeedPropagationDelayModel::GetSpeed() const [member function]
    cls.add_method('GetSpeed', 
                   'double', 
                   [], 
                   is_const=True)
    ## propagation-delay-model.h (module 'propagation'): static ns3::TypeId ns3::ConstantSpeedPropagationDelayModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-delay-model.h (module 'propagation'): void ns3::ConstantSpeedPropagationDelayModel::SetSpeed(double speed) [member function]
    cls.add_method('SetSpeed', 
                   'void', 
                   [param('double', 'speed')])
    ## propagation-delay-model.h (module 'propagation'): int64_t ns3::ConstantSpeedPropagationDelayModel::DoAssignStreams(int64_t stream) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3DeterministicRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::DeterministicRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::DeterministicRandomVariable::DeterministicRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): void ns3::DeterministicRandomVariable::SetValueArray(double * values, std::size_t length) [member function]
    cls.add_method('SetValueArray', 
                   'void', 
                   [param('double *', 'values'), param('std::size_t', 'length')])
    ## random-variable-stream.h (module 'core'): double ns3::DeterministicRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::DeterministicRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3DeviceEnergyModel_methods(root_module, cls):
    ## device-energy-model.h (module 'energy'): ns3::DeviceEnergyModel::DeviceEnergyModel(ns3::DeviceEnergyModel const & arg0) [constructor]
    cls.add_constructor([param('ns3::DeviceEnergyModel const &', 'arg0')])
    ## device-energy-model.h (module 'energy'): ns3::DeviceEnergyModel::DeviceEnergyModel() [constructor]
    cls.add_constructor([])
    ## device-energy-model.h (module 'energy'): void ns3::DeviceEnergyModel::ChangeState(int newState) [member function]
    cls.add_method('ChangeState', 
                   'void', 
                   [param('int', 'newState')], 
                   is_pure_virtual=True, is_virtual=True)
    ## device-energy-model.h (module 'energy'): double ns3::DeviceEnergyModel::GetCurrentA() const [member function]
    cls.add_method('GetCurrentA', 
                   'double', 
                   [], 
                   is_const=True)
    ## device-energy-model.h (module 'energy'): double ns3::DeviceEnergyModel::GetTotalEnergyConsumption() const [member function]
    cls.add_method('GetTotalEnergyConsumption', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## device-energy-model.h (module 'energy'): static ns3::TypeId ns3::DeviceEnergyModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## device-energy-model.h (module 'energy'): void ns3::DeviceEnergyModel::HandleEnergyChanged() [member function]
    cls.add_method('HandleEnergyChanged', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## device-energy-model.h (module 'energy'): void ns3::DeviceEnergyModel::HandleEnergyDepletion() [member function]
    cls.add_method('HandleEnergyDepletion', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## device-energy-model.h (module 'energy'): void ns3::DeviceEnergyModel::HandleEnergyRecharged() [member function]
    cls.add_method('HandleEnergyRecharged', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## device-energy-model.h (module 'energy'): void ns3::DeviceEnergyModel::SetEnergySource(ns3::Ptr<ns3::EnergySource> source) [member function]
    cls.add_method('SetEnergySource', 
                   'void', 
                   [param('ns3::Ptr< ns3::EnergySource >', 'source')], 
                   is_pure_virtual=True, is_virtual=True)
    ## device-energy-model.h (module 'energy'): double ns3::DeviceEnergyModel::DoGetCurrentA() const [member function]
    cls.add_method('DoGetCurrentA', 
                   'double', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3DoubleValue_methods(root_module, cls):
    ## double.h (module 'core'): ns3::DoubleValue::DoubleValue() [constructor]
    cls.add_constructor([])
    ## double.h (module 'core'): ns3::DoubleValue::DoubleValue(double const & value) [constructor]
    cls.add_constructor([param('double const &', 'value')])
    ## double.h (module 'core'): ns3::DoubleValue::DoubleValue(ns3::DoubleValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::DoubleValue const &', 'arg0')])
    ## double.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::DoubleValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## double.h (module 'core'): bool ns3::DoubleValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## double.h (module 'core'): double ns3::DoubleValue::Get() const [member function]
    cls.add_method('Get', 
                   'double', 
                   [], 
                   is_const=True)
    ## double.h (module 'core'): std::string ns3::DoubleValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## double.h (module 'core'): void ns3::DoubleValue::Set(double const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('double const &', 'value')])
    return

def register_Ns3EmpiricalRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): ns3::EmpiricalRandomVariable::EmpiricalRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): void ns3::EmpiricalRandomVariable::CDF(double v, double c) [member function]
    cls.add_method('CDF', 
                   'void', 
                   [param('double', 'v'), param('double', 'c')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::EmpiricalRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::EmpiricalRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): double ns3::EmpiricalRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): double ns3::EmpiricalRandomVariable::Interpolate(double c1, double c2, double v1, double v2, double r) [member function]
    cls.add_method('Interpolate', 
                   'double', 
                   [param('double', 'c1'), param('double', 'c2'), param('double', 'v1'), param('double', 'v2'), param('double', 'r')], 
                   visibility='private', is_virtual=True)
    ## random-variable-stream.h (module 'core'): void ns3::EmpiricalRandomVariable::Validate() [member function]
    cls.add_method('Validate', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3EmptyAttributeAccessor_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::EmptyAttributeAccessor::EmptyAttributeAccessor(ns3::EmptyAttributeAccessor const & arg0) [constructor]
    cls.add_constructor([param('ns3::EmptyAttributeAccessor const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::EmptyAttributeAccessor::EmptyAttributeAccessor() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): bool ns3::EmptyAttributeAccessor::Get(ns3::ObjectBase const * object, ns3::AttributeValue & attribute) const [member function]
    cls.add_method('Get', 
                   'bool', 
                   [param('ns3::ObjectBase const *', 'object'), param('ns3::AttributeValue &', 'attribute')], 
                   is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::EmptyAttributeAccessor::HasGetter() const [member function]
    cls.add_method('HasGetter', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::EmptyAttributeAccessor::HasSetter() const [member function]
    cls.add_method('HasSetter', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::EmptyAttributeAccessor::Set(ns3::ObjectBase * object, ns3::AttributeValue const & value) const [member function]
    cls.add_method('Set', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'object'), param('ns3::AttributeValue const &', 'value')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3EmptyAttributeChecker_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::EmptyAttributeChecker::EmptyAttributeChecker(ns3::EmptyAttributeChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::EmptyAttributeChecker const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::EmptyAttributeChecker::EmptyAttributeChecker() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): bool ns3::EmptyAttributeChecker::Check(ns3::AttributeValue const & value) const [member function]
    cls.add_method('Check', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'value')], 
                   is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::EmptyAttributeChecker::Copy(ns3::AttributeValue const & source, ns3::AttributeValue & destination) const [member function]
    cls.add_method('Copy', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'source'), param('ns3::AttributeValue &', 'destination')], 
                   is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::EmptyAttributeChecker::Create() const [member function]
    cls.add_method('Create', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): std::string ns3::EmptyAttributeChecker::GetUnderlyingTypeInformation() const [member function]
    cls.add_method('GetUnderlyingTypeInformation', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): std::string ns3::EmptyAttributeChecker::GetValueTypeName() const [member function]
    cls.add_method('GetValueTypeName', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::EmptyAttributeChecker::HasUnderlyingTypeInformation() const [member function]
    cls.add_method('HasUnderlyingTypeInformation', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3EmptyAttributeValue_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::EmptyAttributeValue::EmptyAttributeValue(ns3::EmptyAttributeValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::EmptyAttributeValue const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::EmptyAttributeValue::EmptyAttributeValue() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::EmptyAttributeValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::EmptyAttributeValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   visibility='private', is_virtual=True)
    ## attribute.h (module 'core'): std::string ns3::EmptyAttributeValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3EnergyHarvester_methods(root_module, cls):
    ## energy-harvester.h (module 'energy'): ns3::EnergyHarvester::EnergyHarvester(ns3::EnergyHarvester const & arg0) [constructor]
    cls.add_constructor([param('ns3::EnergyHarvester const &', 'arg0')])
    ## energy-harvester.h (module 'energy'): ns3::EnergyHarvester::EnergyHarvester() [constructor]
    cls.add_constructor([])
    ## energy-harvester.h (module 'energy'): ns3::Ptr<ns3::EnergySource> ns3::EnergyHarvester::GetEnergySource() const [member function]
    cls.add_method('GetEnergySource', 
                   'ns3::Ptr< ns3::EnergySource >', 
                   [], 
                   is_const=True)
    ## energy-harvester.h (module 'energy'): ns3::Ptr<ns3::Node> ns3::EnergyHarvester::GetNode() const [member function]
    cls.add_method('GetNode', 
                   'ns3::Ptr< ns3::Node >', 
                   [], 
                   is_const=True)
    ## energy-harvester.h (module 'energy'): double ns3::EnergyHarvester::GetPower() const [member function]
    cls.add_method('GetPower', 
                   'double', 
                   [], 
                   is_const=True)
    ## energy-harvester.h (module 'energy'): static ns3::TypeId ns3::EnergyHarvester::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## energy-harvester.h (module 'energy'): void ns3::EnergyHarvester::SetEnergySource(ns3::Ptr<ns3::EnergySource> source) [member function]
    cls.add_method('SetEnergySource', 
                   'void', 
                   [param('ns3::Ptr< ns3::EnergySource >', 'source')])
    ## energy-harvester.h (module 'energy'): void ns3::EnergyHarvester::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')])
    ## energy-harvester.h (module 'energy'): void ns3::EnergyHarvester::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## energy-harvester.h (module 'energy'): double ns3::EnergyHarvester::DoGetPower() const [member function]
    cls.add_method('DoGetPower', 
                   'double', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3EnergySource_methods(root_module, cls):
    ## energy-source.h (module 'energy'): ns3::EnergySource::EnergySource(ns3::EnergySource const & arg0) [constructor]
    cls.add_constructor([param('ns3::EnergySource const &', 'arg0')])
    ## energy-source.h (module 'energy'): ns3::EnergySource::EnergySource() [constructor]
    cls.add_constructor([])
    ## energy-source.h (module 'energy'): void ns3::EnergySource::AppendDeviceEnergyModel(ns3::Ptr<ns3::DeviceEnergyModel> deviceEnergyModelPtr) [member function]
    cls.add_method('AppendDeviceEnergyModel', 
                   'void', 
                   [param('ns3::Ptr< ns3::DeviceEnergyModel >', 'deviceEnergyModelPtr')])
    ## energy-source.h (module 'energy'): void ns3::EnergySource::ConnectEnergyHarvester(ns3::Ptr<ns3::EnergyHarvester> energyHarvesterPtr) [member function]
    cls.add_method('ConnectEnergyHarvester', 
                   'void', 
                   [param('ns3::Ptr< ns3::EnergyHarvester >', 'energyHarvesterPtr')])
    ## energy-source.h (module 'energy'): void ns3::EnergySource::DisposeDeviceModels() [member function]
    cls.add_method('DisposeDeviceModels', 
                   'void', 
                   [])
    ## energy-source.h (module 'energy'): ns3::DeviceEnergyModelContainer ns3::EnergySource::FindDeviceEnergyModels(ns3::TypeId tid) [member function]
    cls.add_method('FindDeviceEnergyModels', 
                   'ns3::DeviceEnergyModelContainer', 
                   [param('ns3::TypeId', 'tid')])
    ## energy-source.h (module 'energy'): ns3::DeviceEnergyModelContainer ns3::EnergySource::FindDeviceEnergyModels(std::string name) [member function]
    cls.add_method('FindDeviceEnergyModels', 
                   'ns3::DeviceEnergyModelContainer', 
                   [param('std::string', 'name')])
    ## energy-source.h (module 'energy'): double ns3::EnergySource::GetEnergyFraction() [member function]
    cls.add_method('GetEnergyFraction', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## energy-source.h (module 'energy'): double ns3::EnergySource::GetInitialEnergy() const [member function]
    cls.add_method('GetInitialEnergy', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## energy-source.h (module 'energy'): ns3::Ptr<ns3::Node> ns3::EnergySource::GetNode() const [member function]
    cls.add_method('GetNode', 
                   'ns3::Ptr< ns3::Node >', 
                   [], 
                   is_const=True)
    ## energy-source.h (module 'energy'): double ns3::EnergySource::GetRemainingEnergy() [member function]
    cls.add_method('GetRemainingEnergy', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## energy-source.h (module 'energy'): double ns3::EnergySource::GetSupplyVoltage() const [member function]
    cls.add_method('GetSupplyVoltage', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## energy-source.h (module 'energy'): static ns3::TypeId ns3::EnergySource::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## energy-source.h (module 'energy'): void ns3::EnergySource::InitializeDeviceModels() [member function]
    cls.add_method('InitializeDeviceModels', 
                   'void', 
                   [])
    ## energy-source.h (module 'energy'): void ns3::EnergySource::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')])
    ## energy-source.h (module 'energy'): void ns3::EnergySource::UpdateEnergySource() [member function]
    cls.add_method('UpdateEnergySource', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## energy-source.h (module 'energy'): void ns3::EnergySource::BreakDeviceEnergyModelRefCycle() [member function]
    cls.add_method('BreakDeviceEnergyModelRefCycle', 
                   'void', 
                   [], 
                   visibility='protected')
    ## energy-source.h (module 'energy'): double ns3::EnergySource::CalculateTotalCurrent() [member function]
    cls.add_method('CalculateTotalCurrent', 
                   'double', 
                   [], 
                   visibility='protected')
    ## energy-source.h (module 'energy'): void ns3::EnergySource::NotifyEnergyChanged() [member function]
    cls.add_method('NotifyEnergyChanged', 
                   'void', 
                   [], 
                   visibility='protected')
    ## energy-source.h (module 'energy'): void ns3::EnergySource::NotifyEnergyDrained() [member function]
    cls.add_method('NotifyEnergyDrained', 
                   'void', 
                   [], 
                   visibility='protected')
    ## energy-source.h (module 'energy'): void ns3::EnergySource::NotifyEnergyRecharged() [member function]
    cls.add_method('NotifyEnergyRecharged', 
                   'void', 
                   [], 
                   visibility='protected')
    ## energy-source.h (module 'energy'): void ns3::EnergySource::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3EnergySourceContainer_methods(root_module, cls):
    ## energy-source-container.h (module 'energy'): ns3::EnergySourceContainer::EnergySourceContainer(ns3::EnergySourceContainer const & arg0) [constructor]
    cls.add_constructor([param('ns3::EnergySourceContainer const &', 'arg0')])
    ## energy-source-container.h (module 'energy'): ns3::EnergySourceContainer::EnergySourceContainer() [constructor]
    cls.add_constructor([])
    ## energy-source-container.h (module 'energy'): ns3::EnergySourceContainer::EnergySourceContainer(ns3::Ptr<ns3::EnergySource> source) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::EnergySource >', 'source')])
    ## energy-source-container.h (module 'energy'): ns3::EnergySourceContainer::EnergySourceContainer(std::string sourceName) [constructor]
    cls.add_constructor([param('std::string', 'sourceName')])
    ## energy-source-container.h (module 'energy'): ns3::EnergySourceContainer::EnergySourceContainer(ns3::EnergySourceContainer const & a, ns3::EnergySourceContainer const & b) [constructor]
    cls.add_constructor([param('ns3::EnergySourceContainer const &', 'a'), param('ns3::EnergySourceContainer const &', 'b')])
    ## energy-source-container.h (module 'energy'): void ns3::EnergySourceContainer::Add(ns3::EnergySourceContainer container) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::EnergySourceContainer', 'container')])
    ## energy-source-container.h (module 'energy'): void ns3::EnergySourceContainer::Add(ns3::Ptr<ns3::EnergySource> source) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Ptr< ns3::EnergySource >', 'source')])
    ## energy-source-container.h (module 'energy'): void ns3::EnergySourceContainer::Add(std::string sourceName) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'sourceName')])
    ## energy-source-container.h (module 'energy'): ns3::EnergySourceContainer::Iterator ns3::EnergySourceContainer::Begin() const [member function]
    cls.add_method('Begin', 
                   'ns3::EnergySourceContainer::Iterator', 
                   [], 
                   is_const=True)
    ## energy-source-container.h (module 'energy'): ns3::EnergySourceContainer::Iterator ns3::EnergySourceContainer::End() const [member function]
    cls.add_method('End', 
                   'ns3::EnergySourceContainer::Iterator', 
                   [], 
                   is_const=True)
    ## energy-source-container.h (module 'energy'): ns3::Ptr<ns3::EnergySource> ns3::EnergySourceContainer::Get(uint32_t i) const [member function]
    cls.add_method('Get', 
                   'ns3::Ptr< ns3::EnergySource >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## energy-source-container.h (module 'energy'): uint32_t ns3::EnergySourceContainer::GetN() const [member function]
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## energy-source-container.h (module 'energy'): static ns3::TypeId ns3::EnergySourceContainer::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## energy-source-container.h (module 'energy'): void ns3::EnergySourceContainer::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## energy-source-container.h (module 'energy'): void ns3::EnergySourceContainer::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3EnumChecker_methods(root_module, cls):
    ## enum.h (module 'core'): ns3::EnumChecker::EnumChecker(ns3::EnumChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::EnumChecker const &', 'arg0')])
    ## enum.h (module 'core'): ns3::EnumChecker::EnumChecker() [constructor]
    cls.add_constructor([])
    ## enum.h (module 'core'): void ns3::EnumChecker::Add(int value, std::string name) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('int', 'value'), param('std::string', 'name')])
    ## enum.h (module 'core'): void ns3::EnumChecker::AddDefault(int value, std::string name) [member function]
    cls.add_method('AddDefault', 
                   'void', 
                   [param('int', 'value'), param('std::string', 'name')])
    ## enum.h (module 'core'): bool ns3::EnumChecker::Check(ns3::AttributeValue const & value) const [member function]
    cls.add_method('Check', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'value')], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): bool ns3::EnumChecker::Copy(ns3::AttributeValue const & src, ns3::AttributeValue & dst) const [member function]
    cls.add_method('Copy', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'src'), param('ns3::AttributeValue &', 'dst')], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::EnumChecker::Create() const [member function]
    cls.add_method('Create', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): std::string ns3::EnumChecker::GetUnderlyingTypeInformation() const [member function]
    cls.add_method('GetUnderlyingTypeInformation', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): std::string ns3::EnumChecker::GetValueTypeName() const [member function]
    cls.add_method('GetValueTypeName', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): bool ns3::EnumChecker::HasUnderlyingTypeInformation() const [member function]
    cls.add_method('HasUnderlyingTypeInformation', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3EnumValue_methods(root_module, cls):
    ## enum.h (module 'core'): ns3::EnumValue::EnumValue(ns3::EnumValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::EnumValue const &', 'arg0')])
    ## enum.h (module 'core'): ns3::EnumValue::EnumValue() [constructor]
    cls.add_constructor([])
    ## enum.h (module 'core'): ns3::EnumValue::EnumValue(int value) [constructor]
    cls.add_constructor([param('int', 'value')])
    ## enum.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::EnumValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): bool ns3::EnumValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## enum.h (module 'core'): int ns3::EnumValue::Get() const [member function]
    cls.add_method('Get', 
                   'int', 
                   [], 
                   is_const=True)
    ## enum.h (module 'core'): std::string ns3::EnumValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): void ns3::EnumValue::Set(int value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('int', 'value')])
    return

def register_Ns3ErlangRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ErlangRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ErlangRandomVariable::ErlangRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ErlangRandomVariable::GetK() const [member function]
    cls.add_method('GetK', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ErlangRandomVariable::GetLambda() const [member function]
    cls.add_method('GetLambda', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ErlangRandomVariable::GetValue(uint32_t k, double lambda) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('uint32_t', 'k'), param('double', 'lambda')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ErlangRandomVariable::GetInteger(uint32_t k, uint32_t lambda) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'k'), param('uint32_t', 'lambda')])
    ## random-variable-stream.h (module 'core'): double ns3::ErlangRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ErlangRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3EventImpl_methods(root_module, cls):
    ## event-impl.h (module 'core'): ns3::EventImpl::EventImpl(ns3::EventImpl const & arg0) [constructor]
    cls.add_constructor([param('ns3::EventImpl const &', 'arg0')])
    ## event-impl.h (module 'core'): ns3::EventImpl::EventImpl() [constructor]
    cls.add_constructor([])
    ## event-impl.h (module 'core'): void ns3::EventImpl::Cancel() [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [])
    ## event-impl.h (module 'core'): void ns3::EventImpl::Invoke() [member function]
    cls.add_method('Invoke', 
                   'void', 
                   [])
    ## event-impl.h (module 'core'): bool ns3::EventImpl::IsCancelled() [member function]
    cls.add_method('IsCancelled', 
                   'bool', 
                   [])
    ## event-impl.h (module 'core'): void ns3::EventImpl::Notify() [member function]
    cls.add_method('Notify', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    return

def register_Ns3ExponentialRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ExponentialRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ExponentialRandomVariable::ExponentialRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::ExponentialRandomVariable::GetMean() const [member function]
    cls.add_method('GetMean', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ExponentialRandomVariable::GetBound() const [member function]
    cls.add_method('GetBound', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ExponentialRandomVariable::GetValue(double mean, double bound) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mean'), param('double', 'bound')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ExponentialRandomVariable::GetInteger(uint32_t mean, uint32_t bound) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mean'), param('uint32_t', 'bound')])
    ## random-variable-stream.h (module 'core'): double ns3::ExponentialRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ExponentialRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3FixedRssLossModel_methods(root_module, cls):
    ## propagation-loss-model.h (module 'propagation'): static ns3::TypeId ns3::FixedRssLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h (module 'propagation'): ns3::FixedRssLossModel::FixedRssLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h (module 'propagation'): void ns3::FixedRssLossModel::SetRss(double rss) [member function]
    cls.add_method('SetRss', 
                   'void', 
                   [param('double', 'rss')])
    ## propagation-loss-model.h (module 'propagation'): double ns3::FixedRssLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    ## propagation-loss-model.h (module 'propagation'): int64_t ns3::FixedRssLossModel::DoAssignStreams(int64_t stream) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3FriisPropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h (module 'propagation'): static ns3::TypeId ns3::FriisPropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h (module 'propagation'): ns3::FriisPropagationLossModel::FriisPropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h (module 'propagation'): void ns3::FriisPropagationLossModel::SetFrequency(double frequency) [member function]
    cls.add_method('SetFrequency', 
                   'void', 
                   [param('double', 'frequency')])
    ## propagation-loss-model.h (module 'propagation'): void ns3::FriisPropagationLossModel::SetSystemLoss(double systemLoss) [member function]
    cls.add_method('SetSystemLoss', 
                   'void', 
                   [param('double', 'systemLoss')])
    ## propagation-loss-model.h (module 'propagation'): void ns3::FriisPropagationLossModel::SetMinLoss(double minLoss) [member function]
    cls.add_method('SetMinLoss', 
                   'void', 
                   [param('double', 'minLoss')])
    ## propagation-loss-model.h (module 'propagation'): double ns3::FriisPropagationLossModel::GetMinLoss() const [member function]
    cls.add_method('GetMinLoss', 
                   'double', 
                   [], 
                   is_const=True)
    ## propagation-loss-model.h (module 'propagation'): double ns3::FriisPropagationLossModel::GetFrequency() const [member function]
    cls.add_method('GetFrequency', 
                   'double', 
                   [], 
                   is_const=True)
    ## propagation-loss-model.h (module 'propagation'): double ns3::FriisPropagationLossModel::GetSystemLoss() const [member function]
    cls.add_method('GetSystemLoss', 
                   'double', 
                   [], 
                   is_const=True)
    ## propagation-loss-model.h (module 'propagation'): double ns3::FriisPropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    ## propagation-loss-model.h (module 'propagation'): int64_t ns3::FriisPropagationLossModel::DoAssignStreams(int64_t stream) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3GammaRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::GammaRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::GammaRandomVariable::GammaRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::GammaRandomVariable::GetAlpha() const [member function]
    cls.add_method('GetAlpha', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::GammaRandomVariable::GetBeta() const [member function]
    cls.add_method('GetBeta', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::GammaRandomVariable::GetValue(double alpha, double beta) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'alpha'), param('double', 'beta')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::GammaRandomVariable::GetInteger(uint32_t alpha, uint32_t beta) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'alpha'), param('uint32_t', 'beta')])
    ## random-variable-stream.h (module 'core'): double ns3::GammaRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::GammaRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3GwTrailer_methods(root_module, cls):
    ## gw-trailer.h (module 'lora'): ns3::GwTrailer::GwTrailer(ns3::GwTrailer const & arg0) [constructor]
    cls.add_constructor([param('ns3::GwTrailer const &', 'arg0')])
    ## gw-trailer.h (module 'lora'): ns3::GwTrailer::GwTrailer() [constructor]
    cls.add_constructor([])
    ## gw-trailer.h (module 'lora'): uint32_t ns3::GwTrailer::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## gw-trailer.h (module 'lora'): uint32_t ns3::GwTrailer::GetBandwidth() [member function]
    cls.add_method('GetBandwidth', 
                   'uint32_t', 
                   [])
    ## gw-trailer.h (module 'lora'): uint32_t ns3::GwTrailer::GetFrequency() [member function]
    cls.add_method('GetFrequency', 
                   'uint32_t', 
                   [])
    ## gw-trailer.h (module 'lora'): uint32_t ns3::GwTrailer::GetGateway() [member function]
    cls.add_method('GetGateway', 
                   'uint32_t', 
                   [])
    ## gw-trailer.h (module 'lora'): ns3::TypeId ns3::GwTrailer::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## gw-trailer.h (module 'lora'): double ns3::GwTrailer::GetRssi() const [member function]
    cls.add_method('GetRssi', 
                   'double', 
                   [], 
                   is_const=True)
    ## gw-trailer.h (module 'lora'): uint32_t ns3::GwTrailer::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## gw-trailer.h (module 'lora'): uint8_t ns3::GwTrailer::GetSpreadingFactor() [member function]
    cls.add_method('GetSpreadingFactor', 
                   'uint8_t', 
                   [])
    ## gw-trailer.h (module 'lora'): static ns3::TypeId ns3::GwTrailer::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## gw-trailer.h (module 'lora'): void ns3::GwTrailer::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## gw-trailer.h (module 'lora'): void ns3::GwTrailer::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## gw-trailer.h (module 'lora'): void ns3::GwTrailer::SetBandwidth(uint32_t bandwidth) [member function]
    cls.add_method('SetBandwidth', 
                   'void', 
                   [param('uint32_t', 'bandwidth')])
    ## gw-trailer.h (module 'lora'): void ns3::GwTrailer::SetFrequency(uint32_t freq) [member function]
    cls.add_method('SetFrequency', 
                   'void', 
                   [param('uint32_t', 'freq')])
    ## gw-trailer.h (module 'lora'): void ns3::GwTrailer::SetGateway(uint32_t gatewayId) [member function]
    cls.add_method('SetGateway', 
                   'void', 
                   [param('uint32_t', 'gatewayId')])
    ## gw-trailer.h (module 'lora'): void ns3::GwTrailer::SetRssi(double rssi) [member function]
    cls.add_method('SetRssi', 
                   'void', 
                   [param('double', 'rssi')])
    ## gw-trailer.h (module 'lora'): void ns3::GwTrailer::SetSpreadingFactor(uint8_t sf) [member function]
    cls.add_method('SetSpreadingFactor', 
                   'void', 
                   [param('uint8_t', 'sf')])
    return

def register_Ns3IntegerValue_methods(root_module, cls):
    ## integer.h (module 'core'): ns3::IntegerValue::IntegerValue() [constructor]
    cls.add_constructor([])
    ## integer.h (module 'core'): ns3::IntegerValue::IntegerValue(int64_t const & value) [constructor]
    cls.add_constructor([param('int64_t const &', 'value')])
    ## integer.h (module 'core'): ns3::IntegerValue::IntegerValue(ns3::IntegerValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::IntegerValue const &', 'arg0')])
    ## integer.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::IntegerValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## integer.h (module 'core'): bool ns3::IntegerValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## integer.h (module 'core'): int64_t ns3::IntegerValue::Get() const [member function]
    cls.add_method('Get', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## integer.h (module 'core'): std::string ns3::IntegerValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## integer.h (module 'core'): void ns3::IntegerValue::Set(int64_t const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('int64_t const &', 'value')])
    return

def register_Ns3Ipv4AddressChecker_methods(root_module, cls):
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressChecker::Ipv4AddressChecker() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressChecker::Ipv4AddressChecker(ns3::Ipv4AddressChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::Ipv4AddressChecker const &', 'arg0')])
    return

def register_Ns3Ipv4AddressValue_methods(root_module, cls):
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressValue::Ipv4AddressValue() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressValue::Ipv4AddressValue(ns3::Ipv4Address const & value) [constructor]
    cls.add_constructor([param('ns3::Ipv4Address const &', 'value')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressValue::Ipv4AddressValue(ns3::Ipv4AddressValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::Ipv4AddressValue const &', 'arg0')])
    ## ipv4-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Ipv4AddressValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4AddressValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address ns3::Ipv4AddressValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): std::string ns3::Ipv4AddressValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4AddressValue::Set(ns3::Ipv4Address const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv4Address const &', 'value')])
    return

def register_Ns3Ipv4MaskChecker_methods(root_module, cls):
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskChecker::Ipv4MaskChecker() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskChecker::Ipv4MaskChecker(ns3::Ipv4MaskChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::Ipv4MaskChecker const &', 'arg0')])
    return

def register_Ns3Ipv4MaskValue_methods(root_module, cls):
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskValue::Ipv4MaskValue() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskValue::Ipv4MaskValue(ns3::Ipv4Mask const & value) [constructor]
    cls.add_constructor([param('ns3::Ipv4Mask const &', 'value')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskValue::Ipv4MaskValue(ns3::Ipv4MaskValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::Ipv4MaskValue const &', 'arg0')])
    ## ipv4-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Ipv4MaskValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4MaskValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask ns3::Ipv4MaskValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): std::string ns3::Ipv4MaskValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4MaskValue::Set(ns3::Ipv4Mask const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv4Mask const &', 'value')])
    return

def register_Ns3Ipv6AddressChecker_methods(root_module, cls):
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressChecker::Ipv6AddressChecker() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressChecker::Ipv6AddressChecker(ns3::Ipv6AddressChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::Ipv6AddressChecker const &', 'arg0')])
    return

def register_Ns3Ipv6AddressValue_methods(root_module, cls):
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressValue::Ipv6AddressValue() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressValue::Ipv6AddressValue(ns3::Ipv6Address const & value) [constructor]
    cls.add_constructor([param('ns3::Ipv6Address const &', 'value')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressValue::Ipv6AddressValue(ns3::Ipv6AddressValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::Ipv6AddressValue const &', 'arg0')])
    ## ipv6-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Ipv6AddressValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6AddressValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address ns3::Ipv6AddressValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): std::string ns3::Ipv6AddressValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6AddressValue::Set(ns3::Ipv6Address const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv6Address const &', 'value')])
    return

def register_Ns3Ipv6PrefixChecker_methods(root_module, cls):
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixChecker::Ipv6PrefixChecker() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixChecker::Ipv6PrefixChecker(ns3::Ipv6PrefixChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::Ipv6PrefixChecker const &', 'arg0')])
    return

def register_Ns3Ipv6PrefixValue_methods(root_module, cls):
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixValue::Ipv6PrefixValue() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixValue::Ipv6PrefixValue(ns3::Ipv6Prefix const & value) [constructor]
    cls.add_constructor([param('ns3::Ipv6Prefix const &', 'value')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixValue::Ipv6PrefixValue(ns3::Ipv6PrefixValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::Ipv6PrefixValue const &', 'arg0')])
    ## ipv6-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Ipv6PrefixValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6PrefixValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix ns3::Ipv6PrefixValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): std::string ns3::Ipv6PrefixValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6PrefixValue::Set(ns3::Ipv6Prefix const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv6Prefix const &', 'value')])
    return

def register_Ns3LoRaApplication_methods(root_module, cls):
    ## lora-application.h (module 'lora'): static ns3::TypeId ns3::LoRaApplication::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-application.h (module 'lora'): ns3::LoRaApplication::LoRaApplication() [constructor]
    cls.add_constructor([])
    ## lora-application.h (module 'lora'): ns3::LoRaApplication::LoRaApplication(ns3::LoRaApplication const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaApplication const &', 'arg0')])
    ## lora-application.h (module 'lora'): void ns3::LoRaApplication::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-application.h (module 'lora'): void ns3::LoRaApplication::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-application.h (module 'lora'): void ns3::LoRaApplication::StartApplication() [member function]
    cls.add_method('StartApplication', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-application.h (module 'lora'): void ns3::LoRaApplication::StopApplication() [member function]
    cls.add_method('StopApplication', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3LoRaErrorModel_methods(root_module, cls):
    ## lora-error-model.h (module 'lora'): ns3::LoRaErrorModel::LoRaErrorModel(ns3::LoRaErrorModel const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaErrorModel const &', 'arg0')])
    ## lora-error-model.h (module 'lora'): ns3::LoRaErrorModel::LoRaErrorModel() [constructor]
    cls.add_constructor([])
    ## lora-error-model.h (module 'lora'): long double ns3::LoRaErrorModel::GetBER(double snr, uint16_t spreading, int bandwidth) const [member function]
    cls.add_method('GetBER', 
                   'long double', 
                   [param('double', 'snr'), param('uint16_t', 'spreading'), param('int', 'bandwidth')], 
                   is_const=True)
    ## lora-error-model.h (module 'lora'): static ns3::TypeId ns3::LoRaErrorModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3LoRaMacCommand_methods(root_module, cls):
    ## lora-mac-command.h (module 'lora'): ns3::LoRaMacCommand::LoRaMacCommand() [constructor]
    cls.add_constructor([])
    ## lora-mac-command.h (module 'lora'): ns3::LoRaMacCommand::LoRaMacCommand(ns3::LoRaMacCommand const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaMacCommand const &', 'arg0')])
    ## lora-mac-command.h (module 'lora'): static ns3::Ptr<ns3::LoRaMacCommand> ns3::LoRaMacCommand::CommandBasedOnCid(uint8_t cid, ns3::LoRaMacCommandDirection direction) [member function]
    cls.add_method('CommandBasedOnCid', 
                   'ns3::Ptr< ns3::LoRaMacCommand >', 
                   [param('uint8_t', 'cid'), param('ns3::LoRaMacCommandDirection', 'direction')], 
                   is_static=True)
    ## lora-mac-command.h (module 'lora'): uint32_t ns3::LoRaMacCommand::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lora-mac-command.h (module 'lora'): void ns3::LoRaMacCommand::Execute(ns3::Ptr<ns3::LoRaNetDevice> netDevice, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetDevice >', 'netDevice'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## lora-mac-command.h (module 'lora'): void ns3::LoRaMacCommand::Execute(ns3::Ptr<ns3::LoRaNetworkApplication> app, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetworkApplication >', 'app'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## lora-mac-command.h (module 'lora'): ns3::LoRaMacCommandDirection ns3::LoRaMacCommand::GetDirection() const [member function]
    cls.add_method('GetDirection', 
                   'ns3::LoRaMacCommandDirection', 
                   [], 
                   is_const=True)
    ## lora-mac-command.h (module 'lora'): ns3::TypeId ns3::LoRaMacCommand::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-mac-command.h (module 'lora'): uint32_t ns3::LoRaMacCommand::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## lora-mac-command.h (module 'lora'): ns3::LoRaMacCommandCid ns3::LoRaMacCommand::GetType() const [member function]
    cls.add_method('GetType', 
                   'ns3::LoRaMacCommandCid', 
                   [], 
                   is_const=True)
    ## lora-mac-command.h (module 'lora'): static ns3::LoRaMacCommandCid ns3::LoRaMacCommand::GetType(uint8_t arg0) [member function]
    cls.add_method('GetType', 
                   'ns3::LoRaMacCommandCid', 
                   [param('uint8_t', 'arg0')], 
                   is_static=True)
    ## lora-mac-command.h (module 'lora'): static ns3::TypeId ns3::LoRaMacCommand::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-mac-command.h (module 'lora'): void ns3::LoRaMacCommand::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## lora-mac-command.h (module 'lora'): void ns3::LoRaMacCommand::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## lora-mac-command.h (module 'lora'): void ns3::LoRaMacCommand::SetDirection(ns3::LoRaMacCommandDirection direction) [member function]
    cls.add_method('SetDirection', 
                   'void', 
                   [param('ns3::LoRaMacCommandDirection', 'direction')])
    ## lora-mac-command.h (module 'lora'): void ns3::LoRaMacCommand::SetType(ns3::LoRaMacCommandCid cid) [member function]
    cls.add_method('SetType', 
                   'void', 
                   [param('ns3::LoRaMacCommandCid', 'cid')])
    return

def register_Ns3LoRaMacTrailer_methods(root_module, cls):
    ## lora-mac-trailer.h (module 'lora'): ns3::LoRaMacTrailer::LoRaMacTrailer(ns3::LoRaMacTrailer const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaMacTrailer const &', 'arg0')])
    ## lora-mac-trailer.h (module 'lora'): ns3::LoRaMacTrailer::LoRaMacTrailer() [constructor]
    cls.add_constructor([])
    ## lora-mac-trailer.h (module 'lora'): bool ns3::LoRaMacTrailer::CheckMIC(ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('CheckMIC', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet const >', 'p')])
    ## lora-mac-trailer.h (module 'lora'): uint32_t ns3::LoRaMacTrailer::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## lora-mac-trailer.h (module 'lora'): ns3::TypeId ns3::LoRaMacTrailer::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-mac-trailer.h (module 'lora'): uint16_t ns3::LoRaMacTrailer::GetMIC() const [member function]
    cls.add_method('GetMIC', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## lora-mac-trailer.h (module 'lora'): uint32_t ns3::LoRaMacTrailer::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-mac-trailer.h (module 'lora'): static ns3::TypeId ns3::LoRaMacTrailer::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-mac-trailer.h (module 'lora'): void ns3::LoRaMacTrailer::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## lora-mac-trailer.h (module 'lora'): void ns3::LoRaMacTrailer::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## lora-mac-trailer.h (module 'lora'): void ns3::LoRaMacTrailer::SetMIC(ns3::Ptr<const ns3::Packet> p) [member function]
    cls.add_method('SetMIC', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'p')])
    return

def register_Ns3LoRaNetwork_methods(root_module, cls):
    ## lora-network.h (module 'lora'): static ns3::TypeId ns3::LoRaNetwork::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-network.h (module 'lora'): ns3::LoRaNetwork::LoRaNetwork() [constructor]
    cls.add_constructor([])
    ## lora-network.h (module 'lora'): bool ns3::LoRaNetwork::Send(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('Send', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## lora-network.h (module 'lora'): bool ns3::LoRaNetwork::MessageReceived(ns3::Ptr<const ns3::Packet> packet, ns3::Address const & from) [member function]
    cls.add_method('MessageReceived', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Address const &', 'from')])
    ## lora-network.h (module 'lora'): void ns3::LoRaNetwork::RemoveMessage(ns3::Address const & address) [member function]
    cls.add_method('RemoveMessage', 
                   'void', 
                   [param('ns3::Address const &', 'address')])
    ## lora-network.h (module 'lora'): void ns3::LoRaNetwork::WhiteListDevice(ns3::Address const & address) [member function]
    cls.add_method('WhiteListDevice', 
                   'void', 
                   [param('ns3::Address const &', 'address')])
    ## lora-network.h (module 'lora'): void ns3::LoRaNetwork::SetDelayOfDevice(ns3::Address const & address, uint8_t delay) [member function]
    cls.add_method('SetDelayOfDevice', 
                   'void', 
                   [param('ns3::Address const &', 'address'), param('uint8_t', 'delay')])
    ## lora-network.h (module 'lora'): void ns3::LoRaNetwork::SetSettingsOfDevice(ns3::Address const & address, uint8_t offset, uint8_t dr, uint32_t freq) [member function]
    cls.add_method('SetSettingsOfDevice', 
                   'void', 
                   [param('ns3::Address const &', 'address'), param('uint8_t', 'offset'), param('uint8_t', 'dr'), param('uint32_t', 'freq')])
    ## lora-network.h (module 'lora'): uint8_t ns3::LoRaNetwork::GetCount(ns3::Address const & address) [member function]
    cls.add_method('GetCount', 
                   'uint8_t', 
                   [param('ns3::Address const &', 'address')])
    ## lora-network.h (module 'lora'): uint8_t ns3::LoRaNetwork::GetMargin(ns3::Address const & address) [member function]
    cls.add_method('GetMargin', 
                   'uint8_t', 
                   [param('ns3::Address const &', 'address')])
    ## lora-network.h (module 'lora'): void ns3::LoRaNetwork::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lora-network.h (module 'lora'): ns3::LoRaNetwork::LoRaNetwork(ns3::LoRaNetwork const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaNetwork const &', 'arg0')])
    ## lora-network.h (module 'lora'): void ns3::LoRaNetwork::StartApplication() [member function]
    cls.add_method('StartApplication', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-network.h (module 'lora'): void ns3::LoRaNetwork::StopApplication() [member function]
    cls.add_method('StopApplication', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3LoRaNetworkApplication_methods(root_module, cls):
    ## lora-network-application.h (module 'lora'): ns3::LoRaNetworkApplication::LoRaNetworkApplication() [constructor]
    cls.add_constructor([])
    ## lora-network-application.h (module 'lora'): ns3::LoRaNetworkApplication::LoRaNetworkApplication(ns3::LoRaNetworkApplication const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaNetworkApplication const &', 'arg0')])
    ## lora-network-application.h (module 'lora'): void ns3::LoRaNetworkApplication::ConfirmChannelMask(ns3::Address const & address) [member function]
    cls.add_method('ConfirmChannelMask', 
                   'void', 
                   [param('ns3::Address const &', 'address')], 
                   is_virtual=True)
    ## lora-network-application.h (module 'lora'): void ns3::LoRaNetworkApplication::ConfirmDataRate(ns3::Address const & address) [member function]
    cls.add_method('ConfirmDataRate', 
                   'void', 
                   [param('ns3::Address const &', 'address')], 
                   is_virtual=True)
    ## lora-network-application.h (module 'lora'): void ns3::LoRaNetworkApplication::ConfirmFrequency(ns3::Address const & address) [member function]
    cls.add_method('ConfirmFrequency', 
                   'void', 
                   [param('ns3::Address const &', 'address')], 
                   is_virtual=True)
    ## lora-network-application.h (module 'lora'): void ns3::LoRaNetworkApplication::ConfirmPower(ns3::Address const & address) [member function]
    cls.add_method('ConfirmPower', 
                   'void', 
                   [param('ns3::Address const &', 'address')], 
                   is_virtual=True)
    ## lora-network-application.h (module 'lora'): ns3::Ptr<ns3::LoRaNetwork> ns3::LoRaNetworkApplication::GetNetwork() [member function]
    cls.add_method('GetNetwork', 
                   'ns3::Ptr< ns3::LoRaNetwork >', 
                   [])
    ## lora-network-application.h (module 'lora'): static ns3::TypeId ns3::LoRaNetworkApplication::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-network-application.h (module 'lora'): void ns3::LoRaNetworkApplication::NewPacket(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('NewPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lora-network-application.h (module 'lora'): void ns3::LoRaNetworkApplication::SetMacAnswer(ns3::Ptr<ns3::LoRaMacCommand> command) [member function]
    cls.add_method('SetMacAnswer', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaMacCommand >', 'command')], 
                   is_virtual=True)
    ## lora-network-application.h (module 'lora'): void ns3::LoRaNetworkApplication::SetNetwork(ns3::Ptr<ns3::LoRaNetwork> network) [member function]
    cls.add_method('SetNetwork', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetwork >', 'network')])
    ## lora-network-application.h (module 'lora'): void ns3::LoRaNetworkApplication::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-network-application.h (module 'lora'): void ns3::LoRaNetworkApplication::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3LoRaNetworkTrailer_methods(root_module, cls):
    ## lora-network-trailer.h (module 'lora'): ns3::LoRaNetworkTrailer::LoRaNetworkTrailer(ns3::LoRaNetworkTrailer const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaNetworkTrailer const &', 'arg0')])
    ## lora-network-trailer.h (module 'lora'): ns3::LoRaNetworkTrailer::LoRaNetworkTrailer() [constructor]
    cls.add_constructor([])
    ## lora-network-trailer.h (module 'lora'): ns3::LoRaNetworkTrailer::LoRaNetworkTrailer(uint8_t delay, uint8_t rx1Offset, uint8_t rx2Dr, uint32_t rx2Freq) [constructor]
    cls.add_constructor([param('uint8_t', 'delay'), param('uint8_t', 'rx1Offset'), param('uint8_t', 'rx2Dr'), param('uint32_t', 'rx2Freq')])
    ## lora-network-trailer.h (module 'lora'): uint32_t ns3::LoRaNetworkTrailer::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## lora-network-trailer.h (module 'lora'): uint8_t ns3::LoRaNetworkTrailer::GetDelay() [member function]
    cls.add_method('GetDelay', 
                   'uint8_t', 
                   [])
    ## lora-network-trailer.h (module 'lora'): ns3::TypeId ns3::LoRaNetworkTrailer::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-network-trailer.h (module 'lora'): uint8_t ns3::LoRaNetworkTrailer::GetRx1Offset() [member function]
    cls.add_method('GetRx1Offset', 
                   'uint8_t', 
                   [])
    ## lora-network-trailer.h (module 'lora'): uint8_t ns3::LoRaNetworkTrailer::GetRx2Dr() [member function]
    cls.add_method('GetRx2Dr', 
                   'uint8_t', 
                   [])
    ## lora-network-trailer.h (module 'lora'): uint32_t ns3::LoRaNetworkTrailer::GetRx2Freq() [member function]
    cls.add_method('GetRx2Freq', 
                   'uint32_t', 
                   [])
    ## lora-network-trailer.h (module 'lora'): uint32_t ns3::LoRaNetworkTrailer::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-network-trailer.h (module 'lora'): static ns3::TypeId ns3::LoRaNetworkTrailer::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-network-trailer.h (module 'lora'): void ns3::LoRaNetworkTrailer::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## lora-network-trailer.h (module 'lora'): void ns3::LoRaNetworkTrailer::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## lora-network-trailer.h (module 'lora'): void ns3::LoRaNetworkTrailer::SetDelay(uint8_t delay) [member function]
    cls.add_method('SetDelay', 
                   'void', 
                   [param('uint8_t', 'delay')])
    ## lora-network-trailer.h (module 'lora'): void ns3::LoRaNetworkTrailer::SetRx1Offset(uint8_t rx1Offset) [member function]
    cls.add_method('SetRx1Offset', 
                   'void', 
                   [param('uint8_t', 'rx1Offset')])
    ## lora-network-trailer.h (module 'lora'): void ns3::LoRaNetworkTrailer::SetRx2Dr(uint8_t rx2Dr) [member function]
    cls.add_method('SetRx2Dr', 
                   'void', 
                   [param('uint8_t', 'rx2Dr')])
    ## lora-network-trailer.h (module 'lora'): void ns3::LoRaNetworkTrailer::SetRx2Freq(uint32_t rx2Freq) [member function]
    cls.add_method('SetRx2Freq', 
                   'void', 
                   [param('uint32_t', 'rx2Freq')])
    return

def register_Ns3LoRaNoPowerApplication_methods(root_module, cls):
    ## lora-no-power-application.h (module 'lora'): ns3::LoRaNoPowerApplication::LoRaNoPowerApplication(ns3::LoRaNoPowerApplication const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaNoPowerApplication const &', 'arg0')])
    ## lora-no-power-application.h (module 'lora'): ns3::LoRaNoPowerApplication::LoRaNoPowerApplication() [constructor]
    cls.add_constructor([])
    ## lora-no-power-application.h (module 'lora'): static ns3::TypeId ns3::LoRaNoPowerApplication::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-no-power-application.h (module 'lora'): void ns3::LoRaNoPowerApplication::NewPacket(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('NewPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')], 
                   is_virtual=True)
    ## lora-no-power-application.h (module 'lora'): void ns3::LoRaNoPowerApplication::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-no-power-application.h (module 'lora'): void ns3::LoRaNoPowerApplication::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3LoRaPhy_methods(root_module, cls):
    ## lora-phy.h (module 'lora'): ns3::LoRaPhy::LoRaPhy() [constructor]
    cls.add_constructor([])
    ## lora-phy.h (module 'lora'): static ns3::TypeId ns3::LoRaPhy::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetDevice(ns3::Ptr<ns3::NetDevice> d) [member function]
    cls.add_method('SetDevice', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'd')], 
                   is_virtual=True)
    ## lora-phy.h (module 'lora'): ns3::Ptr<ns3::NetDevice> ns3::LoRaPhy::GetDevice() const [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetMobility(ns3::Ptr<ns3::MobilityModel> m) [member function]
    cls.add_method('SetMobility', 
                   'void', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'm')], 
                   is_virtual=True)
    ## lora-phy.h (module 'lora'): ns3::Ptr<ns3::MobilityModel> ns3::LoRaPhy::GetMobility() [member function]
    cls.add_method('GetMobility', 
                   'ns3::Ptr< ns3::MobilityModel >', 
                   [], 
                   is_virtual=True)
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetChannel(ns3::Ptr<ns3::SpectrumChannel> c) [member function]
    cls.add_method('SetChannel', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumChannel >', 'c')], 
                   is_virtual=True)
    ## lora-phy.h (module 'lora'): ns3::Ptr<const ns3::SpectrumModel> ns3::LoRaPhy::GetRxSpectrumModel() const [member function]
    cls.add_method('GetRxSpectrumModel', 
                   'ns3::Ptr< ns3::SpectrumModel const >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetRxSpectrumModel(ns3::Ptr<const ns3::SpectrumModel> model) [member function]
    cls.add_method('SetRxSpectrumModel', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumModel const >', 'model')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::InitPowerSpectralDensity() [member function]
    cls.add_method('InitPowerSpectralDensity', 
                   'void', 
                   [])
    ## lora-phy.h (module 'lora'): ns3::Ptr<ns3::AntennaModel> ns3::LoRaPhy::GetRxAntenna() [member function]
    cls.add_method('GetRxAntenna', 
                   'ns3::Ptr< ns3::AntennaModel >', 
                   [], 
                   is_virtual=True)
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetRxAntenna(ns3::Ptr<ns3::AntennaModel> a) [member function]
    cls.add_method('SetRxAntenna', 
                   'void', 
                   [param('ns3::Ptr< ns3::AntennaModel >', 'a')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::StartRx(ns3::Ptr<ns3::SpectrumSignalParameters> params) [member function]
    cls.add_method('StartRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumSignalParameters >', 'params')], 
                   is_virtual=True)
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::EndRx(ns3::Ptr<ns3::LoRaSpectrumSignalParameters> params) [member function]
    cls.add_method('EndRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaSpectrumSignalParameters >', 'params')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::EndNoise(ns3::Ptr<ns3::SpectrumValue> sv) [member function]
    cls.add_method('EndNoise', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumValue >', 'sv')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::EndSignal(ns3::Ptr<ns3::SpectrumValue> sv, uint32_t frequency, uint8_t spreading, uint32_t bandwidth) [member function]
    cls.add_method('EndSignal', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumValue >', 'sv'), param('uint32_t', 'frequency'), param('uint8_t', 'spreading'), param('uint32_t', 'bandwidth')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetTransmissionEndCallback(ns3::Callback<void, ns3::Ptr<const ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetTransmissionEndCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetReceptionStartCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetReceptionStartCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetReceptionEndCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetReceptionEndCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetReceptionErrorCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetReceptionErrorCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetReceptionMacCallback(ns3::Callback<void, ns3::LoRaMacHeader, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetReceptionMacCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::LoRaMacHeader, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## lora-phy.h (module 'lora'): bool ns3::LoRaPhy::StartTx(ns3::Ptr<ns3::Packet> packet) [member function]
    cls.add_method('StartTx', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::EndTx(ns3::Ptr<ns3::Packet> packet) [member function]
    cls.add_method('EndTx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetChannelIndex(uint32_t channel) [member function]
    cls.add_method('SetChannelIndex', 
                   'void', 
                   [param('uint32_t', 'channel')])
    ## lora-phy.h (module 'lora'): uint32_t ns3::LoRaPhy::GetChannelIndex() [member function]
    cls.add_method('GetChannelIndex', 
                   'uint32_t', 
                   [])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetSpreadingFactor(uint8_t sf) [member function]
    cls.add_method('SetSpreadingFactor', 
                   'void', 
                   [param('uint8_t', 'sf')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetBandwidth(uint32_t bandwidth) [member function]
    cls.add_method('SetBandwidth', 
                   'void', 
                   [param('uint32_t', 'bandwidth')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::SetPower(double power) [member function]
    cls.add_method('SetPower', 
                   'void', 
                   [param('double', 'power')])
    ## lora-phy.h (module 'lora'): int ns3::LoRaPhy::GetBitRate(uint8_t sf) [member function]
    cls.add_method('GetBitRate', 
                   'int', 
                   [param('uint8_t', 'sf')])
    ## lora-phy.h (module 'lora'): ns3::Time ns3::LoRaPhy::GetTimeOfPacket(uint16_t length, uint8_t sf) [member function]
    cls.add_method('GetTimeOfPacket', 
                   'ns3::Time', 
                   [param('uint16_t', 'length'), param('uint8_t', 'sf')])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::ChangeState(ns3::LoRaPhy::State state) [member function]
    cls.add_method('ChangeState', 
                   'void', 
                   [param('ns3::LoRaPhy::State', 'state')])
    ## lora-phy.h (module 'lora'): ns3::Ptr<ns3::SpectrumValue> ns3::LoRaPhy::GetTxPowerSpectralDensity(uint32_t channeloffset, double power) [member function]
    cls.add_method('GetTxPowerSpectralDensity', 
                   'ns3::Ptr< ns3::SpectrumValue >', 
                   [param('uint32_t', 'channeloffset'), param('double', 'power')])
    ## lora-phy.h (module 'lora'): ns3::Ptr<ns3::SpectrumValue> ns3::LoRaPhy::GetFullTxPowerSpectralDensity(uint32_t channeloffset, double power) [member function]
    cls.add_method('GetFullTxPowerSpectralDensity', 
                   'ns3::Ptr< ns3::SpectrumValue >', 
                   [param('uint32_t', 'channeloffset'), param('double', 'power')])
    ## lora-phy.h (module 'lora'): double ns3::LoRaPhy::GetRssiLastPacket() [member function]
    cls.add_method('GetRssiLastPacket', 
                   'double', 
                   [])
    ## lora-phy.h (module 'lora'): double ns3::LoRaPhy::GetSnrLastPacket() [member function]
    cls.add_method('GetSnrLastPacket', 
                   'double', 
                   [])
    ## lora-phy.h (module 'lora'): bool ns3::LoRaPhy::IsTransmitting() [member function]
    cls.add_method('IsTransmitting', 
                   'bool', 
                   [])
    ## lora-phy.h (module 'lora'): void ns3::LoRaPhy::UpdateBer() [member function]
    cls.add_method('UpdateBer', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3LoRaPowerApplication_methods(root_module, cls):
    ## lora-power-application.h (module 'lora'): ns3::LoRaPowerApplication::LoRaPowerApplication(ns3::LoRaPowerApplication const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaPowerApplication const &', 'arg0')])
    ## lora-power-application.h (module 'lora'): ns3::LoRaPowerApplication::LoRaPowerApplication() [constructor]
    cls.add_constructor([])
    ## lora-power-application.h (module 'lora'): void ns3::LoRaPowerApplication::ConfirmPower(ns3::Address const & address) [member function]
    cls.add_method('ConfirmPower', 
                   'void', 
                   [param('ns3::Address const &', 'address')], 
                   is_virtual=True)
    ## lora-power-application.h (module 'lora'): static ns3::TypeId ns3::LoRaPowerApplication::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-power-application.h (module 'lora'): void ns3::LoRaPowerApplication::NewPacket(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('NewPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')], 
                   is_virtual=True)
    ## lora-power-application.h (module 'lora'): void ns3::LoRaPowerApplication::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-power-application.h (module 'lora'): void ns3::LoRaPowerApplication::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-power-application.h (module 'lora'): void ns3::LoRaPowerApplication::StartApplication() [member function]
    cls.add_method('StartApplication', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## lora-power-application.h (module 'lora'): void ns3::LoRaPowerApplication::StopApplication() [member function]
    cls.add_method('StopApplication', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3LoRaRadioEnergyModel_methods(root_module, cls):
    ## lora-radio-energy-model.h (module 'lora'): ns3::LoRaRadioEnergyModel::LoRaRadioEnergyModel(ns3::LoRaRadioEnergyModel const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaRadioEnergyModel const &', 'arg0')])
    ## lora-radio-energy-model.h (module 'lora'): ns3::LoRaRadioEnergyModel::LoRaRadioEnergyModel() [constructor]
    cls.add_constructor([])
    ## lora-radio-energy-model.h (module 'lora'): void ns3::LoRaRadioEnergyModel::ChangeLoRaState(ns3::LoRaPhy::State newstate) [member function]
    cls.add_method('ChangeLoRaState', 
                   'void', 
                   [param('ns3::LoRaPhy::State', 'newstate')])
    ## lora-radio-energy-model.h (module 'lora'): void ns3::LoRaRadioEnergyModel::ChangeState(int newState) [member function]
    cls.add_method('ChangeState', 
                   'void', 
                   [param('int', 'newState')], 
                   is_virtual=True)
    ## lora-radio-energy-model.h (module 'lora'): ns3::LoRaPhy::State ns3::LoRaRadioEnergyModel::GetCurrentState() const [member function]
    cls.add_method('GetCurrentState', 
                   'ns3::LoRaPhy::State', 
                   [], 
                   is_const=True)
    ## lora-radio-energy-model.h (module 'lora'): double ns3::LoRaRadioEnergyModel::GetIdleCurrentA() const [member function]
    cls.add_method('GetIdleCurrentA', 
                   'double', 
                   [], 
                   is_const=True)
    ## lora-radio-energy-model.h (module 'lora'): double ns3::LoRaRadioEnergyModel::GetRxCurrentA() const [member function]
    cls.add_method('GetRxCurrentA', 
                   'double', 
                   [], 
                   is_const=True)
    ## lora-radio-energy-model.h (module 'lora'): double ns3::LoRaRadioEnergyModel::GetTotalEnergyConsumption() const [member function]
    cls.add_method('GetTotalEnergyConsumption', 
                   'double', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-radio-energy-model.h (module 'lora'): double ns3::LoRaRadioEnergyModel::GetTxCurrentA() const [member function]
    cls.add_method('GetTxCurrentA', 
                   'double', 
                   [], 
                   is_const=True)
    ## lora-radio-energy-model.h (module 'lora'): static ns3::TypeId ns3::LoRaRadioEnergyModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-radio-energy-model.h (module 'lora'): void ns3::LoRaRadioEnergyModel::HandleEnergyChanged() [member function]
    cls.add_method('HandleEnergyChanged', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lora-radio-energy-model.h (module 'lora'): void ns3::LoRaRadioEnergyModel::HandleEnergyDepletion() [member function]
    cls.add_method('HandleEnergyDepletion', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lora-radio-energy-model.h (module 'lora'): void ns3::LoRaRadioEnergyModel::HandleEnergyRecharged() [member function]
    cls.add_method('HandleEnergyRecharged', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lora-radio-energy-model.h (module 'lora'): void ns3::LoRaRadioEnergyModel::SetEnergySource(ns3::Ptr<ns3::EnergySource> source) [member function]
    cls.add_method('SetEnergySource', 
                   'void', 
                   [param('ns3::Ptr< ns3::EnergySource >', 'source')], 
                   is_virtual=True)
    ## lora-radio-energy-model.h (module 'lora'): void ns3::LoRaRadioEnergyModel::SetIdleCurrentA(double IdleCurrentA) [member function]
    cls.add_method('SetIdleCurrentA', 
                   'void', 
                   [param('double', 'IdleCurrentA')])
    ## lora-radio-energy-model.h (module 'lora'): void ns3::LoRaRadioEnergyModel::SetRxCurrentA(double RxCurrentA) [member function]
    cls.add_method('SetRxCurrentA', 
                   'void', 
                   [param('double', 'RxCurrentA')])
    ## lora-radio-energy-model.h (module 'lora'): void ns3::LoRaRadioEnergyModel::SetTxCurrentA(double txCurrentA) [member function]
    cls.add_method('SetTxCurrentA', 
                   'void', 
                   [param('double', 'txCurrentA')])
    ## lora-radio-energy-model.h (module 'lora'): void ns3::LoRaRadioEnergyModel::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## lora-radio-energy-model.h (module 'lora'): double ns3::LoRaRadioEnergyModel::DoGetCurrentA() const [member function]
    cls.add_method('DoGetCurrentA', 
                   'double', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3LoRaSinkApplication_methods(root_module, cls):
    ## lora-sink-application.h (module 'lora'): static ns3::TypeId ns3::LoRaSinkApplication::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-sink-application.h (module 'lora'): ns3::LoRaSinkApplication::LoRaSinkApplication() [constructor]
    cls.add_constructor([])
    ## lora-sink-application.h (module 'lora'): void ns3::LoRaSinkApplication::HandleRead(ns3::Ptr<ns3::Socket> socket) [member function]
    cls.add_method('HandleRead', 
                   'void', 
                   [param('ns3::Ptr< ns3::Socket >', 'socket')])
    ## lora-sink-application.h (module 'lora'): void ns3::LoRaSinkApplication::HandleLoRa(ns3::Ptr<ns3::Socket> socket) [member function]
    cls.add_method('HandleLoRa', 
                   'void', 
                   [param('ns3::Ptr< ns3::Socket >', 'socket')])
    ## lora-sink-application.h (module 'lora'): void ns3::LoRaSinkApplication::SetNetDevice(ns3::Ptr<ns3::NetDevice> device) [member function]
    cls.add_method('SetNetDevice', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device')])
    ## lora-sink-application.h (module 'lora'): ns3::LoRaSinkApplication::LoRaSinkApplication(ns3::LoRaSinkApplication const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaSinkApplication const &', 'arg0')])
    ## lora-sink-application.h (module 'lora'): void ns3::LoRaSinkApplication::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-sink-application.h (module 'lora'): void ns3::LoRaSinkApplication::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-sink-application.h (module 'lora'): void ns3::LoRaSinkApplication::StartApplication() [member function]
    cls.add_method('StartApplication', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## lora-sink-application.h (module 'lora'): void ns3::LoRaSinkApplication::StopApplication() [member function]
    cls.add_method('StopApplication', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3LoRaSpectrumSignalParameters_methods(root_module, cls):
    ## lora-spectrum-signal-parameters.h (module 'lora'): ns3::Ptr<ns3::SpectrumSignalParameters> ns3::LoRaSpectrumSignalParameters::Copy() [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::SpectrumSignalParameters >', 
                   [], 
                   is_virtual=True)
    ## lora-spectrum-signal-parameters.h (module 'lora'): ns3::LoRaSpectrumSignalParameters::LoRaSpectrumSignalParameters() [constructor]
    cls.add_constructor([])
    ## lora-spectrum-signal-parameters.h (module 'lora'): ns3::LoRaSpectrumSignalParameters::LoRaSpectrumSignalParameters(ns3::LoRaSpectrumSignalParameters const & p) [constructor]
    cls.add_constructor([param('ns3::LoRaSpectrumSignalParameters const &', 'p')])
    ## lora-spectrum-signal-parameters.h (module 'lora'): ns3::LoRaSpectrumSignalParameters::packet [variable]
    cls.add_instance_attribute('packet', 'ns3::Ptr< ns3::Packet >', is_const=False)
    ## lora-spectrum-signal-parameters.h (module 'lora'): void ns3::LoRaSpectrumSignalParameters::SetChannel(uint32_t channel) [member function]
    cls.add_method('SetChannel', 
                   'void', 
                   [param('uint32_t', 'channel')])
    ## lora-spectrum-signal-parameters.h (module 'lora'): uint32_t ns3::LoRaSpectrumSignalParameters::GetChannel() [member function]
    cls.add_method('GetChannel', 
                   'uint32_t', 
                   [])
    ## lora-spectrum-signal-parameters.h (module 'lora'): void ns3::LoRaSpectrumSignalParameters::SetSpreading(uint16_t spreading) [member function]
    cls.add_method('SetSpreading', 
                   'void', 
                   [param('uint16_t', 'spreading')])
    ## lora-spectrum-signal-parameters.h (module 'lora'): uint16_t ns3::LoRaSpectrumSignalParameters::GetSpreading() [member function]
    cls.add_method('GetSpreading', 
                   'uint16_t', 
                   [])
    ## lora-spectrum-signal-parameters.h (module 'lora'): uint32_t ns3::LoRaSpectrumSignalParameters::GetBandwidth() [member function]
    cls.add_method('GetBandwidth', 
                   'uint32_t', 
                   [])
    ## lora-spectrum-signal-parameters.h (module 'lora'): void ns3::LoRaSpectrumSignalParameters::SetBandwidth(uint32_t bw) [member function]
    cls.add_method('SetBandwidth', 
                   'void', 
                   [param('uint32_t', 'bw')])
    ## lora-spectrum-signal-parameters.h (module 'lora'): uint16_t ns3::LoRaSpectrumSignalParameters::GetBer() [member function]
    cls.add_method('GetBer', 
                   'uint16_t', 
                   [])
    ## lora-spectrum-signal-parameters.h (module 'lora'): void ns3::LoRaSpectrumSignalParameters::SetBer(uint32_t ber) [member function]
    cls.add_method('SetBer', 
                   'void', 
                   [param('uint32_t', 'ber')])
    return

def register_Ns3LoRaTestApplication_methods(root_module, cls):
    ## lora-test-application.h (module 'lora'): ns3::LoRaTestApplication::LoRaTestApplication(ns3::LoRaTestApplication const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaTestApplication const &', 'arg0')])
    ## lora-test-application.h (module 'lora'): ns3::LoRaTestApplication::LoRaTestApplication() [constructor]
    cls.add_constructor([])
    ## lora-test-application.h (module 'lora'): void ns3::LoRaTestApplication::DelayedNewPacket(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('DelayedNewPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## lora-test-application.h (module 'lora'): static ns3::TypeId ns3::LoRaTestApplication::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-test-application.h (module 'lora'): void ns3::LoRaTestApplication::NewPacket(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('NewPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')], 
                   is_virtual=True)
    ## lora-test-application.h (module 'lora'): void ns3::LoRaTestApplication::SetMacAnswer(ns3::Ptr<ns3::LoRaMacCommand> command) [member function]
    cls.add_method('SetMacAnswer', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaMacCommand >', 'command')], 
                   is_virtual=True)
    ## lora-test-application.h (module 'lora'): void ns3::LoRaTestApplication::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-test-application.h (module 'lora'): void ns3::LoRaTestApplication::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3LogDistancePropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h (module 'propagation'): static ns3::TypeId ns3::LogDistancePropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h (module 'propagation'): ns3::LogDistancePropagationLossModel::LogDistancePropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h (module 'propagation'): void ns3::LogDistancePropagationLossModel::SetPathLossExponent(double n) [member function]
    cls.add_method('SetPathLossExponent', 
                   'void', 
                   [param('double', 'n')])
    ## propagation-loss-model.h (module 'propagation'): double ns3::LogDistancePropagationLossModel::GetPathLossExponent() const [member function]
    cls.add_method('GetPathLossExponent', 
                   'double', 
                   [], 
                   is_const=True)
    ## propagation-loss-model.h (module 'propagation'): void ns3::LogDistancePropagationLossModel::SetReference(double referenceDistance, double referenceLoss) [member function]
    cls.add_method('SetReference', 
                   'void', 
                   [param('double', 'referenceDistance'), param('double', 'referenceLoss')])
    ## propagation-loss-model.h (module 'propagation'): double ns3::LogDistancePropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    ## propagation-loss-model.h (module 'propagation'): int64_t ns3::LogDistancePropagationLossModel::DoAssignStreams(int64_t stream) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3LogNormalRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::LogNormalRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::LogNormalRandomVariable::LogNormalRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::LogNormalRandomVariable::GetMu() const [member function]
    cls.add_method('GetMu', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::LogNormalRandomVariable::GetSigma() const [member function]
    cls.add_method('GetSigma', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::LogNormalRandomVariable::GetValue(double mu, double sigma) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mu'), param('double', 'sigma')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::LogNormalRandomVariable::GetInteger(uint32_t mu, uint32_t sigma) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mu'), param('uint32_t', 'sigma')])
    ## random-variable-stream.h (module 'core'): double ns3::LogNormalRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::LogNormalRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3Mac32AddressChecker_methods(root_module, cls):
    ## mac32-address.h (module 'lora'): ns3::Mac32AddressChecker::Mac32AddressChecker() [constructor]
    cls.add_constructor([])
    ## mac32-address.h (module 'lora'): ns3::Mac32AddressChecker::Mac32AddressChecker(ns3::Mac32AddressChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::Mac32AddressChecker const &', 'arg0')])
    return

def register_Ns3Mac32AddressValue_methods(root_module, cls):
    ## mac32-address.h (module 'lora'): ns3::Mac32AddressValue::Mac32AddressValue() [constructor]
    cls.add_constructor([])
    ## mac32-address.h (module 'lora'): ns3::Mac32AddressValue::Mac32AddressValue(ns3::Mac32Address const & value) [constructor]
    cls.add_constructor([param('ns3::Mac32Address const &', 'value')])
    ## mac32-address.h (module 'lora'): ns3::Mac32AddressValue::Mac32AddressValue(ns3::Mac32AddressValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::Mac32AddressValue const &', 'arg0')])
    ## mac32-address.h (module 'lora'): ns3::Ptr<ns3::AttributeValue> ns3::Mac32AddressValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mac32-address.h (module 'lora'): bool ns3::Mac32AddressValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## mac32-address.h (module 'lora'): ns3::Mac32Address ns3::Mac32AddressValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Mac32Address', 
                   [], 
                   is_const=True)
    ## mac32-address.h (module 'lora'): std::string ns3::Mac32AddressValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## mac32-address.h (module 'lora'): void ns3::Mac32AddressValue::Set(ns3::Mac32Address const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Mac32Address const &', 'value')])
    return

def register_Ns3Mac48AddressChecker_methods(root_module, cls):
    ## mac48-address.h (module 'network'): ns3::Mac48AddressChecker::Mac48AddressChecker() [constructor]
    cls.add_constructor([])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressChecker::Mac48AddressChecker(ns3::Mac48AddressChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::Mac48AddressChecker const &', 'arg0')])
    return

def register_Ns3Mac48AddressValue_methods(root_module, cls):
    ## mac48-address.h (module 'network'): ns3::Mac48AddressValue::Mac48AddressValue() [constructor]
    cls.add_constructor([])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressValue::Mac48AddressValue(ns3::Mac48Address const & value) [constructor]
    cls.add_constructor([param('ns3::Mac48Address const &', 'value')])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressValue::Mac48AddressValue(ns3::Mac48AddressValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::Mac48AddressValue const &', 'arg0')])
    ## mac48-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Mac48AddressValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mac48-address.h (module 'network'): bool ns3::Mac48AddressValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## mac48-address.h (module 'network'): ns3::Mac48Address ns3::Mac48AddressValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## mac48-address.h (module 'network'): std::string ns3::Mac48AddressValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## mac48-address.h (module 'network'): void ns3::Mac48AddressValue::Set(ns3::Mac48Address const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Mac48Address const &', 'value')])
    return

def register_Ns3MatrixPropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h (module 'propagation'): static ns3::TypeId ns3::MatrixPropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h (module 'propagation'): ns3::MatrixPropagationLossModel::MatrixPropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h (module 'propagation'): void ns3::MatrixPropagationLossModel::SetLoss(ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b, double loss, bool symmetric=true) [member function]
    cls.add_method('SetLoss', 
                   'void', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b'), param('double', 'loss'), param('bool', 'symmetric', default_value='true')])
    ## propagation-loss-model.h (module 'propagation'): void ns3::MatrixPropagationLossModel::SetDefaultLoss(double defaultLoss) [member function]
    cls.add_method('SetDefaultLoss', 
                   'void', 
                   [param('double', 'defaultLoss')])
    ## propagation-loss-model.h (module 'propagation'): double ns3::MatrixPropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    ## propagation-loss-model.h (module 'propagation'): int64_t ns3::MatrixPropagationLossModel::DoAssignStreams(int64_t stream) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3MobilityModel_methods(root_module, cls):
    ## mobility-model.h (module 'mobility'): ns3::MobilityModel::MobilityModel(ns3::MobilityModel const & arg0) [constructor]
    cls.add_constructor([param('ns3::MobilityModel const &', 'arg0')])
    ## mobility-model.h (module 'mobility'): ns3::MobilityModel::MobilityModel() [constructor]
    cls.add_constructor([])
    ## mobility-model.h (module 'mobility'): int64_t ns3::MobilityModel::AssignStreams(int64_t stream) [member function]
    cls.add_method('AssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')])
    ## mobility-model.h (module 'mobility'): double ns3::MobilityModel::GetDistanceFrom(ns3::Ptr<const ns3::MobilityModel> position) const [member function]
    cls.add_method('GetDistanceFrom', 
                   'double', 
                   [param('ns3::Ptr< ns3::MobilityModel const >', 'position')], 
                   is_const=True)
    ## mobility-model.h (module 'mobility'): ns3::Vector ns3::MobilityModel::GetPosition() const [member function]
    cls.add_method('GetPosition', 
                   'ns3::Vector', 
                   [], 
                   is_const=True)
    ## mobility-model.h (module 'mobility'): double ns3::MobilityModel::GetRelativeSpeed(ns3::Ptr<const ns3::MobilityModel> other) const [member function]
    cls.add_method('GetRelativeSpeed', 
                   'double', 
                   [param('ns3::Ptr< ns3::MobilityModel const >', 'other')], 
                   is_const=True)
    ## mobility-model.h (module 'mobility'): static ns3::TypeId ns3::MobilityModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## mobility-model.h (module 'mobility'): ns3::Vector ns3::MobilityModel::GetVelocity() const [member function]
    cls.add_method('GetVelocity', 
                   'ns3::Vector', 
                   [], 
                   is_const=True)
    ## mobility-model.h (module 'mobility'): void ns3::MobilityModel::SetPosition(ns3::Vector const & position) [member function]
    cls.add_method('SetPosition', 
                   'void', 
                   [param('ns3::Vector const &', 'position')])
    ## mobility-model.h (module 'mobility'): void ns3::MobilityModel::NotifyCourseChange() const [member function]
    cls.add_method('NotifyCourseChange', 
                   'void', 
                   [], 
                   is_const=True, visibility='protected')
    ## mobility-model.h (module 'mobility'): int64_t ns3::MobilityModel::DoAssignStreams(int64_t start) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'start')], 
                   visibility='private', is_virtual=True)
    ## mobility-model.h (module 'mobility'): ns3::Vector ns3::MobilityModel::DoGetPosition() const [member function]
    cls.add_method('DoGetPosition', 
                   'ns3::Vector', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    ## mobility-model.h (module 'mobility'): ns3::Vector ns3::MobilityModel::DoGetVelocity() const [member function]
    cls.add_method('DoGetVelocity', 
                   'ns3::Vector', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    ## mobility-model.h (module 'mobility'): void ns3::MobilityModel::DoSetPosition(ns3::Vector const & position) [member function]
    cls.add_method('DoSetPosition', 
                   'void', 
                   [param('ns3::Vector const &', 'position')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    return

def register_Ns3NakagamiPropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h (module 'propagation'): static ns3::TypeId ns3::NakagamiPropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h (module 'propagation'): ns3::NakagamiPropagationLossModel::NakagamiPropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h (module 'propagation'): double ns3::NakagamiPropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    ## propagation-loss-model.h (module 'propagation'): int64_t ns3::NakagamiPropagationLossModel::DoAssignStreams(int64_t stream) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3NetDevice_methods(root_module, cls):
    ## net-device.h (module 'network'): ns3::NetDevice::NetDevice() [constructor]
    cls.add_constructor([])
    ## net-device.h (module 'network'): ns3::NetDevice::NetDevice(ns3::NetDevice const & arg0) [constructor]
    cls.add_constructor([param('ns3::NetDevice const &', 'arg0')])
    ## net-device.h (module 'network'): void ns3::NetDevice::AddLinkChangeCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('AddLinkChangeCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Address ns3::NetDevice::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Address', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Address ns3::NetDevice::GetBroadcast() const [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Address', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Ptr<ns3::Channel> ns3::NetDevice::GetChannel() const [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::Channel >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): uint32_t ns3::NetDevice::GetIfIndex() const [member function]
    cls.add_method('GetIfIndex', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): uint16_t ns3::NetDevice::GetMtu() const [member function]
    cls.add_method('GetMtu', 
                   'uint16_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Address ns3::NetDevice::GetMulticast(ns3::Ipv4Address multicastGroup) const [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv4Address', 'multicastGroup')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Address ns3::NetDevice::GetMulticast(ns3::Ipv6Address addr) const [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv6Address', 'addr')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Ptr<ns3::Node> ns3::NetDevice::GetNode() const [member function]
    cls.add_method('GetNode', 
                   'ns3::Ptr< ns3::Node >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): static ns3::TypeId ns3::NetDevice::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsBridge() const [member function]
    cls.add_method('IsBridge', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsLinkUp() const [member function]
    cls.add_method('IsLinkUp', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsMulticast() const [member function]
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsPointToPoint() const [member function]
    cls.add_method('IsPointToPoint', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::NeedsArp() const [member function]
    cls.add_method('NeedsArp', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::Send(ns3::Ptr<ns3::Packet> packet, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('Send', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::SendFrom(ns3::Ptr<ns3::Packet> packet, ns3::Address const & source, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('SendFrom', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'source'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetAddress(ns3::Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Address', 'address')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetIfIndex(uint32_t const index) [member function]
    cls.add_method('SetIfIndex', 
                   'void', 
                   [param('uint32_t const', 'index')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::SetMtu(uint16_t const mtu) [member function]
    cls.add_method('SetMtu', 
                   'bool', 
                   [param('uint16_t const', 'mtu')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetPromiscReceiveCallback(ns3::NetDevice::PromiscReceiveCallback cb) [member function]
    cls.add_method('SetPromiscReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetReceiveCallback(ns3::NetDevice::ReceiveCallback cb) [member function]
    cls.add_method('SetReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3NewChannelAns_methods(root_module, cls):
    ## new-channel-ans.h (module 'lora'): ns3::NewChannelAns::NewChannelAns(ns3::NewChannelAns const & arg0) [constructor]
    cls.add_constructor([param('ns3::NewChannelAns const &', 'arg0')])
    ## new-channel-ans.h (module 'lora'): ns3::NewChannelAns::NewChannelAns() [constructor]
    cls.add_constructor([])
    ## new-channel-ans.h (module 'lora'): ns3::NewChannelAns::NewChannelAns(bool datarateOk, bool freqOk) [constructor]
    cls.add_constructor([param('bool', 'datarateOk'), param('bool', 'freqOk')])
    ## new-channel-ans.h (module 'lora'): uint32_t ns3::NewChannelAns::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## new-channel-ans.h (module 'lora'): void ns3::NewChannelAns::Execute(ns3::Ptr<ns3::LoRaNetworkApplication> netDevice, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetworkApplication >', 'netDevice'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## new-channel-ans.h (module 'lora'): bool ns3::NewChannelAns::GetDatarateOk() [member function]
    cls.add_method('GetDatarateOk', 
                   'bool', 
                   [])
    ## new-channel-ans.h (module 'lora'): bool ns3::NewChannelAns::GetFreqOk() [member function]
    cls.add_method('GetFreqOk', 
                   'bool', 
                   [])
    ## new-channel-ans.h (module 'lora'): ns3::TypeId ns3::NewChannelAns::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## new-channel-ans.h (module 'lora'): std::string ns3::NewChannelAns::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## new-channel-ans.h (module 'lora'): uint32_t ns3::NewChannelAns::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## new-channel-ans.h (module 'lora'): static ns3::TypeId ns3::NewChannelAns::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## new-channel-ans.h (module 'lora'): void ns3::NewChannelAns::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## new-channel-ans.h (module 'lora'): void ns3::NewChannelAns::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## new-channel-ans.h (module 'lora'): void ns3::NewChannelAns::SetDatarateOk(bool drOk) [member function]
    cls.add_method('SetDatarateOk', 
                   'void', 
                   [param('bool', 'drOk')])
    ## new-channel-ans.h (module 'lora'): void ns3::NewChannelAns::SetFreqOk(bool freqOk) [member function]
    cls.add_method('SetFreqOk', 
                   'void', 
                   [param('bool', 'freqOk')])
    return

def register_Ns3NewChannelReq_methods(root_module, cls):
    ## new-channel-req.h (module 'lora'): ns3::NewChannelReq::NewChannelReq(ns3::NewChannelReq const & arg0) [constructor]
    cls.add_constructor([param('ns3::NewChannelReq const &', 'arg0')])
    ## new-channel-req.h (module 'lora'): ns3::NewChannelReq::NewChannelReq() [constructor]
    cls.add_constructor([])
    ## new-channel-req.h (module 'lora'): ns3::NewChannelReq::NewChannelReq(uint8_t chIndex, uint32_t freq, uint8_t minDr, uint8_t maxDr) [constructor]
    cls.add_constructor([param('uint8_t', 'chIndex'), param('uint32_t', 'freq'), param('uint8_t', 'minDr'), param('uint8_t', 'maxDr')])
    ## new-channel-req.h (module 'lora'): uint32_t ns3::NewChannelReq::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## new-channel-req.h (module 'lora'): void ns3::NewChannelReq::Execute(ns3::Ptr<ns3::LoRaNetDevice> netDevice, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetDevice >', 'netDevice'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## new-channel-req.h (module 'lora'): ns3::TypeId ns3::NewChannelReq::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## new-channel-req.h (module 'lora'): std::string ns3::NewChannelReq::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## new-channel-req.h (module 'lora'): uint32_t ns3::NewChannelReq::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## new-channel-req.h (module 'lora'): static ns3::TypeId ns3::NewChannelReq::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## new-channel-req.h (module 'lora'): void ns3::NewChannelReq::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## new-channel-req.h (module 'lora'): void ns3::NewChannelReq::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3NixVector_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## nix-vector.h (module 'network'): ns3::NixVector::NixVector() [constructor]
    cls.add_constructor([])
    ## nix-vector.h (module 'network'): ns3::NixVector::NixVector(ns3::NixVector const & o) [constructor]
    cls.add_constructor([param('ns3::NixVector const &', 'o')])
    ## nix-vector.h (module 'network'): void ns3::NixVector::AddNeighborIndex(uint32_t newBits, uint32_t numberOfBits) [member function]
    cls.add_method('AddNeighborIndex', 
                   'void', 
                   [param('uint32_t', 'newBits'), param('uint32_t', 'numberOfBits')])
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::BitCount(uint32_t numberOfNeighbors) const [member function]
    cls.add_method('BitCount', 
                   'uint32_t', 
                   [param('uint32_t', 'numberOfNeighbors')], 
                   is_const=True)
    ## nix-vector.h (module 'network'): ns3::Ptr<ns3::NixVector> ns3::NixVector::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::NixVector >', 
                   [], 
                   is_const=True)
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::Deserialize(uint32_t const * buffer, uint32_t size) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('uint32_t const *', 'buffer'), param('uint32_t', 'size')])
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::ExtractNeighborIndex(uint32_t numberOfBits) [member function]
    cls.add_method('ExtractNeighborIndex', 
                   'uint32_t', 
                   [param('uint32_t', 'numberOfBits')])
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::GetRemainingBits() [member function]
    cls.add_method('GetRemainingBits', 
                   'uint32_t', 
                   [])
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::Serialize(uint32_t * buffer, uint32_t maxSize) const [member function]
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint32_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    return

def register_Ns3Node_methods(root_module, cls):
    ## node.h (module 'network'): ns3::Node::Node(ns3::Node const & arg0) [constructor]
    cls.add_constructor([param('ns3::Node const &', 'arg0')])
    ## node.h (module 'network'): ns3::Node::Node() [constructor]
    cls.add_constructor([])
    ## node.h (module 'network'): ns3::Node::Node(uint32_t systemId) [constructor]
    cls.add_constructor([param('uint32_t', 'systemId')])
    ## node.h (module 'network'): uint32_t ns3::Node::AddApplication(ns3::Ptr<ns3::Application> application) [member function]
    cls.add_method('AddApplication', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::Application >', 'application')])
    ## node.h (module 'network'): uint32_t ns3::Node::AddDevice(ns3::Ptr<ns3::NetDevice> device) [member function]
    cls.add_method('AddDevice', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device')])
    ## node.h (module 'network'): static bool ns3::Node::ChecksumEnabled() [member function]
    cls.add_method('ChecksumEnabled', 
                   'bool', 
                   [], 
                   is_static=True)
    ## node.h (module 'network'): ns3::Ptr<ns3::Application> ns3::Node::GetApplication(uint32_t index) const [member function]
    cls.add_method('GetApplication', 
                   'ns3::Ptr< ns3::Application >', 
                   [param('uint32_t', 'index')], 
                   is_const=True)
    ## node.h (module 'network'): ns3::Ptr<ns3::NetDevice> ns3::Node::GetDevice(uint32_t index) const [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'index')], 
                   is_const=True)
    ## node.h (module 'network'): uint32_t ns3::Node::GetId() const [member function]
    cls.add_method('GetId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## node.h (module 'network'): ns3::Time ns3::Node::GetLocalTime() const [member function]
    cls.add_method('GetLocalTime', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## node.h (module 'network'): uint32_t ns3::Node::GetNApplications() const [member function]
    cls.add_method('GetNApplications', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## node.h (module 'network'): uint32_t ns3::Node::GetNDevices() const [member function]
    cls.add_method('GetNDevices', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## node.h (module 'network'): uint32_t ns3::Node::GetSystemId() const [member function]
    cls.add_method('GetSystemId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## node.h (module 'network'): static ns3::TypeId ns3::Node::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## node.h (module 'network'): void ns3::Node::RegisterDeviceAdditionListener(ns3::Node::DeviceAdditionListener listener) [member function]
    cls.add_method('RegisterDeviceAdditionListener', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'listener')])
    ## node.h (module 'network'): void ns3::Node::RegisterProtocolHandler(ns3::Node::ProtocolHandler handler, uint16_t protocolType, ns3::Ptr<ns3::NetDevice> device, bool promiscuous=false) [member function]
    cls.add_method('RegisterProtocolHandler', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'handler'), param('uint16_t', 'protocolType'), param('ns3::Ptr< ns3::NetDevice >', 'device'), param('bool', 'promiscuous', default_value='false')])
    ## node.h (module 'network'): void ns3::Node::UnregisterDeviceAdditionListener(ns3::Node::DeviceAdditionListener listener) [member function]
    cls.add_method('UnregisterDeviceAdditionListener', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'listener')])
    ## node.h (module 'network'): void ns3::Node::UnregisterProtocolHandler(ns3::Node::ProtocolHandler handler) [member function]
    cls.add_method('UnregisterProtocolHandler', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'handler')])
    ## node.h (module 'network'): void ns3::Node::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## node.h (module 'network'): void ns3::Node::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3NormalRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): ns3::NormalRandomVariable::INFINITE_VALUE [variable]
    cls.add_static_attribute('INFINITE_VALUE', 'double const', is_const=True)
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::NormalRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::NormalRandomVariable::NormalRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetMean() const [member function]
    cls.add_method('GetMean', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetVariance() const [member function]
    cls.add_method('GetVariance', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetBound() const [member function]
    cls.add_method('GetBound', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetValue(double mean, double variance, double bound=ns3::NormalRandomVariable::INFINITE_VALUE) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mean'), param('double', 'variance'), param('double', 'bound', default_value='ns3::NormalRandomVariable::INFINITE_VALUE')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::NormalRandomVariable::GetInteger(uint32_t mean, uint32_t variance, uint32_t bound) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mean'), param('uint32_t', 'variance'), param('uint32_t', 'bound')])
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::NormalRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3ObjectFactoryChecker_methods(root_module, cls):
    ## object-factory.h (module 'core'): ns3::ObjectFactoryChecker::ObjectFactoryChecker() [constructor]
    cls.add_constructor([])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryChecker::ObjectFactoryChecker(ns3::ObjectFactoryChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::ObjectFactoryChecker const &', 'arg0')])
    return

def register_Ns3ObjectFactoryValue_methods(root_module, cls):
    ## object-factory.h (module 'core'): ns3::ObjectFactoryValue::ObjectFactoryValue() [constructor]
    cls.add_constructor([])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryValue::ObjectFactoryValue(ns3::ObjectFactory const & value) [constructor]
    cls.add_constructor([param('ns3::ObjectFactory const &', 'value')])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryValue::ObjectFactoryValue(ns3::ObjectFactoryValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::ObjectFactoryValue const &', 'arg0')])
    ## object-factory.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::ObjectFactoryValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## object-factory.h (module 'core'): bool ns3::ObjectFactoryValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## object-factory.h (module 'core'): ns3::ObjectFactory ns3::ObjectFactoryValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::ObjectFactory', 
                   [], 
                   is_const=True)
    ## object-factory.h (module 'core'): std::string ns3::ObjectFactoryValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## object-factory.h (module 'core'): void ns3::ObjectFactoryValue::Set(ns3::ObjectFactory const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::ObjectFactory const &', 'value')])
    return

def register_Ns3OutputStreamWrapper_methods(root_module, cls):
    ## output-stream-wrapper.h (module 'network'): ns3::OutputStreamWrapper::OutputStreamWrapper(ns3::OutputStreamWrapper const & arg0) [constructor]
    cls.add_constructor([param('ns3::OutputStreamWrapper const &', 'arg0')])
    ## output-stream-wrapper.h (module 'network'): ns3::OutputStreamWrapper::OutputStreamWrapper(std::string filename, std::ios_base::openmode filemode) [constructor]
    cls.add_constructor([param('std::string', 'filename'), param('std::ios_base::openmode', 'filemode')])
    ## output-stream-wrapper.h (module 'network'): ns3::OutputStreamWrapper::OutputStreamWrapper(std::ostream * os) [constructor]
    cls.add_constructor([param('std::ostream *', 'os')])
    ## output-stream-wrapper.h (module 'network'): std::ostream * ns3::OutputStreamWrapper::GetStream() [member function]
    cls.add_method('GetStream', 
                   'std::ostream *', 
                   [])
    return

def register_Ns3Packet_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## packet.h (module 'network'): ns3::Packet::Packet() [constructor]
    cls.add_constructor([])
    ## packet.h (module 'network'): ns3::Packet::Packet(ns3::Packet const & o) [constructor]
    cls.add_constructor([param('ns3::Packet const &', 'o')])
    ## packet.h (module 'network'): ns3::Packet::Packet(uint32_t size) [constructor]
    cls.add_constructor([param('uint32_t', 'size')])
    ## packet.h (module 'network'): ns3::Packet::Packet(uint8_t const * buffer, uint32_t size, bool magic) [constructor]
    cls.add_constructor([param('uint8_t const *', 'buffer'), param('uint32_t', 'size'), param('bool', 'magic')])
    ## packet.h (module 'network'): ns3::Packet::Packet(uint8_t const * buffer, uint32_t size) [constructor]
    cls.add_constructor([param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## packet.h (module 'network'): void ns3::Packet::AddAtEnd(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## packet.h (module 'network'): void ns3::Packet::AddByteTag(ns3::Tag const & tag) const [member function]
    cls.add_method('AddByteTag', 
                   'void', 
                   [param('ns3::Tag const &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::AddHeader(ns3::Header const & header) [member function]
    cls.add_method('AddHeader', 
                   'void', 
                   [param('ns3::Header const &', 'header')])
    ## packet.h (module 'network'): void ns3::Packet::AddPacketTag(ns3::Tag const & tag) const [member function]
    cls.add_method('AddPacketTag', 
                   'void', 
                   [param('ns3::Tag const &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::AddPaddingAtEnd(uint32_t size) [member function]
    cls.add_method('AddPaddingAtEnd', 
                   'void', 
                   [param('uint32_t', 'size')])
    ## packet.h (module 'network'): void ns3::Packet::AddTrailer(ns3::Trailer const & trailer) [member function]
    cls.add_method('AddTrailer', 
                   'void', 
                   [param('ns3::Trailer const &', 'trailer')])
    ## packet.h (module 'network'): ns3::PacketMetadata::ItemIterator ns3::Packet::BeginItem() const [member function]
    cls.add_method('BeginItem', 
                   'ns3::PacketMetadata::ItemIterator', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::Ptr<ns3::Packet> ns3::Packet::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::Packet >', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::CopyData(uint8_t * buffer, uint32_t size) const [member function]
    cls.add_method('CopyData', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::CopyData(std::ostream * os, uint32_t size) const [member function]
    cls.add_method('CopyData', 
                   'void', 
                   [param('std::ostream *', 'os'), param('uint32_t', 'size')], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::Ptr<ns3::Packet> ns3::Packet::CreateFragment(uint32_t start, uint32_t length) const [member function]
    cls.add_method('CreateFragment', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('uint32_t', 'start'), param('uint32_t', 'length')], 
                   is_const=True)
    ## packet.h (module 'network'): static void ns3::Packet::EnableChecking() [member function]
    cls.add_method('EnableChecking', 
                   'void', 
                   [], 
                   is_static=True)
    ## packet.h (module 'network'): static void ns3::Packet::EnablePrinting() [member function]
    cls.add_method('EnablePrinting', 
                   'void', 
                   [], 
                   is_static=True)
    ## packet.h (module 'network'): bool ns3::Packet::FindFirstMatchingByteTag(ns3::Tag & tag) const [member function]
    cls.add_method('FindFirstMatchingByteTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::ByteTagIterator ns3::Packet::GetByteTagIterator() const [member function]
    cls.add_method('GetByteTagIterator', 
                   'ns3::ByteTagIterator', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::Ptr<ns3::NixVector> ns3::Packet::GetNixVector() const [member function]
    cls.add_method('GetNixVector', 
                   'ns3::Ptr< ns3::NixVector >', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::PacketTagIterator ns3::Packet::GetPacketTagIterator() const [member function]
    cls.add_method('GetPacketTagIterator', 
                   'ns3::PacketTagIterator', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint64_t ns3::Packet::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::PeekHeader(ns3::Header & header) const [member function]
    cls.add_method('PeekHeader', 
                   'uint32_t', 
                   [param('ns3::Header &', 'header')], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::PeekHeader(ns3::Header & header, uint32_t size) const [member function]
    cls.add_method('PeekHeader', 
                   'uint32_t', 
                   [param('ns3::Header &', 'header'), param('uint32_t', 'size')], 
                   is_const=True)
    ## packet.h (module 'network'): bool ns3::Packet::PeekPacketTag(ns3::Tag & tag) const [member function]
    cls.add_method('PeekPacketTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::PeekTrailer(ns3::Trailer & trailer) [member function]
    cls.add_method('PeekTrailer', 
                   'uint32_t', 
                   [param('ns3::Trailer &', 'trailer')])
    ## packet.h (module 'network'): void ns3::Packet::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::PrintByteTags(std::ostream & os) const [member function]
    cls.add_method('PrintByteTags', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::PrintPacketTags(std::ostream & os) const [member function]
    cls.add_method('PrintPacketTags', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::RemoveAllByteTags() [member function]
    cls.add_method('RemoveAllByteTags', 
                   'void', 
                   [])
    ## packet.h (module 'network'): void ns3::Packet::RemoveAllPacketTags() [member function]
    cls.add_method('RemoveAllPacketTags', 
                   'void', 
                   [])
    ## packet.h (module 'network'): void ns3::Packet::RemoveAtEnd(uint32_t size) [member function]
    cls.add_method('RemoveAtEnd', 
                   'void', 
                   [param('uint32_t', 'size')])
    ## packet.h (module 'network'): void ns3::Packet::RemoveAtStart(uint32_t size) [member function]
    cls.add_method('RemoveAtStart', 
                   'void', 
                   [param('uint32_t', 'size')])
    ## packet.h (module 'network'): uint32_t ns3::Packet::RemoveHeader(ns3::Header & header) [member function]
    cls.add_method('RemoveHeader', 
                   'uint32_t', 
                   [param('ns3::Header &', 'header')])
    ## packet.h (module 'network'): uint32_t ns3::Packet::RemoveHeader(ns3::Header & header, uint32_t size) [member function]
    cls.add_method('RemoveHeader', 
                   'uint32_t', 
                   [param('ns3::Header &', 'header'), param('uint32_t', 'size')])
    ## packet.h (module 'network'): bool ns3::Packet::RemovePacketTag(ns3::Tag & tag) [member function]
    cls.add_method('RemovePacketTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    ## packet.h (module 'network'): uint32_t ns3::Packet::RemoveTrailer(ns3::Trailer & trailer) [member function]
    cls.add_method('RemoveTrailer', 
                   'uint32_t', 
                   [param('ns3::Trailer &', 'trailer')])
    ## packet.h (module 'network'): bool ns3::Packet::ReplacePacketTag(ns3::Tag & tag) [member function]
    cls.add_method('ReplacePacketTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    ## packet.h (module 'network'): uint32_t ns3::Packet::Serialize(uint8_t * buffer, uint32_t maxSize) const [member function]
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::SetNixVector(ns3::Ptr<ns3::NixVector> nixVector) [member function]
    cls.add_method('SetNixVector', 
                   'void', 
                   [param('ns3::Ptr< ns3::NixVector >', 'nixVector')])
    ## packet.h (module 'network'): std::string ns3::Packet::ToString() const [member function]
    cls.add_method('ToString', 
                   'std::string', 
                   [], 
                   is_const=True)
    return

def register_Ns3ParetoRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ParetoRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ParetoRandomVariable::ParetoRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetMean() const [member function]
    cls.add_method('GetMean', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetScale() const [member function]
    cls.add_method('GetScale', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetShape() const [member function]
    cls.add_method('GetShape', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetBound() const [member function]
    cls.add_method('GetBound', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetValue(double scale, double shape, double bound) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'scale'), param('double', 'shape'), param('double', 'bound')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ParetoRandomVariable::GetInteger(uint32_t scale, uint32_t shape, uint32_t bound) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'scale'), param('uint32_t', 'shape'), param('uint32_t', 'bound')])
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ParetoRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3QueueItem_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## queue-item.h (module 'network'): ns3::QueueItem::QueueItem(ns3::Ptr<ns3::Packet> p) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::Packet >', 'p')])
    ## queue-item.h (module 'network'): ns3::Ptr<ns3::Packet> ns3::QueueItem::GetPacket() const [member function]
    cls.add_method('GetPacket', 
                   'ns3::Ptr< ns3::Packet >', 
                   [], 
                   is_const=True)
    ## queue-item.h (module 'network'): uint32_t ns3::QueueItem::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## queue-item.h (module 'network'): bool ns3::QueueItem::GetUint8Value(ns3::QueueItem::Uint8Values field, uint8_t & value) const [member function]
    cls.add_method('GetUint8Value', 
                   'bool', 
                   [param('ns3::QueueItem::Uint8Values', 'field'), param('uint8_t &', 'value')], 
                   is_const=True, is_virtual=True)
    ## queue-item.h (module 'network'): void ns3::QueueItem::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3RxParamSetupAns_methods(root_module, cls):
    ## rx-param-setup-ans.h (module 'lora'): ns3::RxParamSetupAns::RxParamSetupAns(ns3::RxParamSetupAns const & arg0) [constructor]
    cls.add_constructor([param('ns3::RxParamSetupAns const &', 'arg0')])
    ## rx-param-setup-ans.h (module 'lora'): ns3::RxParamSetupAns::RxParamSetupAns() [constructor]
    cls.add_constructor([])
    ## rx-param-setup-ans.h (module 'lora'): ns3::RxParamSetupAns::RxParamSetupAns(bool offset, bool dr, bool channel) [constructor]
    cls.add_constructor([param('bool', 'offset'), param('bool', 'dr'), param('bool', 'channel')])
    ## rx-param-setup-ans.h (module 'lora'): uint32_t ns3::RxParamSetupAns::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## rx-param-setup-ans.h (module 'lora'): void ns3::RxParamSetupAns::Execute(ns3::Ptr<ns3::LoRaNetworkApplication> netDevice, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetworkApplication >', 'netDevice'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## rx-param-setup-ans.h (module 'lora'): bool ns3::RxParamSetupAns::GetChannelAck() [member function]
    cls.add_method('GetChannelAck', 
                   'bool', 
                   [])
    ## rx-param-setup-ans.h (module 'lora'): bool ns3::RxParamSetupAns::GetDrAck() [member function]
    cls.add_method('GetDrAck', 
                   'bool', 
                   [])
    ## rx-param-setup-ans.h (module 'lora'): ns3::TypeId ns3::RxParamSetupAns::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## rx-param-setup-ans.h (module 'lora'): std::string ns3::RxParamSetupAns::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## rx-param-setup-ans.h (module 'lora'): bool ns3::RxParamSetupAns::GetOffsetAck() [member function]
    cls.add_method('GetOffsetAck', 
                   'bool', 
                   [])
    ## rx-param-setup-ans.h (module 'lora'): uint32_t ns3::RxParamSetupAns::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## rx-param-setup-ans.h (module 'lora'): static ns3::TypeId ns3::RxParamSetupAns::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## rx-param-setup-ans.h (module 'lora'): void ns3::RxParamSetupAns::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## rx-param-setup-ans.h (module 'lora'): void ns3::RxParamSetupAns::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## rx-param-setup-ans.h (module 'lora'): void ns3::RxParamSetupAns::SetChannelAck(bool ack) [member function]
    cls.add_method('SetChannelAck', 
                   'void', 
                   [param('bool', 'ack')])
    ## rx-param-setup-ans.h (module 'lora'): void ns3::RxParamSetupAns::SetDrAck(bool ack) [member function]
    cls.add_method('SetDrAck', 
                   'void', 
                   [param('bool', 'ack')])
    ## rx-param-setup-ans.h (module 'lora'): void ns3::RxParamSetupAns::SetOffsetAck(bool ack) [member function]
    cls.add_method('SetOffsetAck', 
                   'void', 
                   [param('bool', 'ack')])
    return

def register_Ns3RxParamSetupReq_methods(root_module, cls):
    ## rx-param-setup-req.h (module 'lora'): ns3::RxParamSetupReq::RxParamSetupReq(ns3::RxParamSetupReq const & arg0) [constructor]
    cls.add_constructor([param('ns3::RxParamSetupReq const &', 'arg0')])
    ## rx-param-setup-req.h (module 'lora'): ns3::RxParamSetupReq::RxParamSetupReq() [constructor]
    cls.add_constructor([])
    ## rx-param-setup-req.h (module 'lora'): ns3::RxParamSetupReq::RxParamSetupReq(uint8_t rx1Offset, uint8_t rx2Dr, uint32_t rx2Freq) [constructor]
    cls.add_constructor([param('uint8_t', 'rx1Offset'), param('uint8_t', 'rx2Dr'), param('uint32_t', 'rx2Freq')])
    ## rx-param-setup-req.h (module 'lora'): uint32_t ns3::RxParamSetupReq::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## rx-param-setup-req.h (module 'lora'): void ns3::RxParamSetupReq::Execute(ns3::Ptr<ns3::LoRaNetDevice> netDevice, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetDevice >', 'netDevice'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## rx-param-setup-req.h (module 'lora'): ns3::TypeId ns3::RxParamSetupReq::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## rx-param-setup-req.h (module 'lora'): std::string ns3::RxParamSetupReq::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## rx-param-setup-req.h (module 'lora'): uint8_t ns3::RxParamSetupReq::GetRx1Offset() [member function]
    cls.add_method('GetRx1Offset', 
                   'uint8_t', 
                   [])
    ## rx-param-setup-req.h (module 'lora'): uint8_t ns3::RxParamSetupReq::GetRx2Dr() [member function]
    cls.add_method('GetRx2Dr', 
                   'uint8_t', 
                   [])
    ## rx-param-setup-req.h (module 'lora'): uint32_t ns3::RxParamSetupReq::GetRx2Freq() [member function]
    cls.add_method('GetRx2Freq', 
                   'uint32_t', 
                   [])
    ## rx-param-setup-req.h (module 'lora'): uint32_t ns3::RxParamSetupReq::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## rx-param-setup-req.h (module 'lora'): static ns3::TypeId ns3::RxParamSetupReq::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## rx-param-setup-req.h (module 'lora'): void ns3::RxParamSetupReq::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## rx-param-setup-req.h (module 'lora'): void ns3::RxParamSetupReq::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## rx-param-setup-req.h (module 'lora'): void ns3::RxParamSetupReq::SetRx1Offset(uint8_t rx1Offset) [member function]
    cls.add_method('SetRx1Offset', 
                   'void', 
                   [param('uint8_t', 'rx1Offset')])
    ## rx-param-setup-req.h (module 'lora'): void ns3::RxParamSetupReq::SetRx2Dr(uint8_t rx2Dr) [member function]
    cls.add_method('SetRx2Dr', 
                   'void', 
                   [param('uint8_t', 'rx2Dr')])
    ## rx-param-setup-req.h (module 'lora'): void ns3::RxParamSetupReq::SetRx2Freq(uint32_t rx2Freq) [member function]
    cls.add_method('SetRx2Freq', 
                   'void', 
                   [param('uint32_t', 'rx2Freq')])
    return

def register_Ns3RxTimingSetupAns_methods(root_module, cls):
    ## rx-timing-setup-ans.h (module 'lora'): ns3::RxTimingSetupAns::RxTimingSetupAns(ns3::RxTimingSetupAns const & arg0) [constructor]
    cls.add_constructor([param('ns3::RxTimingSetupAns const &', 'arg0')])
    ## rx-timing-setup-ans.h (module 'lora'): ns3::RxTimingSetupAns::RxTimingSetupAns() [constructor]
    cls.add_constructor([])
    ## rx-timing-setup-ans.h (module 'lora'): uint32_t ns3::RxTimingSetupAns::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## rx-timing-setup-ans.h (module 'lora'): void ns3::RxTimingSetupAns::Execute(ns3::Ptr<ns3::LoRaNetworkApplication> netDevice, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetworkApplication >', 'netDevice'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## rx-timing-setup-ans.h (module 'lora'): ns3::TypeId ns3::RxTimingSetupAns::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## rx-timing-setup-ans.h (module 'lora'): std::string ns3::RxTimingSetupAns::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## rx-timing-setup-ans.h (module 'lora'): uint32_t ns3::RxTimingSetupAns::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## rx-timing-setup-ans.h (module 'lora'): static ns3::TypeId ns3::RxTimingSetupAns::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## rx-timing-setup-ans.h (module 'lora'): void ns3::RxTimingSetupAns::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## rx-timing-setup-ans.h (module 'lora'): void ns3::RxTimingSetupAns::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3RxTimingSetupReq_methods(root_module, cls):
    ## rx-timing-setup-req.h (module 'lora'): ns3::RxTimingSetupReq::RxTimingSetupReq(ns3::RxTimingSetupReq const & arg0) [constructor]
    cls.add_constructor([param('ns3::RxTimingSetupReq const &', 'arg0')])
    ## rx-timing-setup-req.h (module 'lora'): ns3::RxTimingSetupReq::RxTimingSetupReq() [constructor]
    cls.add_constructor([])
    ## rx-timing-setup-req.h (module 'lora'): ns3::RxTimingSetupReq::RxTimingSetupReq(uint8_t del) [constructor]
    cls.add_constructor([param('uint8_t', 'del')])
    ## rx-timing-setup-req.h (module 'lora'): uint32_t ns3::RxTimingSetupReq::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## rx-timing-setup-req.h (module 'lora'): void ns3::RxTimingSetupReq::Execute(ns3::Ptr<ns3::LoRaNetDevice> netDevice, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetDevice >', 'netDevice'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## rx-timing-setup-req.h (module 'lora'): uint8_t ns3::RxTimingSetupReq::GetDelay() [member function]
    cls.add_method('GetDelay', 
                   'uint8_t', 
                   [])
    ## rx-timing-setup-req.h (module 'lora'): ns3::TypeId ns3::RxTimingSetupReq::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## rx-timing-setup-req.h (module 'lora'): std::string ns3::RxTimingSetupReq::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## rx-timing-setup-req.h (module 'lora'): uint32_t ns3::RxTimingSetupReq::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## rx-timing-setup-req.h (module 'lora'): static ns3::TypeId ns3::RxTimingSetupReq::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## rx-timing-setup-req.h (module 'lora'): void ns3::RxTimingSetupReq::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## rx-timing-setup-req.h (module 'lora'): void ns3::RxTimingSetupReq::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## rx-timing-setup-req.h (module 'lora'): void ns3::RxTimingSetupReq::SetDelay(uint8_t del) [member function]
    cls.add_method('SetDelay', 
                   'void', 
                   [param('uint8_t', 'del')])
    return

def register_Ns3SpectrumChannel_methods(root_module, cls):
    ## spectrum-channel.h (module 'spectrum'): ns3::SpectrumChannel::SpectrumChannel(ns3::SpectrumChannel const & arg0) [constructor]
    cls.add_constructor([param('ns3::SpectrumChannel const &', 'arg0')])
    ## spectrum-channel.h (module 'spectrum'): ns3::SpectrumChannel::SpectrumChannel() [constructor]
    cls.add_constructor([])
    ## spectrum-channel.h (module 'spectrum'): void ns3::SpectrumChannel::AddPropagationLossModel(ns3::Ptr<ns3::PropagationLossModel> loss) [member function]
    cls.add_method('AddPropagationLossModel', 
                   'void', 
                   [param('ns3::Ptr< ns3::PropagationLossModel >', 'loss')])
    ## spectrum-channel.h (module 'spectrum'): void ns3::SpectrumChannel::AddRx(ns3::Ptr<ns3::SpectrumPhy> phy) [member function]
    cls.add_method('AddRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumPhy >', 'phy')], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-channel.h (module 'spectrum'): void ns3::SpectrumChannel::AddSpectrumPropagationLossModel(ns3::Ptr<ns3::SpectrumPropagationLossModel> loss) [member function]
    cls.add_method('AddSpectrumPropagationLossModel', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumPropagationLossModel >', 'loss')])
    ## spectrum-channel.h (module 'spectrum'): void ns3::SpectrumChannel::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## spectrum-channel.h (module 'spectrum'): ns3::Ptr<ns3::SpectrumPropagationLossModel> ns3::SpectrumChannel::GetSpectrumPropagationLossModel() [member function]
    cls.add_method('GetSpectrumPropagationLossModel', 
                   'ns3::Ptr< ns3::SpectrumPropagationLossModel >', 
                   [])
    ## spectrum-channel.h (module 'spectrum'): static ns3::TypeId ns3::SpectrumChannel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## spectrum-channel.h (module 'spectrum'): void ns3::SpectrumChannel::SetPropagationDelayModel(ns3::Ptr<ns3::PropagationDelayModel> delay) [member function]
    cls.add_method('SetPropagationDelayModel', 
                   'void', 
                   [param('ns3::Ptr< ns3::PropagationDelayModel >', 'delay')])
    ## spectrum-channel.h (module 'spectrum'): void ns3::SpectrumChannel::StartTx(ns3::Ptr<ns3::SpectrumSignalParameters> params) [member function]
    cls.add_method('StartTx', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumSignalParameters >', 'params')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3TimeValue_methods(root_module, cls):
    ## nstime.h (module 'core'): ns3::TimeValue::TimeValue() [constructor]
    cls.add_constructor([])
    ## nstime.h (module 'core'): ns3::TimeValue::TimeValue(ns3::Time const & value) [constructor]
    cls.add_constructor([param('ns3::Time const &', 'value')])
    ## nstime.h (module 'core'): ns3::TimeValue::TimeValue(ns3::TimeValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::TimeValue const &', 'arg0')])
    ## nstime.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::TimeValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nstime.h (module 'core'): bool ns3::TimeValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## nstime.h (module 'core'): ns3::Time ns3::TimeValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): std::string ns3::TimeValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## nstime.h (module 'core'): void ns3::TimeValue::Set(ns3::Time const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Time const &', 'value')])
    return

def register_Ns3TypeIdChecker_methods(root_module, cls):
    ## type-id.h (module 'core'): ns3::TypeIdChecker::TypeIdChecker() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeIdChecker::TypeIdChecker(ns3::TypeIdChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::TypeIdChecker const &', 'arg0')])
    return

def register_Ns3TypeIdValue_methods(root_module, cls):
    ## type-id.h (module 'core'): ns3::TypeIdValue::TypeIdValue() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeIdValue::TypeIdValue(ns3::TypeId const & value) [constructor]
    cls.add_constructor([param('ns3::TypeId const &', 'value')])
    ## type-id.h (module 'core'): ns3::TypeIdValue::TypeIdValue(ns3::TypeIdValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::TypeIdValue const &', 'arg0')])
    ## type-id.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::TypeIdValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## type-id.h (module 'core'): bool ns3::TypeIdValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeIdValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): std::string ns3::TypeIdValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## type-id.h (module 'core'): void ns3::TypeIdValue::Set(ns3::TypeId const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::TypeId const &', 'value')])
    return

def register_Ns3UintegerValue_methods(root_module, cls):
    ## uinteger.h (module 'core'): ns3::UintegerValue::UintegerValue() [constructor]
    cls.add_constructor([])
    ## uinteger.h (module 'core'): ns3::UintegerValue::UintegerValue(uint64_t const & value) [constructor]
    cls.add_constructor([param('uint64_t const &', 'value')])
    ## uinteger.h (module 'core'): ns3::UintegerValue::UintegerValue(ns3::UintegerValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::UintegerValue const &', 'arg0')])
    ## uinteger.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::UintegerValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## uinteger.h (module 'core'): bool ns3::UintegerValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## uinteger.h (module 'core'): uint64_t ns3::UintegerValue::Get() const [member function]
    cls.add_method('Get', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## uinteger.h (module 'core'): std::string ns3::UintegerValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## uinteger.h (module 'core'): void ns3::UintegerValue::Set(uint64_t const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('uint64_t const &', 'value')])
    return

def register_Ns3Vector2DChecker_methods(root_module, cls):
    ## vector.h (module 'core'): ns3::Vector2DChecker::Vector2DChecker() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector2DChecker::Vector2DChecker(ns3::Vector2DChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::Vector2DChecker const &', 'arg0')])
    return

def register_Ns3Vector2DValue_methods(root_module, cls):
    ## vector.h (module 'core'): ns3::Vector2DValue::Vector2DValue() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector2DValue::Vector2DValue(ns3::Vector2D const & value) [constructor]
    cls.add_constructor([param('ns3::Vector2D const &', 'value')])
    ## vector.h (module 'core'): ns3::Vector2DValue::Vector2DValue(ns3::Vector2DValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::Vector2DValue const &', 'arg0')])
    ## vector.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::Vector2DValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## vector.h (module 'core'): bool ns3::Vector2DValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## vector.h (module 'core'): ns3::Vector2D ns3::Vector2DValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Vector2D', 
                   [], 
                   is_const=True)
    ## vector.h (module 'core'): std::string ns3::Vector2DValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## vector.h (module 'core'): void ns3::Vector2DValue::Set(ns3::Vector2D const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Vector2D const &', 'value')])
    return

def register_Ns3Vector3DChecker_methods(root_module, cls):
    ## vector.h (module 'core'): ns3::Vector3DChecker::Vector3DChecker() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector3DChecker::Vector3DChecker(ns3::Vector3DChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::Vector3DChecker const &', 'arg0')])
    return

def register_Ns3Vector3DValue_methods(root_module, cls):
    ## vector.h (module 'core'): ns3::Vector3DValue::Vector3DValue() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector3DValue::Vector3DValue(ns3::Vector3D const & value) [constructor]
    cls.add_constructor([param('ns3::Vector3D const &', 'value')])
    ## vector.h (module 'core'): ns3::Vector3DValue::Vector3DValue(ns3::Vector3DValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::Vector3DValue const &', 'arg0')])
    ## vector.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::Vector3DValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## vector.h (module 'core'): bool ns3::Vector3DValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## vector.h (module 'core'): ns3::Vector3D ns3::Vector3DValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Vector3D', 
                   [], 
                   is_const=True)
    ## vector.h (module 'core'): std::string ns3::Vector3DValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## vector.h (module 'core'): void ns3::Vector3DValue::Set(ns3::Vector3D const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Vector3D const &', 'value')])
    return

def register_Ns3AddressChecker_methods(root_module, cls):
    ## address.h (module 'network'): ns3::AddressChecker::AddressChecker() [constructor]
    cls.add_constructor([])
    ## address.h (module 'network'): ns3::AddressChecker::AddressChecker(ns3::AddressChecker const & arg0) [constructor]
    cls.add_constructor([param('ns3::AddressChecker const &', 'arg0')])
    return

def register_Ns3AddressValue_methods(root_module, cls):
    ## address.h (module 'network'): ns3::AddressValue::AddressValue() [constructor]
    cls.add_constructor([])
    ## address.h (module 'network'): ns3::AddressValue::AddressValue(ns3::Address const & value) [constructor]
    cls.add_constructor([param('ns3::Address const &', 'value')])
    ## address.h (module 'network'): ns3::AddressValue::AddressValue(ns3::AddressValue const & arg0) [constructor]
    cls.add_constructor([param('ns3::AddressValue const &', 'arg0')])
    ## address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::AddressValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## address.h (module 'network'): bool ns3::AddressValue::DeserializeFromString(std::string value, ns3::Ptr<const ns3::AttributeChecker> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## address.h (module 'network'): ns3::Address ns3::AddressValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Address', 
                   [], 
                   is_const=True)
    ## address.h (module 'network'): std::string ns3::AddressValue::SerializeToString(ns3::Ptr<const ns3::AttributeChecker> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## address.h (module 'network'): void ns3::AddressValue::Set(ns3::Address const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Address const &', 'value')])
    return

def register_Ns3CallbackImpl__Bool_Ns3Ptr__lt__ns3NetDevice__gt___Ns3Ptr__lt__const_ns3Packet__gt___Unsigned_short_Const_ns3Address___amp___Const_ns3Address___amp___Ns3NetDevicePacketType_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): bool ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty>::operator()(ns3::Ptr<ns3::NetDevice> arg0, ns3::Ptr<const ns3::Packet> arg1, short unsigned int arg2, ns3::Address const & arg3, ns3::Address const & arg4, ns3::NetDevice::PacketType arg5) [member operator]
    cls.add_method('operator()', 
                   'bool', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'arg0'), param('ns3::Ptr< ns3::Packet const >', 'arg1'), param('short unsigned int', 'arg2'), param('ns3::Address const &', 'arg3'), param('ns3::Address const &', 'arg4'), param('ns3::NetDevice::PacketType', 'arg5')], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Bool_Ns3Ptr__lt__ns3NetDevice__gt___Ns3Ptr__lt__const_ns3Packet__gt___Unsigned_short_Const_ns3Address___amp___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): bool ns3::CallbackImpl<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::operator()(ns3::Ptr<ns3::NetDevice> arg0, ns3::Ptr<const ns3::Packet> arg1, short unsigned int arg2, ns3::Address const & arg3) [member operator]
    cls.add_method('operator()', 
                   'bool', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'arg0'), param('ns3::Ptr< ns3::Packet const >', 'arg1'), param('short unsigned int', 'arg2'), param('ns3::Address const &', 'arg3')], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Bool_Ns3Ptr__lt__ns3Packet__gt___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<bool, ns3::Ptr<ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<bool, ns3::Ptr<ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<bool, ns3::Ptr<ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< bool, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<bool, ns3::Ptr<ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<bool, ns3::Ptr<ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): bool ns3::CallbackImpl<bool, ns3::Ptr<ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::operator()(ns3::Ptr<ns3::Packet> arg0) [member operator]
    cls.add_method('operator()', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'arg0')], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Ns3ObjectBase___star___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): ns3::ObjectBase * ns3::CallbackImpl<ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::operator()() [member operator]
    cls.add_method('operator()', 
                   'ns3::ObjectBase *', 
                   [], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Void_Double_Double_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<void, double, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, double, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<void, double, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< void, double, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<void, double, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<void, double, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackImpl<void, double, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::operator()(double arg0, double arg1) [member operator]
    cls.add_method('operator()', 
                   'void', 
                   [param('double', 'arg0'), param('double', 'arg1')], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Void_Ns3LoRaPhyState_Ns3LoRaPhyState_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::LoRaPhy::State, ns3::LoRaPhy::State, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::LoRaPhy::State, ns3::LoRaPhy::State, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<void, ns3::LoRaPhy::State, ns3::LoRaPhy::State, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< void, ns3::LoRaPhy::State, ns3::LoRaPhy::State, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<void, ns3::LoRaPhy::State, ns3::LoRaPhy::State, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<void, ns3::LoRaPhy::State, ns3::LoRaPhy::State, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackImpl<void, ns3::LoRaPhy::State, ns3::LoRaPhy::State, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::operator()(ns3::LoRaPhy::State arg0, ns3::LoRaPhy::State arg1) [member operator]
    cls.add_method('operator()', 
                   'void', 
                   [param('ns3::LoRaPhy::State', 'arg0'), param('ns3::LoRaPhy::State', 'arg1')], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Void_Ns3Ptr__lt__const_ns3MobilityModel__gt___Ns3Ptr__lt__const_ns3MobilityModel__gt___Double_Double_Double_Double_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::Ptr<const ns3::MobilityModel>, double, double, double, double, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::Ptr<const ns3::MobilityModel>, double, double, double, double, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::Ptr<const ns3::MobilityModel>, double, double, double, double, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< void, ns3::Ptr< ns3::MobilityModel const >, ns3::Ptr< ns3::MobilityModel const >, double, double, double, double, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::Ptr<const ns3::MobilityModel>, double, double, double, double, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::Ptr<const ns3::MobilityModel>, double, double, double, double, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::Ptr<const ns3::MobilityModel>, double, double, double, double, ns3::empty, ns3::empty, ns3::empty>::operator()(ns3::Ptr<const ns3::MobilityModel> arg0, ns3::Ptr<const ns3::MobilityModel> arg1, double arg2, double arg3, double arg4, double arg5) [member operator]
    cls.add_method('operator()', 
                   'void', 
                   [param('ns3::Ptr< ns3::MobilityModel const >', 'arg0'), param('ns3::Ptr< ns3::MobilityModel const >', 'arg1'), param('double', 'arg2'), param('double', 'arg3'), param('double', 'arg4'), param('double', 'arg5')], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Void_Ns3Ptr__lt__const_ns3MobilityModel__gt___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< void, ns3::Ptr< ns3::MobilityModel const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackImpl<void, ns3::Ptr<const ns3::MobilityModel>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::operator()(ns3::Ptr<const ns3::MobilityModel> arg0) [member operator]
    cls.add_method('operator()', 
                   'void', 
                   [param('ns3::Ptr< ns3::MobilityModel const >', 'arg0')], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Void_Ns3Ptr__lt__const_ns3Packet__gt___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<const ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<const ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<void, ns3::Ptr<const ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< void, ns3::Ptr< ns3::Packet const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<void, ns3::Ptr<const ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<void, ns3::Ptr<const ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackImpl<void, ns3::Ptr<const ns3::Packet>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::operator()(ns3::Ptr<const ns3::Packet> arg0) [member operator]
    cls.add_method('operator()', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'arg0')], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Void_Ns3Ptr__lt__const_ns3SpectrumPhy__gt___Ns3Ptr__lt__const_ns3SpectrumPhy__gt___Double_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<const ns3::SpectrumPhy>, ns3::Ptr<const ns3::SpectrumPhy>, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<const ns3::SpectrumPhy>, ns3::Ptr<const ns3::SpectrumPhy>, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<void, ns3::Ptr<const ns3::SpectrumPhy>, ns3::Ptr<const ns3::SpectrumPhy>, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< void, ns3::Ptr< ns3::SpectrumPhy const >, ns3::Ptr< ns3::SpectrumPhy const >, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<void, ns3::Ptr<const ns3::SpectrumPhy>, ns3::Ptr<const ns3::SpectrumPhy>, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<void, ns3::Ptr<const ns3::SpectrumPhy>, ns3::Ptr<const ns3::SpectrumPhy>, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackImpl<void, ns3::Ptr<const ns3::SpectrumPhy>, ns3::Ptr<const ns3::SpectrumPhy>, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::operator()(ns3::Ptr<const ns3::SpectrumPhy> arg0, ns3::Ptr<const ns3::SpectrumPhy> arg1, double arg2) [member operator]
    cls.add_method('operator()', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumPhy const >', 'arg0'), param('ns3::Ptr< ns3::SpectrumPhy const >', 'arg1'), param('double', 'arg2')], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Void_Ns3Ptr__lt__ns3NetDevice__gt___Ns3Ptr__lt__const_ns3Packet__gt___Unsigned_short_Const_ns3Address___amp___Const_ns3Address___amp___Ns3NetDevicePacketType_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< void, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<const ns3::Packet>, unsigned short, const ns3::Address &, const ns3::Address &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty>::operator()(ns3::Ptr<ns3::NetDevice> arg0, ns3::Ptr<const ns3::Packet> arg1, short unsigned int arg2, ns3::Address const & arg3, ns3::Address const & arg4, ns3::NetDevice::PacketType arg5) [member operator]
    cls.add_method('operator()', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'arg0'), param('ns3::Ptr< ns3::Packet const >', 'arg1'), param('short unsigned int', 'arg2'), param('ns3::Address const &', 'arg3'), param('ns3::Address const &', 'arg4'), param('ns3::NetDevice::PacketType', 'arg5')], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Void_Ns3Ptr__lt__ns3NetDevice__gt___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< void, ns3::Ptr< ns3::NetDevice >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackImpl<void, ns3::Ptr<ns3::NetDevice>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::operator()(ns3::Ptr<ns3::NetDevice> arg0) [member operator]
    cls.add_method('operator()', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'arg0')], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Void_Ns3Ptr__lt__ns3SpectrumSignalParameters__gt___Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<ns3::SpectrumSignalParameters>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::Ptr<ns3::SpectrumSignalParameters>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<void, ns3::Ptr<ns3::SpectrumSignalParameters>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< void, ns3::Ptr< ns3::SpectrumSignalParameters >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<void, ns3::Ptr<ns3::SpectrumSignalParameters>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<void, ns3::Ptr<ns3::SpectrumSignalParameters>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackImpl<void, ns3::Ptr<ns3::SpectrumSignalParameters>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::operator()(ns3::Ptr<ns3::SpectrumSignalParameters> arg0) [member operator]
    cls.add_method('operator()', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumSignalParameters >', 'arg0')], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Void_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackImpl<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty>::operator()() [member operator]
    cls.add_method('operator()', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3CallbackImpl__Void_StdBasic_string__lt__char__gt___StdBasic_string__lt__char__gt___Bool_Double_Double_Double_Ns3Empty_Ns3Empty_Ns3Empty_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImpl<void, std::basic_string<char>, std::basic_string<char>, bool, double, double, double, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImpl<void, std::basic_string<char>, std::basic_string<char>, bool, double, double, double, ns3::empty, ns3::empty, ns3::empty>::CallbackImpl(ns3::CallbackImpl<void, std::basic_string<char>, std::basic_string<char>, bool, double, double, double, ns3::empty, ns3::empty, ns3::empty> const & arg0) [constructor]
    cls.add_constructor([param('ns3::CallbackImpl< void, std::basic_string< char >, std::basic_string< char >, bool, double, double, double, ns3::empty, ns3::empty, ns3::empty > const &', 'arg0')])
    ## callback.h (module 'core'): static std::string ns3::CallbackImpl<void, std::basic_string<char>, std::basic_string<char>, bool, double, double, double, ns3::empty, ns3::empty, ns3::empty>::DoGetTypeid() [member function]
    cls.add_method('DoGetTypeid', 
                   'std::string', 
                   [], 
                   is_static=True)
    ## callback.h (module 'core'): std::string ns3::CallbackImpl<void, std::basic_string<char>, std::basic_string<char>, bool, double, double, double, ns3::empty, ns3::empty, ns3::empty>::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackImpl<void, std::basic_string<char>, std::basic_string<char>, bool, double, double, double, ns3::empty, ns3::empty, ns3::empty>::operator()(std::basic_string<char, std::char_traits<char>, std::allocator<char> > arg0, std::basic_string<char, std::char_traits<char>, std::allocator<char> > arg1, bool arg2, double arg3, double arg4, double arg5) [member operator]
    cls.add_method('operator()', 
                   'void', 
                   [param('std::string', 'arg0'), param('std::string', 'arg1'), param('bool', 'arg2'), param('double', 'arg3'), param('double', 'arg4'), param('double', 'arg5')], 
                   is_pure_virtual=True, is_virtual=True, custom_name=u'__call__')
    return

def register_Ns3DevStatusAns_methods(root_module, cls):
    ## dev-status-ans.h (module 'lora'): ns3::DevStatusAns::DevStatusAns(ns3::DevStatusAns const & arg0) [constructor]
    cls.add_constructor([param('ns3::DevStatusAns const &', 'arg0')])
    ## dev-status-ans.h (module 'lora'): ns3::DevStatusAns::DevStatusAns() [constructor]
    cls.add_constructor([])
    ## dev-status-ans.h (module 'lora'): ns3::DevStatusAns::DevStatusAns(uint8_t battery, int8_t margin) [constructor]
    cls.add_constructor([param('uint8_t', 'battery'), param('int8_t', 'margin')])
    ## dev-status-ans.h (module 'lora'): uint32_t ns3::DevStatusAns::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## dev-status-ans.h (module 'lora'): void ns3::DevStatusAns::Execute(ns3::Ptr<ns3::LoRaNetworkApplication> app, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetworkApplication >', 'app'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## dev-status-ans.h (module 'lora'): uint8_t ns3::DevStatusAns::GetBattery() [member function]
    cls.add_method('GetBattery', 
                   'uint8_t', 
                   [])
    ## dev-status-ans.h (module 'lora'): ns3::TypeId ns3::DevStatusAns::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## dev-status-ans.h (module 'lora'): int8_t ns3::DevStatusAns::GetMargin() [member function]
    cls.add_method('GetMargin', 
                   'int8_t', 
                   [])
    ## dev-status-ans.h (module 'lora'): std::string ns3::DevStatusAns::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## dev-status-ans.h (module 'lora'): uint32_t ns3::DevStatusAns::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## dev-status-ans.h (module 'lora'): static ns3::TypeId ns3::DevStatusAns::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## dev-status-ans.h (module 'lora'): void ns3::DevStatusAns::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## dev-status-ans.h (module 'lora'): void ns3::DevStatusAns::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## dev-status-ans.h (module 'lora'): void ns3::DevStatusAns::SetBattery(uint8_t battery) [member function]
    cls.add_method('SetBattery', 
                   'void', 
                   [param('uint8_t', 'battery')])
    ## dev-status-ans.h (module 'lora'): void ns3::DevStatusAns::SetMargin(int8_t margin) [member function]
    cls.add_method('SetMargin', 
                   'void', 
                   [param('int8_t', 'margin')])
    return

def register_Ns3DevStatusReq_methods(root_module, cls):
    ## dev-status-req.h (module 'lora'): ns3::DevStatusReq::DevStatusReq(ns3::DevStatusReq const & arg0) [constructor]
    cls.add_constructor([param('ns3::DevStatusReq const &', 'arg0')])
    ## dev-status-req.h (module 'lora'): ns3::DevStatusReq::DevStatusReq() [constructor]
    cls.add_constructor([])
    ## dev-status-req.h (module 'lora'): uint32_t ns3::DevStatusReq::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## dev-status-req.h (module 'lora'): void ns3::DevStatusReq::Execute(ns3::Ptr<ns3::LoRaNetDevice> netDevice, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetDevice >', 'netDevice'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## dev-status-req.h (module 'lora'): ns3::TypeId ns3::DevStatusReq::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## dev-status-req.h (module 'lora'): std::string ns3::DevStatusReq::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## dev-status-req.h (module 'lora'): uint32_t ns3::DevStatusReq::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## dev-status-req.h (module 'lora'): static ns3::TypeId ns3::DevStatusReq::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## dev-status-req.h (module 'lora'): void ns3::DevStatusReq::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## dev-status-req.h (module 'lora'): void ns3::DevStatusReq::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3DutyCycleAns_methods(root_module, cls):
    ## duty-cycle-ans.h (module 'lora'): ns3::DutyCycleAns::DutyCycleAns(ns3::DutyCycleAns const & arg0) [constructor]
    cls.add_constructor([param('ns3::DutyCycleAns const &', 'arg0')])
    ## duty-cycle-ans.h (module 'lora'): ns3::DutyCycleAns::DutyCycleAns() [constructor]
    cls.add_constructor([])
    ## duty-cycle-ans.h (module 'lora'): uint32_t ns3::DutyCycleAns::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## duty-cycle-ans.h (module 'lora'): void ns3::DutyCycleAns::Execute(ns3::Ptr<ns3::LoRaNetworkApplication> app, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetworkApplication >', 'app'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## duty-cycle-ans.h (module 'lora'): ns3::TypeId ns3::DutyCycleAns::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## duty-cycle-ans.h (module 'lora'): std::string ns3::DutyCycleAns::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## duty-cycle-ans.h (module 'lora'): uint32_t ns3::DutyCycleAns::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## duty-cycle-ans.h (module 'lora'): static ns3::TypeId ns3::DutyCycleAns::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## duty-cycle-ans.h (module 'lora'): void ns3::DutyCycleAns::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## duty-cycle-ans.h (module 'lora'): void ns3::DutyCycleAns::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3DutyCycleReq_methods(root_module, cls):
    ## duty-cycle-req.h (module 'lora'): ns3::DutyCycleReq::DutyCycleReq(ns3::DutyCycleReq const & arg0) [constructor]
    cls.add_constructor([param('ns3::DutyCycleReq const &', 'arg0')])
    ## duty-cycle-req.h (module 'lora'): ns3::DutyCycleReq::DutyCycleReq() [constructor]
    cls.add_constructor([])
    ## duty-cycle-req.h (module 'lora'): ns3::DutyCycleReq::DutyCycleReq(uint8_t dutyCycle) [constructor]
    cls.add_constructor([param('uint8_t', 'dutyCycle')])
    ## duty-cycle-req.h (module 'lora'): uint32_t ns3::DutyCycleReq::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## duty-cycle-req.h (module 'lora'): void ns3::DutyCycleReq::Execute(ns3::Ptr<ns3::LoRaNetDevice> netDevice, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetDevice >', 'netDevice'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## duty-cycle-req.h (module 'lora'): uint8_t ns3::DutyCycleReq::GetDutyCycle() [member function]
    cls.add_method('GetDutyCycle', 
                   'uint8_t', 
                   [])
    ## duty-cycle-req.h (module 'lora'): ns3::TypeId ns3::DutyCycleReq::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## duty-cycle-req.h (module 'lora'): std::string ns3::DutyCycleReq::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## duty-cycle-req.h (module 'lora'): uint32_t ns3::DutyCycleReq::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## duty-cycle-req.h (module 'lora'): static ns3::TypeId ns3::DutyCycleReq::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## duty-cycle-req.h (module 'lora'): void ns3::DutyCycleReq::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## duty-cycle-req.h (module 'lora'): void ns3::DutyCycleReq::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## duty-cycle-req.h (module 'lora'): void ns3::DutyCycleReq::SetDutyCycle(uint8_t dutyCycle) [member function]
    cls.add_method('SetDutyCycle', 
                   'void', 
                   [param('uint8_t', 'dutyCycle')])
    return

def register_Ns3LinkAdrAns_methods(root_module, cls):
    ## link-adr-ans.h (module 'lora'): ns3::LinkAdrAns::LinkAdrAns(ns3::LinkAdrAns const & arg0) [constructor]
    cls.add_constructor([param('ns3::LinkAdrAns const &', 'arg0')])
    ## link-adr-ans.h (module 'lora'): ns3::LinkAdrAns::LinkAdrAns() [constructor]
    cls.add_constructor([])
    ## link-adr-ans.h (module 'lora'): ns3::LinkAdrAns::LinkAdrAns(bool datarate, bool power, bool channelmask) [constructor]
    cls.add_constructor([param('bool', 'datarate'), param('bool', 'power'), param('bool', 'channelmask')])
    ## link-adr-ans.h (module 'lora'): bool ns3::LinkAdrAns::ChannelMaskSet() [member function]
    cls.add_method('ChannelMaskSet', 
                   'bool', 
                   [])
    ## link-adr-ans.h (module 'lora'): bool ns3::LinkAdrAns::DatarateSet() [member function]
    cls.add_method('DatarateSet', 
                   'bool', 
                   [])
    ## link-adr-ans.h (module 'lora'): uint32_t ns3::LinkAdrAns::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## link-adr-ans.h (module 'lora'): void ns3::LinkAdrAns::Execute(ns3::Ptr<ns3::LoRaNetworkApplication> app, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetworkApplication >', 'app'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## link-adr-ans.h (module 'lora'): ns3::TypeId ns3::LinkAdrAns::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## link-adr-ans.h (module 'lora'): std::string ns3::LinkAdrAns::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## link-adr-ans.h (module 'lora'): uint32_t ns3::LinkAdrAns::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## link-adr-ans.h (module 'lora'): static ns3::TypeId ns3::LinkAdrAns::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## link-adr-ans.h (module 'lora'): bool ns3::LinkAdrAns::PowerSet() [member function]
    cls.add_method('PowerSet', 
                   'bool', 
                   [])
    ## link-adr-ans.h (module 'lora'): void ns3::LinkAdrAns::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## link-adr-ans.h (module 'lora'): void ns3::LinkAdrAns::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## link-adr-ans.h (module 'lora'): void ns3::LinkAdrAns::SetChannelMask(bool channelmask) [member function]
    cls.add_method('SetChannelMask', 
                   'void', 
                   [param('bool', 'channelmask')])
    ## link-adr-ans.h (module 'lora'): void ns3::LinkAdrAns::SetDatarate(bool datarate) [member function]
    cls.add_method('SetDatarate', 
                   'void', 
                   [param('bool', 'datarate')])
    ## link-adr-ans.h (module 'lora'): void ns3::LinkAdrAns::SetPower(bool power) [member function]
    cls.add_method('SetPower', 
                   'void', 
                   [param('bool', 'power')])
    return

def register_Ns3LinkAdrReq_methods(root_module, cls):
    ## link-adr-req.h (module 'lora'): ns3::LinkAdrReq::LinkAdrReq(ns3::LinkAdrReq const & arg0) [constructor]
    cls.add_constructor([param('ns3::LinkAdrReq const &', 'arg0')])
    ## link-adr-req.h (module 'lora'): ns3::LinkAdrReq::LinkAdrReq() [constructor]
    cls.add_constructor([])
    ## link-adr-req.h (module 'lora'): ns3::LinkAdrReq::LinkAdrReq(uint8_t dataRate, uint8_t power, uint16_t channelMask, uint8_t repetitions) [constructor]
    cls.add_constructor([param('uint8_t', 'dataRate'), param('uint8_t', 'power'), param('uint16_t', 'channelMask'), param('uint8_t', 'repetitions')])
    ## link-adr-req.h (module 'lora'): uint32_t ns3::LinkAdrReq::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## link-adr-req.h (module 'lora'): void ns3::LinkAdrReq::Execute(ns3::Ptr<ns3::LoRaNetDevice> netDevice, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetDevice >', 'netDevice'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## link-adr-req.h (module 'lora'): uint16_t ns3::LinkAdrReq::GetChannelMask() [member function]
    cls.add_method('GetChannelMask', 
                   'uint16_t', 
                   [])
    ## link-adr-req.h (module 'lora'): uint8_t ns3::LinkAdrReq::GetDataRate() [member function]
    cls.add_method('GetDataRate', 
                   'uint8_t', 
                   [])
    ## link-adr-req.h (module 'lora'): ns3::TypeId ns3::LinkAdrReq::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## link-adr-req.h (module 'lora'): std::string ns3::LinkAdrReq::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## link-adr-req.h (module 'lora'): uint8_t ns3::LinkAdrReq::GetPower() [member function]
    cls.add_method('GetPower', 
                   'uint8_t', 
                   [])
    ## link-adr-req.h (module 'lora'): uint8_t ns3::LinkAdrReq::GetRepetitions() [member function]
    cls.add_method('GetRepetitions', 
                   'uint8_t', 
                   [])
    ## link-adr-req.h (module 'lora'): uint32_t ns3::LinkAdrReq::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## link-adr-req.h (module 'lora'): static ns3::TypeId ns3::LinkAdrReq::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## link-adr-req.h (module 'lora'): void ns3::LinkAdrReq::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## link-adr-req.h (module 'lora'): void ns3::LinkAdrReq::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## link-adr-req.h (module 'lora'): void ns3::LinkAdrReq::SetChannelMask(uint16_t channelMask) [member function]
    cls.add_method('SetChannelMask', 
                   'void', 
                   [param('uint16_t', 'channelMask')])
    ## link-adr-req.h (module 'lora'): void ns3::LinkAdrReq::SetDataRate(uint8_t dataRate) [member function]
    cls.add_method('SetDataRate', 
                   'void', 
                   [param('uint8_t', 'dataRate')])
    ## link-adr-req.h (module 'lora'): void ns3::LinkAdrReq::SetPower(uint8_t power) [member function]
    cls.add_method('SetPower', 
                   'void', 
                   [param('uint8_t', 'power')])
    ## link-adr-req.h (module 'lora'): void ns3::LinkAdrReq::SetRepetitions(uint8_t repetitions) [member function]
    cls.add_method('SetRepetitions', 
                   'void', 
                   [param('uint8_t', 'repetitions')])
    return

def register_Ns3LinkCheckAns_methods(root_module, cls):
    ## link-check-ans.h (module 'lora'): ns3::LinkCheckAns::LinkCheckAns(ns3::LinkCheckAns const & arg0) [constructor]
    cls.add_constructor([param('ns3::LinkCheckAns const &', 'arg0')])
    ## link-check-ans.h (module 'lora'): ns3::LinkCheckAns::LinkCheckAns() [constructor]
    cls.add_constructor([])
    ## link-check-ans.h (module 'lora'): ns3::LinkCheckAns::LinkCheckAns(uint8_t margin, uint8_t count) [constructor]
    cls.add_constructor([param('uint8_t', 'margin'), param('uint8_t', 'count')])
    ## link-check-ans.h (module 'lora'): uint32_t ns3::LinkCheckAns::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## link-check-ans.h (module 'lora'): void ns3::LinkCheckAns::Execute(ns3::Ptr<ns3::LoRaNetDevice> netDevice, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetDevice >', 'netDevice'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## link-check-ans.h (module 'lora'): uint8_t ns3::LinkCheckAns::GetCount() [member function]
    cls.add_method('GetCount', 
                   'uint8_t', 
                   [])
    ## link-check-ans.h (module 'lora'): ns3::TypeId ns3::LinkCheckAns::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## link-check-ans.h (module 'lora'): uint8_t ns3::LinkCheckAns::GetMargin() [member function]
    cls.add_method('GetMargin', 
                   'uint8_t', 
                   [])
    ## link-check-ans.h (module 'lora'): std::string ns3::LinkCheckAns::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## link-check-ans.h (module 'lora'): uint32_t ns3::LinkCheckAns::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## link-check-ans.h (module 'lora'): static ns3::TypeId ns3::LinkCheckAns::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## link-check-ans.h (module 'lora'): void ns3::LinkCheckAns::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## link-check-ans.h (module 'lora'): void ns3::LinkCheckAns::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## link-check-ans.h (module 'lora'): void ns3::LinkCheckAns::SetCount(uint8_t count) [member function]
    cls.add_method('SetCount', 
                   'void', 
                   [param('uint8_t', 'count')])
    ## link-check-ans.h (module 'lora'): void ns3::LinkCheckAns::SetMargin(uint8_t margin) [member function]
    cls.add_method('SetMargin', 
                   'void', 
                   [param('uint8_t', 'margin')])
    return

def register_Ns3LinkCheckReq_methods(root_module, cls):
    ## link-check-req.h (module 'lora'): ns3::LinkCheckReq::LinkCheckReq(ns3::LinkCheckReq const & arg0) [constructor]
    cls.add_constructor([param('ns3::LinkCheckReq const &', 'arg0')])
    ## link-check-req.h (module 'lora'): ns3::LinkCheckReq::LinkCheckReq() [constructor]
    cls.add_constructor([])
    ## link-check-req.h (module 'lora'): uint32_t ns3::LinkCheckReq::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## link-check-req.h (module 'lora'): void ns3::LinkCheckReq::Execute(ns3::Ptr<ns3::LoRaNetworkApplication> app, ns3::Address address) [member function]
    cls.add_method('Execute', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaNetworkApplication >', 'app'), param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## link-check-req.h (module 'lora'): ns3::TypeId ns3::LinkCheckReq::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## link-check-req.h (module 'lora'): std::string ns3::LinkCheckReq::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## link-check-req.h (module 'lora'): uint32_t ns3::LinkCheckReq::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## link-check-req.h (module 'lora'): static ns3::TypeId ns3::LinkCheckReq::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## link-check-req.h (module 'lora'): void ns3::LinkCheckReq::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## link-check-req.h (module 'lora'): void ns3::LinkCheckReq::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3LoRaGwPhy_methods(root_module, cls):
    ## lora-gw-phy.h (module 'lora'): ns3::LoRaGwPhy::LoRaGwPhy() [constructor]
    cls.add_constructor([])
    ## lora-gw-phy.h (module 'lora'): void ns3::LoRaGwPhy::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lora-gw-phy.h (module 'lora'): static ns3::TypeId ns3::LoRaGwPhy::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-gw-phy.h (module 'lora'): uint32_t ns3::LoRaGwPhy::GetReceptions() [member function]
    cls.add_method('GetReceptions', 
                   'uint32_t', 
                   [])
    ## lora-gw-phy.h (module 'lora'): void ns3::LoRaGwPhy::StartRx(ns3::Ptr<ns3::SpectrumSignalParameters> params) [member function]
    cls.add_method('StartRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumSignalParameters >', 'params')], 
                   is_virtual=True)
    ## lora-gw-phy.h (module 'lora'): void ns3::LoRaGwPhy::EndRx(ns3::Ptr<ns3::LoRaSpectrumSignalParameters> params) [member function]
    cls.add_method('EndRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaSpectrumSignalParameters >', 'params')])
    ## lora-gw-phy.h (module 'lora'): bool ns3::LoRaGwPhy::StartTx(ns3::Ptr<ns3::Packet> packet) [member function]
    cls.add_method('StartTx', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet')])
    ## lora-gw-phy.h (module 'lora'): void ns3::LoRaGwPhy::SetReceptionEndCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, unsigned int, unsigned char, unsigned int, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetReceptionEndCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, unsigned int, unsigned char, unsigned int, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## lora-gw-phy.h (module 'lora'): uint32_t ns3::LoRaGwPhy::GetCollisions() [member function]
    cls.add_method('GetCollisions', 
                   'uint32_t', 
                   [])
    ## lora-gw-phy.h (module 'lora'): void ns3::LoRaGwPhy::UpdateBer() [member function]
    cls.add_method('UpdateBer', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3LoRaNetDevice_methods(root_module, cls):
    ## lora-net-device.h (module 'lora'): static ns3::TypeId ns3::LoRaNetDevice::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-net-device.h (module 'lora'): ns3::LoRaNetDevice::LoRaNetDevice() [constructor]
    cls.add_constructor([])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::SetQueue(ns3::Ptr<ns3::Queue<ns3::QueueItem> > queue) [member function]
    cls.add_method('SetQueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Queue< ns3::QueueItem > >', 'queue')], 
                   is_virtual=True)
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::NotifyTransmissionEnd(ns3::Ptr<const ns3::Packet> arg0) [member function]
    cls.add_method('NotifyTransmissionEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'arg0')])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::NotifyReceptionStart() [member function]
    cls.add_method('NotifyReceptionStart', 
                   'void', 
                   [])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::NotifyReceptionEndError() [member function]
    cls.add_method('NotifyReceptionEndError', 
                   'void', 
                   [])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::NotifyReceptionEndOk(ns3::Ptr<ns3::Packet> p, double rssi) [member function]
    cls.add_method('NotifyReceptionEndOk', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'p'), param('double', 'rssi')])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::SetChannel(ns3::Ptr<ns3::Channel> c) [member function]
    cls.add_method('SetChannel', 
                   'void', 
                   [param('ns3::Ptr< ns3::Channel >', 'c')])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::SetGenericPhyTxStartCallback(ns3::GenericPhyTxStartCallback c) [member function]
    cls.add_method('SetGenericPhyTxStartCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'c')])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::SetPhy(ns3::Ptr<ns3::LoRaPhy> phy) [member function]
    cls.add_method('SetPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaPhy >', 'phy')])
    ## lora-net-device.h (module 'lora'): ns3::Ptr<ns3::LoRaPhy> ns3::LoRaNetDevice::GetPhy() const [member function]
    cls.add_method('GetPhy', 
                   'ns3::Ptr< ns3::LoRaPhy >', 
                   [], 
                   is_const=True)
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::SetIfIndex(uint32_t const index) [member function]
    cls.add_method('SetIfIndex', 
                   'void', 
                   [param('uint32_t const', 'index')], 
                   is_virtual=True)
    ## lora-net-device.h (module 'lora'): uint32_t ns3::LoRaNetDevice::GetIfIndex() const [member function]
    cls.add_method('GetIfIndex', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): ns3::Ptr<ns3::Channel> ns3::LoRaNetDevice::GetChannel() const [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::Channel >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::SetMtu(uint16_t const mtu) [member function]
    cls.add_method('SetMtu', 
                   'bool', 
                   [param('uint16_t const', 'mtu')], 
                   is_virtual=True)
    ## lora-net-device.h (module 'lora'): uint16_t ns3::LoRaNetDevice::GetMtu() const [member function]
    cls.add_method('GetMtu', 
                   'uint16_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::SetAddress(ns3::Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## lora-net-device.h (module 'lora'): ns3::Address ns3::LoRaNetDevice::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::IsLinkUp() const [member function]
    cls.add_method('IsLinkUp', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::AddLinkChangeCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('AddLinkChangeCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): ns3::Address ns3::LoRaNetDevice::GetBroadcast() const [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::IsMulticast() const [member function]
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::IsPointToPoint() const [member function]
    cls.add_method('IsPointToPoint', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::IsBridge() const [member function]
    cls.add_method('IsBridge', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::Send(ns3::Ptr<ns3::Packet> packet, uint16_t protocolNumber) [member function]
    cls.add_method('Send', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('uint16_t', 'protocolNumber')], 
                   is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::Send(ns3::Ptr<ns3::Packet> packet, ns3::Address const & dest) [member function]
    cls.add_method('Send', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'dest')], 
                   is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::Send(ns3::Ptr<ns3::Packet> packet, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('Send', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::SendFrom(ns3::Ptr<ns3::Packet> packet, ns3::Address const & source, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('SendFrom', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'source'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_virtual=True)
    ## lora-net-device.h (module 'lora'): ns3::Ptr<ns3::Node> ns3::LoRaNetDevice::GetNode() const [member function]
    cls.add_method('GetNode', 
                   'ns3::Ptr< ns3::Node >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')], 
                   is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::NeedsArp() const [member function]
    cls.add_method('NeedsArp', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::SetReceiveCallback(ns3::NetDevice::ReceiveCallback cb) [member function]
    cls.add_method('SetReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_virtual=True)
    ## lora-net-device.h (module 'lora'): ns3::Address ns3::LoRaNetDevice::GetMulticast(ns3::Ipv4Address addr) const [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv4Address', 'addr')], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): ns3::Address ns3::LoRaNetDevice::GetMulticast(ns3::Ipv6Address addr) const [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv6Address', 'addr')], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::SetPromiscReceiveCallback(ns3::NetDevice::PromiscReceiveCallback cb) [member function]
    cls.add_method('SetPromiscReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::SetMaxPower(uint8_t power) [member function]
    cls.add_method('SetMaxPower', 
                   'bool', 
                   [param('uint8_t', 'power')])
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::SetMaxDataRate(uint8_t datarate) [member function]
    cls.add_method('SetMaxDataRate', 
                   'bool', 
                   [param('uint8_t', 'datarate')])
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::SetMaxDataRate(uint8_t datarate, uint8_t index) [member function]
    cls.add_method('SetMaxDataRate', 
                   'bool', 
                   [param('uint8_t', 'datarate'), param('uint8_t', 'index')])
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::SetMinDataRate(uint8_t datarate) [member function]
    cls.add_method('SetMinDataRate', 
                   'bool', 
                   [param('uint8_t', 'datarate')])
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::SetMinDataRate(uint8_t datarate, uint8_t index) [member function]
    cls.add_method('SetMinDataRate', 
                   'bool', 
                   [param('uint8_t', 'datarate'), param('uint8_t', 'index')])
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::SetDelay(uint8_t delay) [member function]
    cls.add_method('SetDelay', 
                   'bool', 
                   [param('uint8_t', 'delay')])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::SetReset(bool reset) [member function]
    cls.add_method('SetReset', 
                   'void', 
                   [param('bool', 'reset')])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::CheckCorrectReceiver(ns3::LoRaMacHeader header) [member function]
    cls.add_method('CheckCorrectReceiver', 
                   'void', 
                   [param('ns3::LoRaMacHeader', 'header')])
    ## lora-net-device.h (module 'lora'): double ns3::LoRaNetDevice::GetAvgRetransmissionCount() [member function]
    cls.add_method('GetAvgRetransmissionCount', 
                   'double', 
                   [])
    ## lora-net-device.h (module 'lora'): double ns3::LoRaNetDevice::GetAvgTime() [member function]
    cls.add_method('GetAvgTime', 
                   'double', 
                   [])
    ## lora-net-device.h (module 'lora'): uint32_t ns3::LoRaNetDevice::GetMissed() [member function]
    cls.add_method('GetMissed', 
                   'uint32_t', 
                   [])
    ## lora-net-device.h (module 'lora'): uint32_t ns3::LoRaNetDevice::GetArrived() [member function]
    cls.add_method('GetArrived', 
                   'uint32_t', 
                   [])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::SetNbRep(uint8_t repetitions) [member function]
    cls.add_method('SetNbRep', 
                   'void', 
                   [param('uint8_t', 'repetitions')])
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::SetChannelMask(uint16_t channelMask) [member function]
    cls.add_method('SetChannelMask', 
                   'bool', 
                   [param('uint16_t', 'channelMask')])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::SetMacAnswer(ns3::Ptr<ns3::LoRaMacCommand> command) [member function]
    cls.add_method('SetMacAnswer', 
                   'void', 
                   [param('ns3::Ptr< ns3::LoRaMacCommand >', 'command')])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::TryAgain() [member function]
    cls.add_method('TryAgain', 
                   'void', 
                   [])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::SetDutyCycle(uint8_t dutycycle) [member function]
    cls.add_method('SetDutyCycle', 
                   'void', 
                   [param('uint8_t', 'dutycycle')])
    ## lora-net-device.h (module 'lora'): uint8_t ns3::LoRaNetDevice::GetDutyCycle() [member function]
    cls.add_method('GetDutyCycle', 
                   'uint8_t', 
                   [])
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::SetRx2Settings(uint8_t datarate, uint32_t freq) [member function]
    cls.add_method('SetRx2Settings', 
                   'bool', 
                   [param('uint8_t', 'datarate'), param('uint32_t', 'freq')])
    ## lora-net-device.h (module 'lora'): uint32_t ns3::LoRaNetDevice::GetRx2Frequency() [member function]
    cls.add_method('GetRx2Frequency', 
                   'uint32_t', 
                   [])
    ## lora-net-device.h (module 'lora'): uint8_t ns3::LoRaNetDevice::GetRx2Datarate() [member function]
    cls.add_method('GetRx2Datarate', 
                   'uint8_t', 
                   [])
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::SetDlOffset(uint8_t offset) [member function]
    cls.add_method('SetDlOffset', 
                   'bool', 
                   [param('uint8_t', 'offset')])
    ## lora-net-device.h (module 'lora'): uint8_t ns3::LoRaNetDevice::GetDlOffset() [member function]
    cls.add_method('GetDlOffset', 
                   'uint8_t', 
                   [])
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::AddChannel(uint8_t index, uint32_t freq) [member function]
    cls.add_method('AddChannel', 
                   'bool', 
                   [param('uint8_t', 'index'), param('uint32_t', 'freq')])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::RemoveChannel(uint8_t index) [member function]
    cls.add_method('RemoveChannel', 
                   'void', 
                   [param('uint8_t', 'index')])
    ## lora-net-device.h (module 'lora'): ns3::LoRaNetDevice::LoRaNetDevice(ns3::LoRaNetDevice const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaNetDevice const &', 'arg0')])
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::StartTransmissionNoArgs() [member function]
    cls.add_method('StartTransmissionNoArgs', 
                   'void', 
                   [], 
                   visibility='protected')
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::DoTryAgain() [member function]
    cls.add_method('DoTryAgain', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-net-device.h (module 'lora'): uint8_t ns3::LoRaNetDevice::GetFreeChannel() [member function]
    cls.add_method('GetFreeChannel', 
                   'uint8_t', 
                   [], 
                   visibility='protected')
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::FreeChannel(uint8_t channelIndex) [member function]
    cls.add_method('FreeChannel', 
                   'void', 
                   [param('uint8_t', 'channelIndex')], 
                   visibility='protected')
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::PrepareReception(uint32_t bandwidth, uint32_t frequency, uint32_t spreading) [member function]
    cls.add_method('PrepareReception', 
                   'void', 
                   [param('uint32_t', 'bandwidth'), param('uint32_t', 'frequency'), param('uint32_t', 'spreading')], 
                   visibility='protected')
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::DoPrepareReception(uint32_t bandwidth, uint32_t frequency, uint32_t spreading) [member function]
    cls.add_method('DoPrepareReception', 
                   'void', 
                   [param('uint32_t', 'bandwidth'), param('uint32_t', 'frequency'), param('uint32_t', 'spreading')], 
                   visibility='protected', is_virtual=True)
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::CheckReception() [member function]
    cls.add_method('CheckReception', 
                   'void', 
                   [], 
                   visibility='protected')
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::DoCheckReception() [member function]
    cls.add_method('DoCheckReception', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::CheckReception2() [member function]
    cls.add_method('CheckReception2', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-net-device.h (module 'lora'): void ns3::LoRaNetDevice::DoCheckReception2() [member function]
    cls.add_method('DoCheckReception2', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-net-device.h (module 'lora'): bool ns3::LoRaNetDevice::StartTransmission(ns3::Ptr<ns3::Packet> packet, uint32_t frequency, uint8_t datarate, uint8_t powerIndex) [member function]
    cls.add_method('StartTransmission', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('uint32_t', 'frequency'), param('uint8_t', 'datarate'), param('uint8_t', 'powerIndex')], 
                   visibility='protected')
    ## lora-net-device.h (module 'lora'): uint8_t ns3::LoRaNetDevice::GetRxDatarate(uint8_t dr) [member function]
    cls.add_method('GetRxDatarate', 
                   'uint8_t', 
                   [param('uint8_t', 'dr')], 
                   visibility='protected')
    return

def register_Ns3LoRaRsNetDevice_methods(root_module, cls):
    ## lora-rs-net-device.h (module 'lora'): static ns3::TypeId ns3::LoRaRsNetDevice::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-rs-net-device.h (module 'lora'): ns3::LoRaRsNetDevice::LoRaRsNetDevice() [constructor]
    cls.add_constructor([])
    ## lora-rs-net-device.h (module 'lora'): void ns3::LoRaRsNetDevice::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lora-rs-net-device.h (module 'lora'): uint32_t ns3::LoRaRsNetDevice::GetOffset() [member function]
    cls.add_method('GetOffset', 
                   'uint32_t', 
                   [])
    ## lora-rs-net-device.h (module 'lora'): void ns3::LoRaRsNetDevice::SetOffset(uint32_t offset) [member function]
    cls.add_method('SetOffset', 
                   'void', 
                   [param('uint32_t', 'offset')])
    ## lora-rs-net-device.h (module 'lora'): void ns3::LoRaRsNetDevice::NotifyReceptionStart() [member function]
    cls.add_method('NotifyReceptionStart', 
                   'void', 
                   [])
    ## lora-rs-net-device.h (module 'lora'): void ns3::LoRaRsNetDevice::NotifyReceptionEndError() [member function]
    cls.add_method('NotifyReceptionEndError', 
                   'void', 
                   [])
    ## lora-rs-net-device.h (module 'lora'): void ns3::LoRaRsNetDevice::NotifyReceptionEndOk(ns3::Ptr<ns3::Packet> p, double snr) [member function]
    cls.add_method('NotifyReceptionEndOk', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'p'), param('double', 'snr')])
    ## lora-rs-net-device.h (module 'lora'): void ns3::LoRaRsNetDevice::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lora-rs-net-device.h (module 'lora'): bool ns3::LoRaRsNetDevice::SendFrom(ns3::Ptr<ns3::Packet> packet, ns3::Address const & source, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('SendFrom', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'source'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_virtual=True)
    ## lora-rs-net-device.h (module 'lora'): void ns3::LoRaRsNetDevice::SetReset(bool reset) [member function]
    cls.add_method('SetReset', 
                   'void', 
                   [param('bool', 'reset')])
    ## lora-rs-net-device.h (module 'lora'): ns3::LoRaRsNetDevice::LoRaRsNetDevice(ns3::LoRaRsNetDevice const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaRsNetDevice const &', 'arg0')])
    ## lora-rs-net-device.h (module 'lora'): uint8_t ns3::LoRaRsNetDevice::GetChannelNbFromFrequency(uint32_t frequency) [member function]
    cls.add_method('GetChannelNbFromFrequency', 
                   'uint8_t', 
                   [param('uint32_t', 'frequency')], 
                   visibility='protected')
    ## lora-rs-net-device.h (module 'lora'): void ns3::LoRaRsNetDevice::DoTryAgain() [member function]
    cls.add_method('DoTryAgain', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-rs-net-device.h (module 'lora'): void ns3::LoRaRsNetDevice::DoPrepareReception(uint32_t bandwidthSetting, uint32_t frequency, uint32_t spreadingfactor) [member function]
    cls.add_method('DoPrepareReception', 
                   'void', 
                   [param('uint32_t', 'bandwidthSetting'), param('uint32_t', 'frequency'), param('uint32_t', 'spreadingfactor')], 
                   visibility='private', is_virtual=True)
    ## lora-rs-net-device.h (module 'lora'): void ns3::LoRaRsNetDevice::DoCheckReception() [member function]
    cls.add_method('DoCheckReception', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## lora-rs-net-device.h (module 'lora'): void ns3::LoRaRsNetDevice::DoCheckReception2() [member function]
    cls.add_method('DoCheckReception2', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3QueueDiscItem_methods(root_module, cls):
    ## queue-item.h (module 'network'): ns3::QueueDiscItem::QueueDiscItem(ns3::Ptr<ns3::Packet> p, ns3::Address const & addr, uint16_t protocol) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::Packet >', 'p'), param('ns3::Address const &', 'addr'), param('uint16_t', 'protocol')])
    ## queue-item.h (module 'network'): ns3::Address ns3::QueueDiscItem::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Address', 
                   [], 
                   is_const=True)
    ## queue-item.h (module 'network'): uint16_t ns3::QueueDiscItem::GetProtocol() const [member function]
    cls.add_method('GetProtocol', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## queue-item.h (module 'network'): uint8_t ns3::QueueDiscItem::GetTxQueueIndex() const [member function]
    cls.add_method('GetTxQueueIndex', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## queue-item.h (module 'network'): void ns3::QueueDiscItem::SetTxQueueIndex(uint8_t txq) [member function]
    cls.add_method('SetTxQueueIndex', 
                   'void', 
                   [param('uint8_t', 'txq')])
    ## queue-item.h (module 'network'): ns3::Time ns3::QueueDiscItem::GetTimeStamp() const [member function]
    cls.add_method('GetTimeStamp', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## queue-item.h (module 'network'): void ns3::QueueDiscItem::SetTimeStamp(ns3::Time t) [member function]
    cls.add_method('SetTimeStamp', 
                   'void', 
                   [param('ns3::Time', 't')])
    ## queue-item.h (module 'network'): void ns3::QueueDiscItem::AddHeader() [member function]
    cls.add_method('AddHeader', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## queue-item.h (module 'network'): void ns3::QueueDiscItem::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## queue-item.h (module 'network'): bool ns3::QueueDiscItem::Mark() [member function]
    cls.add_method('Mark', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## queue-item.h (module 'network'): uint32_t ns3::QueueDiscItem::Hash(uint32_t perturbation=0) const [member function]
    cls.add_method('Hash', 
                   'uint32_t', 
                   [param('uint32_t', 'perturbation', default_value='0')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3LoRaGwNetDevice_methods(root_module, cls):
    ## lora-gw-net-device.h (module 'lora'): ns3::LoRaGwNetDevice::LoRaGwNetDevice(ns3::LoRaGwNetDevice const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaGwNetDevice const &', 'arg0')])
    ## lora-gw-net-device.h (module 'lora'): ns3::LoRaGwNetDevice::LoRaGwNetDevice() [constructor]
    cls.add_constructor([])
    ## lora-gw-net-device.h (module 'lora'): void ns3::LoRaGwNetDevice::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lora-gw-net-device.h (module 'lora'): ns3::Ptr<ns3::LoRaGwPhy> ns3::LoRaGwNetDevice::GetPhy() const [member function]
    cls.add_method('GetPhy', 
                   'ns3::Ptr< ns3::LoRaGwPhy >', 
                   [], 
                   is_const=True)
    ## lora-gw-net-device.h (module 'lora'): static ns3::TypeId ns3::LoRaGwNetDevice::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-gw-net-device.h (module 'lora'): void ns3::LoRaGwNetDevice::NotifyReceptionEndError() [member function]
    cls.add_method('NotifyReceptionEndError', 
                   'void', 
                   [])
    ## lora-gw-net-device.h (module 'lora'): void ns3::LoRaGwNetDevice::NotifyReceptionEndOk(ns3::Ptr<ns3::Packet> p, uint32_t bandwidth, uint8_t spreading, uint32_t frequency, double rssi) [member function]
    cls.add_method('NotifyReceptionEndOk', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'p'), param('uint32_t', 'bandwidth'), param('uint8_t', 'spreading'), param('uint32_t', 'frequency'), param('double', 'rssi')])
    ## lora-gw-net-device.h (module 'lora'): void ns3::LoRaGwNetDevice::NotifyTransmissionEnd(ns3::Ptr<const ns3::Packet> arg0) [member function]
    cls.add_method('NotifyTransmissionEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'arg0')])
    ## lora-gw-net-device.h (module 'lora'): bool ns3::LoRaGwNetDevice::SendFrom(ns3::Ptr<ns3::Packet> packet, ns3::Address const & source, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('SendFrom', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'source'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_virtual=True)
    ## lora-gw-net-device.h (module 'lora'): void ns3::LoRaGwNetDevice::CheckAckSend(ns3::Address const & addr, uint32_t frequency, uint8_t datarate, uint8_t powerIndex) [member function]
    cls.add_method('CheckAckSend', 
                   'void', 
                   [param('ns3::Address const &', 'addr'), param('uint32_t', 'frequency'), param('uint8_t', 'datarate'), param('uint8_t', 'powerIndex')], 
                   visibility='protected')
    ## lora-gw-net-device.h (module 'lora'): void ns3::LoRaGwNetDevice::DoCheckAckSend(ns3::Ptr<ns3::Packet> packet, uint32_t frequency, uint8_t datarate, uint8_t powerIndex) [member function]
    cls.add_method('DoCheckAckSend', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('uint32_t', 'frequency'), param('uint8_t', 'datarate'), param('uint8_t', 'powerIndex')], 
                   visibility='protected', is_virtual=True)
    ## lora-gw-net-device.h (module 'lora'): void ns3::LoRaGwNetDevice::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-gw-net-device.h (module 'lora'): static uint8_t ns3::LoRaGwNetDevice::GetDatarate(uint32_t bandwidth, uint8_t spreading) [member function]
    cls.add_method('GetDatarate', 
                   'uint8_t', 
                   [param('uint32_t', 'bandwidth'), param('uint8_t', 'spreading')], 
                   is_static=True, visibility='protected')
    ## lora-gw-net-device.h (module 'lora'): uint8_t ns3::LoRaGwNetDevice::GetRxDatarate(uint8_t dr, uint8_t offset) [member function]
    cls.add_method('GetRxDatarate', 
                   'uint8_t', 
                   [param('uint8_t', 'dr'), param('uint8_t', 'offset')], 
                   visibility='protected')
    ## lora-gw-net-device.h (module 'lora'): void ns3::LoRaGwNetDevice::RemoveFromPending(ns3::Address const & addr) [member function]
    cls.add_method('RemoveFromPending', 
                   'void', 
                   [param('ns3::Address const &', 'addr')], 
                   visibility='protected')
    return

def register_Ns3LoRaGwNetDeviceDeviceInfo_methods(root_module, cls):
    ## lora-gw-net-device.h (module 'lora'): ns3::LoRaGwNetDevice::DeviceInfo::DeviceInfo() [constructor]
    cls.add_constructor([])
    ## lora-gw-net-device.h (module 'lora'): ns3::LoRaGwNetDevice::DeviceInfo::DeviceInfo(ns3::LoRaGwNetDevice::DeviceInfo const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaGwNetDevice::DeviceInfo const &', 'arg0')])
    ## lora-gw-net-device.h (module 'lora'): ns3::LoRaGwNetDevice::DeviceInfo::address [variable]
    cls.add_instance_attribute('address', 'ns3::Mac32Address', is_const=False)
    ## lora-gw-net-device.h (module 'lora'): ns3::LoRaGwNetDevice::DeviceInfo::datarate [variable]
    cls.add_instance_attribute('datarate', 'uint8_t', is_const=False)
    ## lora-gw-net-device.h (module 'lora'): ns3::LoRaGwNetDevice::DeviceInfo::delay [variable]
    cls.add_instance_attribute('delay', 'uint8_t', is_const=False)
    ## lora-gw-net-device.h (module 'lora'): ns3::LoRaGwNetDevice::DeviceInfo::frequency [variable]
    cls.add_instance_attribute('frequency', 'uint16_t', is_const=False)
    return

def register_Ns3LoRaRsGwNetDevice_methods(root_module, cls):
    ## lora-rs-gw-net-device.h (module 'lora'): ns3::LoRaRsGwNetDevice::LoRaRsGwNetDevice(ns3::LoRaRsGwNetDevice const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaRsGwNetDevice const &', 'arg0')])
    ## lora-rs-gw-net-device.h (module 'lora'): ns3::LoRaRsGwNetDevice::LoRaRsGwNetDevice() [constructor]
    cls.add_constructor([])
    ## lora-rs-gw-net-device.h (module 'lora'): void ns3::LoRaRsGwNetDevice::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lora-rs-gw-net-device.h (module 'lora'): uint32_t ns3::LoRaRsGwNetDevice::GetOffset() [member function]
    cls.add_method('GetOffset', 
                   'uint32_t', 
                   [])
    ## lora-rs-gw-net-device.h (module 'lora'): static ns3::TypeId ns3::LoRaRsGwNetDevice::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lora-rs-gw-net-device.h (module 'lora'): void ns3::LoRaRsGwNetDevice::SetOffset(uint32_t offset) [member function]
    cls.add_method('SetOffset', 
                   'void', 
                   [param('uint32_t', 'offset')])
    ## lora-rs-gw-net-device.h (module 'lora'): void ns3::LoRaRsGwNetDevice::DoCheckAckSend(ns3::Ptr<const ns3::Packet> packet, uint32_t frequency, uint8_t datarate, uint8_t powerIndex) [member function]
    cls.add_method('DoCheckAckSend', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint32_t', 'frequency'), param('uint8_t', 'datarate'), param('uint8_t', 'powerIndex')], 
                   visibility='protected', is_virtual=True)
    ## lora-rs-gw-net-device.h (module 'lora'): void ns3::LoRaRsGwNetDevice::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## lora-rs-gw-net-device.h (module 'lora'): static uint8_t ns3::LoRaRsGwNetDevice::GetDatarate(uint32_t bandwidth, uint8_t spreading) [member function]
    cls.add_method('GetDatarate', 
                   'uint8_t', 
                   [param('uint32_t', 'bandwidth'), param('uint8_t', 'spreading')], 
                   is_static=True, visibility='protected')
    ## lora-rs-gw-net-device.h (module 'lora'): void ns3::LoRaRsGwNetDevice::SendBeacon() [member function]
    cls.add_method('SendBeacon', 
                   'void', 
                   [], 
                   visibility='protected')
    return

def register_Ns3LoRaRsGwNetDeviceDeviceInfo_methods(root_module, cls):
    ## lora-rs-gw-net-device.h (module 'lora'): ns3::LoRaRsGwNetDevice::DeviceInfo::DeviceInfo() [constructor]
    cls.add_constructor([])
    ## lora-rs-gw-net-device.h (module 'lora'): ns3::LoRaRsGwNetDevice::DeviceInfo::DeviceInfo(ns3::LoRaRsGwNetDevice::DeviceInfo const & arg0) [constructor]
    cls.add_constructor([param('ns3::LoRaRsGwNetDevice::DeviceInfo const &', 'arg0')])
    ## lora-rs-gw-net-device.h (module 'lora'): ns3::LoRaRsGwNetDevice::DeviceInfo::address [variable]
    cls.add_instance_attribute('address', 'ns3::Mac32Address', is_const=False)
    ## lora-rs-gw-net-device.h (module 'lora'): ns3::LoRaRsGwNetDevice::DeviceInfo::datarate [variable]
    cls.add_instance_attribute('datarate', 'uint8_t', is_const=False)
    ## lora-rs-gw-net-device.h (module 'lora'): ns3::LoRaRsGwNetDevice::DeviceInfo::delay [variable]
    cls.add_instance_attribute('delay', 'uint8_t', is_const=False)
    ## lora-rs-gw-net-device.h (module 'lora'): ns3::LoRaRsGwNetDevice::DeviceInfo::power [variable]
    cls.add_instance_attribute('power', 'uint8_t', is_const=False)
    return

def register_Ns3HashImplementation_methods(root_module, cls):
    ## hash-function.h (module 'core'): ns3::Hash::Implementation::Implementation(ns3::Hash::Implementation const & arg0) [constructor]
    cls.add_constructor([param('ns3::Hash::Implementation const &', 'arg0')])
    ## hash-function.h (module 'core'): ns3::Hash::Implementation::Implementation() [constructor]
    cls.add_constructor([])
    ## hash-function.h (module 'core'): uint32_t ns3::Hash::Implementation::GetHash32(char const * buffer, std::size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('std::size_t const', 'size')], 
                   is_pure_virtual=True, is_virtual=True)
    ## hash-function.h (module 'core'): uint64_t ns3::Hash::Implementation::GetHash64(char const * buffer, std::size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('std::size_t const', 'size')], 
                   is_virtual=True)
    ## hash-function.h (module 'core'): void ns3::Hash::Implementation::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3HashFunctionFnv1a_methods(root_module, cls):
    ## hash-fnv.h (module 'core'): ns3::Hash::Function::Fnv1a::Fnv1a(ns3::Hash::Function::Fnv1a const & arg0) [constructor]
    cls.add_constructor([param('ns3::Hash::Function::Fnv1a const &', 'arg0')])
    ## hash-fnv.h (module 'core'): ns3::Hash::Function::Fnv1a::Fnv1a() [constructor]
    cls.add_constructor([])
    ## hash-fnv.h (module 'core'): uint32_t ns3::Hash::Function::Fnv1a::GetHash32(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-fnv.h (module 'core'): uint64_t ns3::Hash::Function::Fnv1a::GetHash64(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-fnv.h (module 'core'): void ns3::Hash::Function::Fnv1a::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3HashFunctionHash32_methods(root_module, cls):
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash32::Hash32(ns3::Hash::Function::Hash32 const & arg0) [constructor]
    cls.add_constructor([param('ns3::Hash::Function::Hash32 const &', 'arg0')])
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash32::Hash32(ns3::Hash::Hash32Function_ptr hp) [constructor]
    cls.add_constructor([param('ns3::Hash::Hash32Function_ptr', 'hp')])
    ## hash-function.h (module 'core'): uint32_t ns3::Hash::Function::Hash32::GetHash32(char const * buffer, std::size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('std::size_t const', 'size')], 
                   is_virtual=True)
    ## hash-function.h (module 'core'): void ns3::Hash::Function::Hash32::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3HashFunctionHash64_methods(root_module, cls):
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash64::Hash64(ns3::Hash::Function::Hash64 const & arg0) [constructor]
    cls.add_constructor([param('ns3::Hash::Function::Hash64 const &', 'arg0')])
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash64::Hash64(ns3::Hash::Hash64Function_ptr hp) [constructor]
    cls.add_constructor([param('ns3::Hash::Hash64Function_ptr', 'hp')])
    ## hash-function.h (module 'core'): uint32_t ns3::Hash::Function::Hash64::GetHash32(char const * buffer, std::size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('std::size_t const', 'size')], 
                   is_virtual=True)
    ## hash-function.h (module 'core'): uint64_t ns3::Hash::Function::Hash64::GetHash64(char const * buffer, std::size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('std::size_t const', 'size')], 
                   is_virtual=True)
    ## hash-function.h (module 'core'): void ns3::Hash::Function::Hash64::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3HashFunctionMurmur3_methods(root_module, cls):
    ## hash-murmur3.h (module 'core'): ns3::Hash::Function::Murmur3::Murmur3(ns3::Hash::Function::Murmur3 const & arg0) [constructor]
    cls.add_constructor([param('ns3::Hash::Function::Murmur3 const &', 'arg0')])
    ## hash-murmur3.h (module 'core'): ns3::Hash::Function::Murmur3::Murmur3() [constructor]
    cls.add_constructor([])
    ## hash-murmur3.h (module 'core'): uint32_t ns3::Hash::Function::Murmur3::GetHash32(char const * buffer, std::size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('std::size_t const', 'size')], 
                   is_virtual=True)
    ## hash-murmur3.h (module 'core'): uint64_t ns3::Hash::Function::Murmur3::GetHash64(char const * buffer, std::size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('std::size_t const', 'size')], 
                   is_virtual=True)
    ## hash-murmur3.h (module 'core'): void ns3::Hash::Function::Murmur3::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    return

def register_functions(root_module):
    module = root_module
    ## mac32-address.h (module 'lora'): ns3::Ptr<const ns3::AttributeChecker> ns3::MakeMac32AddressChecker() [free function]
    module.add_function('MakeMac32AddressChecker', 
                        'ns3::Ptr< ns3::AttributeChecker const >', 
                        [])
    ## lora-mac-header.h (module 'lora'): void ns3::ReadFrom(ns3::Buffer::Iterator & i, ns3::Mac32Address & ad) [free function]
    module.add_function('ReadFrom', 
                        'void', 
                        [param('ns3::Buffer::Iterator &', 'i'), param('ns3::Mac32Address &', 'ad')])
    ## lora-mac-header.h (module 'lora'): void ns3::WriteTo(ns3::Buffer::Iterator & i, ns3::Mac32Address ad) [free function]
    module.add_function('WriteTo', 
                        'void', 
                        [param('ns3::Buffer::Iterator &', 'i'), param('ns3::Mac32Address', 'ad')])
    register_functions_ns3_FatalImpl(module.add_cpp_namespace('FatalImpl'), root_module)
    register_functions_ns3_Hash(module.add_cpp_namespace('Hash'), root_module)
    register_functions_ns3_TracedValueCallback(module.add_cpp_namespace('TracedValueCallback'), root_module)
    register_functions_ns3_internal(module.add_cpp_namespace('internal'), root_module)
    return

def register_functions_ns3_FatalImpl(module, root_module):
    return

def register_functions_ns3_Hash(module, root_module):
    register_functions_ns3_Hash_Function(module.add_cpp_namespace('Function'), root_module)
    return

def register_functions_ns3_Hash_Function(module, root_module):
    return

def register_functions_ns3_TracedValueCallback(module, root_module):
    return

def register_functions_ns3_internal(module, root_module):
    return

def main():
    out = FileCodeSink(sys.stdout)
    root_module = module_init()
    register_types(root_module)
    register_methods(root_module)
    register_functions(root_module)
    root_module.generate(out)

if __name__ == '__main__':
    main()

