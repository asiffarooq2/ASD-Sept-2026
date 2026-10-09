# import dns.resolver
# domain = "google.com"
# subdomains = ["mail", "ftp", "test", "admin", "api", "dev", "blog"]
# for sub in subdomains:
#     full_domain = f"{sub}.{domain}"#mail.example.com
#     try:
#         result = dns.resolver.resolve(full_domain, "A")
#         # print(result)
#         print(f"[FOUND] {full_domain}")
#     except Exception as e:
#         print(e)


import dns.resolver
domain = "google.com"
with open("subdomains.txt", "r") as file:
    subs = file.read().splitlines()
    # subs = file.read()
# print(subs)
for sub in subs:
    full_domain = f"{sub}.{domain}"
    try:
        dns.resolver.resolve(full_domain, "A")
        print("[ACTIVE]", full_domain)
        answers = dns.resolver.resolve(full_domain, "A")
        for rdata in answers:
            print(rdata.to_text())
    # except Exception as e:
    #     print(e)
    except dns.resolver.NXDOMAIN:
        print(dns.resolver.NXDOMAIN)
    # except dns.resolver.NoAnswer:
    #     print(dns.resolver.NoAnswer)
    # except:
    #     pass