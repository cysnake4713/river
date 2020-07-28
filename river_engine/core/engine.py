from river_engine.core.resource import ResourceItem, ResourceMapper
from river_engine.core.scheduler import Scheduler
from river_engine.core.synchronizer import SyncItem, Synchronizer


class ExecutionEngine:

    def __init__(self, settings) -> None:
        super().__init__()
        self._resource_mapper_settings = {}

        self._setup(settings)

    def _setup(self, settings):
        self._resource_mapper_settings = settings.RESOURCE_MAPPER

    def sync_update(self, resource_item: ResourceItem):
        resource_mapper = self.get_resource_mapper(resource_item)
        sync_item = resource_mapper.translate(resource_item)

        scheduler = self.get_scheduler()

        scheduler.push(sync_item)

    def async_update(self, sync_item: SyncItem):
        synchronizer = self.get_synchronizer(sync_item)

        sync_result = synchronizer.sync(sync_item)
        return sync_result

    def async_apply(self, resource_item: ResourceItem):
        resource_mapper = self.get_resource_mapper(resource_item)
        sync_item = resource_mapper.translate(resource_item)

        scheduler = self.get_scheduler()

        scheduler.push(sync_item)

    def get_resource_mapper(self, resource_item: ResourceItem) -> ResourceMapper:
        # TODO:
        pass

    def get_scheduler(self) -> Scheduler:
        pass

    def get_synchronizer(self, sync_item) -> Synchronizer:
        pass
