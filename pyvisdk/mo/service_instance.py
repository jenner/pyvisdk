
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ServiceInstance(BaseEntity):
    '''The ServiceInstance managed object is the singleton root object of the inventory
        on both vCenter servers and servers running on standalone host agents. The
        server creates the ServiceInstance automatically, and also automatically
        creates the various manager entities that provide services in the virtual
        environment. Some examples of manager entities are LicenseManager,
        PerformanceManager, and ViewManager. You can access the manager entities
        through the content property.A vSphere API client application begins by
        connecting to a server and obtaining a reference to the ServiceInstance.
        The client can then use the RetrieveServiceContent method to gain access
        to the various vSphere manager entities and to the root folder of the
        inventory.When you create managed objects, the server adds them to the
        inventory. The inventory of managed objects includes instances the
        following object types:The following figure shows the organization of
        managed objects in the vCenter hierarchy:Every Datacenter has the
        following set of dedicated folders. These folders are empty until you
        create entities for the Datacenter.The host agent hierarchy has the same
        general form as the vCenter hierarchy, but most of the objects are limited
        to one instance:
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ServiceInstance):
        # MUST define these
        super(ServiceInstance, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def capability(self):
        '''API-wide capabilities.
        '''
        return self.update('capability')

    @property
    def content(self):
        '''The properties of the ServiceInstance managed object. The content property is
        identical to the return value from the RetrieveServiceContent method.
        '''
        return self.update('content')

    @property
    def serverClock(self):
        '''Contains the time most recently obtained from the server. The time is not
        necessarily current. This property is intended for use with the
        PropertyCollector WaitForUpdates method. The PropertyCollector will
        provide notification if some event occurs that changes the server clock
        time in a non-linear fashion.
        '''
        return self.update('serverClock')


    def CurrentTime(self, vm, state, testType, pool, host):
        '''Returns the current time on the server. To monitor non-linear time changes, use
        the serverClock property.

        :param vm: to a VirtualMachine[]The set of virtual machines intended for migration.

        :param state: The power state that the virtual machines must have. If this argument is not set,
        each virtual machine is evaluated according to its current power state.

        :param testType: The set of tests to run. If this argument is not set, all tests will be run.

        :param pool: to a ResourcePoolThe target resource pool for the virtual machines. If the pool
        parameter is left unset, the target pool for each particular virtual
        machine's migration will be that virtual machine's current pool. If the
        virtual machine is a template then either this parameter or the host
        parameter must be set; additionally if resource tests are requested then
        this parameter is required.

        :param host: to a HostSystemThe target host on which the virtual machines will run. The host
        parameter may be left unset if the compute resource associated with the
        target pool represents a stand-alone host or a DRS-enabled cluster. In the
        former case the stand-alone host is used as the target host. In the latter
        case, each connected host in the cluster that is not in maintenance mode
        is tested as a target host. If the virtual machine is a template then
        either this parameter or the pool parameter must be set.


        :rtype: Event[] 

        '''
        
        return self.delegate("CurrentTime")(vm,state,testType,pool,host)
        

    def QueryVMotionCompatibility(self, vm, state, testType, pool, host):
        '''Deprecated. As of vSphere API 4.0, use QueryVMotionCompatibilityEx_Task instead.
        Investigates the general VMotion compatibility of a virtual machine with a
        set of hosts. The virtual machine may be in any power state. Hosts may be
        in any connection state and also may be in maintenance mode.

        :param vm: to a VirtualMachine[]The set of virtual machines intended for migration.

        :param state: The power state that the virtual machines must have. If this argument is not set,
        each virtual machine is evaluated according to its current power state.

        :param testType: The set of tests to run. If this argument is not set, all tests will be run.

        :param pool: to a ResourcePoolThe target resource pool for the virtual machines. If the pool
        parameter is left unset, the target pool for each particular virtual
        machine's migration will be that virtual machine's current pool. If the
        virtual machine is a template then either this parameter or the host
        parameter must be set; additionally if resource tests are requested then
        this parameter is required.

        :param host: to a HostSystemThe target host on which the virtual machines will run. The host
        parameter may be left unset if the compute resource associated with the
        target pool represents a stand-alone host or a DRS-enabled cluster. In the
        former case the stand-alone host is used as the target host. In the latter
        case, each connected host in the cluster that is not in maintenance mode
        is tested as a target host. If the virtual machine is a template then
        either this parameter or the pool parameter must be set.


        :rtype: Event[] 

        '''
        
        return self.delegate("QueryVMotionCompatibility")(vm,state,testType,pool,host)
        

    def RetrieveProductComponents(self, vm, state, testType, pool, host):
        '''Component information for bundled products

        :param vm: to a VirtualMachine[]The set of virtual machines intended for migration.

        :param state: The power state that the virtual machines must have. If this argument is not set,
        each virtual machine is evaluated according to its current power state.

        :param testType: The set of tests to run. If this argument is not set, all tests will be run.

        :param pool: to a ResourcePoolThe target resource pool for the virtual machines. If the pool
        parameter is left unset, the target pool for each particular virtual
        machine's migration will be that virtual machine's current pool. If the
        virtual machine is a template then either this parameter or the host
        parameter must be set; additionally if resource tests are requested then
        this parameter is required.

        :param host: to a HostSystemThe target host on which the virtual machines will run. The host
        parameter may be left unset if the compute resource associated with the
        target pool represents a stand-alone host or a DRS-enabled cluster. In the
        former case the stand-alone host is used as the target host. In the latter
        case, each connected host in the cluster that is not in maintenance mode
        is tested as a target host. If the virtual machine is a template then
        either this parameter or the pool parameter must be set.


        :rtype: Event[] 

        '''
        
        return self.delegate("RetrieveProductComponents")(vm,state,testType,pool,host)
        

    def RetrieveServiceContent(self, vm, state, testType, pool, host):
        '''Retrieves the properties of the service instance.

        :param vm: to a VirtualMachine[]The set of virtual machines intended for migration.

        :param state: The power state that the virtual machines must have. If this argument is not set,
        each virtual machine is evaluated according to its current power state.

        :param testType: The set of tests to run. If this argument is not set, all tests will be run.

        :param pool: to a ResourcePoolThe target resource pool for the virtual machines. If the pool
        parameter is left unset, the target pool for each particular virtual
        machine's migration will be that virtual machine's current pool. If the
        virtual machine is a template then either this parameter or the host
        parameter must be set; additionally if resource tests are requested then
        this parameter is required.

        :param host: to a HostSystemThe target host on which the virtual machines will run. The host
        parameter may be left unset if the compute resource associated with the
        target pool represents a stand-alone host or a DRS-enabled cluster. In the
        former case the stand-alone host is used as the target host. In the latter
        case, each connected host in the cluster that is not in maintenance mode
        is tested as a target host. If the virtual machine is a template then
        either this parameter or the pool parameter must be set.


        :rtype: Event[] 

        '''
        
        return self.delegate("RetrieveServiceContent")(vm,state,testType,pool,host)
        

    def ValidateMigration(self, vm, state, testType, pool, host):
        '''Deprecated. As of vSphere API 4.0, use VirtualMachineProvisioningChecker instead.
        Checks the validity of a set of proposed migrations. A migration is the
        act of changing the assigned execution host of a virtual machine, which
        can result from invoking MigrateVM_Task or RelocateVM_Task.

        :param vm: to a VirtualMachine[]The set of virtual machines intended for migration.

        :param state: The power state that the virtual machines must have. If this argument is not set,
        each virtual machine is evaluated according to its current power state.

        :param testType: The set of tests to run. If this argument is not set, all tests will be run.

        :param pool: to a ResourcePoolThe target resource pool for the virtual machines. If the pool
        parameter is left unset, the target pool for each particular virtual
        machine's migration will be that virtual machine's current pool. If the
        virtual machine is a template then either this parameter or the host
        parameter must be set; additionally if resource tests are requested then
        this parameter is required.

        :param host: to a HostSystemThe target host on which the virtual machines will run. The host
        parameter may be left unset if the compute resource associated with the
        target pool represents a stand-alone host or a DRS-enabled cluster. In the
        former case the stand-alone host is used as the target host. In the latter
        case, each connected host in the cluster that is not in maintenance mode
        is tested as a target host. If the virtual machine is a template then
        either this parameter or the pool parameter must be set.


        :rtype: Event[] 

        '''
        
        return self.delegate("ValidateMigration")(vm,state,testType,pool,host)
        
