class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_map = {}
        for cp in cpdomains:
            count, domain = cp.split(" ")
            count = int(count)
            domains = domain.split(".")
             # Iterate through the subdomains, starting from the full domain
            for i in range(len(domains)):
                subdomain = ".".join(domains[i:])
                domain_map[subdomain] = domain_map.get(subdomain, 0) + count
        
        return [f"{count} {domain}" for domain, count in domain_map.items()]
# TC O (3n) + O(nm)
# SC O(n * m)