from Agents.assistant_agent import AssistantAgent
from Agents.dev_agent import DevAgent
from Agents.teacher_agent import TeacherAgent
from Agents.therapist_agent import TherapistAgent


class AgentsFactory():
    agents = {
        "Assistant": AssistantAgent,
        "Teacher": TeacherAgent,
        "Therapist": TherapistAgent,
        "Developer": DevAgent
    }

    @classmethod
    def get_agent(cls, agent_type):
        agent_class = cls.agents.get(agent_type)
        return agent_class(agent_type.lower()) if agent_class else None
