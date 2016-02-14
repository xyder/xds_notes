from sqlalchemy import Column, Integer, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from core.database import Base
from core.lib import get_custom_prefixer
from xds_notes import APP_NAME

prefixer = get_custom_prefixer(APP_NAME)


class TaskProject(Base):
    __tablename__ = prefixer('task_projects')
    id = Column(Integer, primary_key=True)

    name = Column(Text)

    def __repr__(self):
        return self.name


class TaskList(Base):
    __tablename__ = prefixer('task_lists')
    id = Column(Integer, primary_key=True)

    title = Column(Text)

    position = Column(Integer)

    parent_id = Column(Integer, ForeignKey(prefixer('task_projects.id')), index=True)
    parent = relationship('TaskProject', backref='task_lists')

    def __repr__(self):
        return self.title


class Task(Base):
    __tablename__ = prefixer('task')
    id = Column(Integer, primary_key=True)

    title = Column(Text)
    description = Column(Text)
    state = Column(Enum('open', 'in_progress', 'closed', name='task_states'), nullable=False)

    position = Column(Integer)

    parent_id = Column(Integer, ForeignKey(prefixer('task_lists.id')), index=True)
    parent = relationship('TaskList', backref='tasks')

    def __repr__(self):
        return self.title


# register recounting listeners for these models
Base.register_recountable_model(TaskList)
Base.register_recountable_model(Task)
