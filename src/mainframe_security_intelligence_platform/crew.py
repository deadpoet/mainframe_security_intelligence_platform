import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	ScrapeWebsiteTool
)






@CrewBase
class MainframeSecurityIntelligencePlatformCrew:
    """MainframeSecurityIntelligencePlatform crew"""

    
    @agent
    def smf_type_80_racf_log_analyst(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["smf_type_80_racf_log_analyst"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-2.5-flash",
                temperature=0.3,
                
            ),
            
        )
        
    
    @agent
    def z_os_racf_threat_hunter(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["z_os_racf_threat_hunter"],
            
            
            tools=[				ScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-2.5-flash",
                temperature=0.3,
                
            ),
            
        )
        
    
    @agent
    def z_os_security_remediation_engineer(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["z_os_security_remediation_engineer"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-2.5-flash",
                temperature=0.3,
                
            ),
            
        )
        
    

    
    @task
    def parse_smf_type_80_logs(self) -> Task:
        return Task(
            config=self.tasks_config["parse_smf_type_80_logs"],
            markdown=False,
            
            
        )
    
    @task
    def threat_hunting_and_incident_detection(self) -> Task:
        return Task(
            config=self.tasks_config["threat_hunting_and_incident_detection"],
            markdown=False,
            
            
        )
    
    @task
    def generate_actionable_remediation(self) -> Task:
        return Task(
            config=self.tasks_config["generate_actionable_remediation"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the MainframeSecurityIntelligencePlatform crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


