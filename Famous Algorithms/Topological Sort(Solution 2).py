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
#Solution --
# Time O(V + E) and Space
--------------------
def TopSort(jobs, deps):
    jobgraph = createGraph(jobs, deps)
    return getOrderedJob(jobgraph)

def getOrderedJob(jobgraph):
    orderedJob = []
    node_with_NoPre = list(filter(lambda node: node.numofPre == 0, jobgraph.nodes))
    while node_with_NoPre:
        node = node_with_NoPre.pop()
        orderedJob.append(node.job)
        removeDeps(node, node_with_NoPre)

    graphHasCycle = any(node.numofPre for node in jobgraph.nodes)
    return [] if graphHasCycle else orderedJob

def removeDeps(node, node_with_NoPre):
    while node.deps:
        dep = node.deps.pop()
        dep.numofPre -= 1
        if dep.numofPre == 0:
            node_with_NoPre.append(dep)


def createGraph(jobs, deps):
    jobgraph = JobGraph(jobs)
    for dep, job in deps:
        jobgraph.addDeps(dep, job)
    return jobgraph
        
class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in range(jobs):
            self.addNode(job)
        
    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])
        
    def addDeps(self, dep, job):
        jobNode = self.getNode(job)
        depNode = self.getNode(dep)
        jobNode.deps.append(depNode)
        depNode.numofPre += 1
        
    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]
        
class JobNode:
    def __init__(self, job):
        self.job = job
        self.deps = []
        self.numofPre = 0
