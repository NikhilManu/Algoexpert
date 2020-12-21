"""
Course Schedule II [leetCode]
"""
"""
There are a total of n courses you have to take labelled from 0 to n - 1.
Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course ai before the course bi.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [3, 1, 2, 0]
"""
#Solution -->
# Time O(V + E) | Space O(V + E)
-------------------------
def TopSort(jobs, deps):
    jobgraph = createGraph(jobs, deps)
    return getOrderedJob(jobgraph)

def getOrderedJob(jobgraph):
    orderedJob = []
    nodes = jobgraph.nodes
    while nodes:
        node = nodes.pop()
        containsCycle = dfs(node, orderedJob)
        if containsCycle:
            return []
    return orderedJob

def dfs(node, orderedJob):
    if node.visited:
        return False
    if node.visiting:
        return True
    node.visiting = True
    for prereq in node.prereq:
        containsCycle = dfs(prereq, orderedJob)
        if containsCycle:
            return True
        
    node.visiting = False
    node.visited = True
    orderedJob.append(node.job)
    
def createGraph(jobs, deps):
    jobgraph = JobGraph(jobs)
    for prereq, job in deps:
        jobgraph.addPrereq(prereq, job)
    return jobgraph

class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)
            
    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])
        
    def addPrereq(self, prereq, job):
        prereqNode = self.getNode(prereq)
        jobNode = self.getNode(job)
        jobNode.prereq.append(prereqNode)
        
    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]
        
class JobNode:
    def __init__(self, job):
        self.job = job
        self.prereq = []
        self.visited = False
        self.visiting = False
           
         
  
