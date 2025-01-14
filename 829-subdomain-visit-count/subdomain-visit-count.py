class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_map = {}
        for cp in cpdomains:
            count, domain = cp.split(" ")
            domains = domain.split(".")
            domain_map[domain] = domain_map.get(domain,0) + int(count)
            # for domain in domains[1:]:
            if(len(domains) == 3):
                domain = domains[1] + "." + domains[2]
                domain_map[domain] = domain_map.get(domain,0) + int(count)
            domain = domains[-1]
            domain_map[domain] = domain_map.get(domain,0) + int(count)
        
        array_of_lists = [ str(value) + " "+ key for key, value in domain_map.items()] 
        return array_of_lists
