-- Kalpa Retail warehouse, the two-quarter book Anand asks for every Monday.
-- Built by data/generate_client_zero.py. Load with: psql -f data/warehouse_v4.sql
-- payments carries no foreign key on purpose: the feed holds payments whose order never arrived.
-- campaign_exposure carries no primary key on purpose: the second feed re-sent some customers.
DROP TABLE IF EXISTS campaign_exposure, plan_line, refunds, payments, orders, campaigns, customers;

CREATE TABLE customers (
    customer_id  text PRIMARY KEY,
    segment      text NOT NULL,
    city         text NOT NULL,
    country      text NOT NULL,
    joined_date  date NOT NULL
);

CREATE TABLE orders (
    order_id     text PRIMARY KEY,
    customer_id  text NOT NULL REFERENCES customers (customer_id),
    order_date   date NOT NULL,
    quarter      text NOT NULL,
    channel      text NOT NULL,
    amount       numeric(12, 2) NOT NULL,
    status       text NOT NULL
);

CREATE TABLE payments (
    payment_id    text PRIMARY KEY,
    order_id      text NOT NULL,
    paid_date     date NOT NULL,
    amount        numeric(12, 2) NOT NULL,
    method        text NOT NULL,
    instalment_no integer NOT NULL
);

CREATE TABLE refunds (
    refund_id    text PRIMARY KEY,
    order_id     text NOT NULL,
    refund_date  date NOT NULL,
    amount       numeric(12, 2) NOT NULL,
    reason       text NOT NULL
);

CREATE TABLE campaigns (
    campaign_id  text PRIMARY KEY,
    name         text NOT NULL,
    start_date   date NOT NULL,
    end_date     date NOT NULL,
    segment      text NOT NULL
);

CREATE TABLE campaign_exposure (
    customer_id  text NOT NULL,
    campaign_id  text NOT NULL,
    exposed_date date NOT NULL
);

CREATE TABLE plan_line (
    week_start    date PRIMARY KEY,
    plan_revenue  numeric(14, 2) NOT NULL
);

COPY customers (customer_id, segment, city, country, joined_date) FROM stdin;
C-0001	Retail-Core	Delhi	IN	2024-01-09
C-0002	Retail-Core	Chennai	IN	2025-09-17
C-0003	Retail-Core	Delhi	IN	2025-10-10
C-0004	Retail-Core	Bengaluru	IN	2025-12-02
C-0005	Retail-Core	Bengaluru	IN	2025-07-04
C-0006	Retail-Core	Hyderabad	IN	2023-06-11
C-0007	Retail-Core	Bengaluru	IN	2025-10-04
C-0008	Retail-Core	Chennai	IN	2023-09-26
C-0009	Retail-Core	Pune	IN	2023-12-28
C-0010	Retail-Core	Hyderabad	IN	2023-01-19
C-0011	Retail-Core	Bengaluru	IN	2024-04-07
C-0012	Retail-Core	Delhi	IN	2025-12-07
C-0013	Retail-Core	Hyderabad	IN	2025-12-22
C-0014	Retail-Core	Mumbai	IN	2023-02-20
C-0015	Retail-Core	Pune	IN	2023-08-21
C-0016	Retail-Core	Delhi	IN	2024-03-04
C-0017	Retail-Core	Bengaluru	IN	2024-08-17
C-0018	Retail-Core	Delhi	IN	2025-07-25
C-0019	Retail-Core	Delhi	IN	2024-07-15
C-0020	Retail-Core	Pune	IN	2025-12-14
C-0021	Retail-Core	Mumbai	IN	2024-05-20
C-0022	Retail-Core	Hyderabad	IN	2024-06-23
C-0023	Retail-Core	Bengaluru	IN	2024-08-16
C-0024	Retail-Core	Hyderabad	IN	2025-04-20
C-0025	Retail-Core	Chennai	IN	2025-06-22
C-0026	Retail-Core	Chennai	IN	2023-06-27
C-0027	Retail-Core	Mumbai	IN	2025-02-24
C-0028	Retail-Core	Hyderabad	IN	2024-07-05
C-0029	Retail-Core	Mumbai	IN	2025-01-28
C-0030	Retail-Core	Delhi	IN	2025-11-15
C-0031	Retail-Core	Hyderabad	IN	2023-04-04
C-0032	Retail-Core	Hyderabad	IN	2024-11-06
C-0033	Retail-Core	Mumbai	IN	2023-08-07
C-0034	Retail-Core	Bengaluru	IN	2023-10-08
C-0035	Retail-Core	Bengaluru	IN	2025-06-23
C-0036	Retail-Core	Delhi	IN	2025-12-25
C-0037	Retail-Core	Chennai	IN	2025-01-22
C-0038	Retail-Core	Pune	IN	2023-10-19
C-0039	Retail-Core	Delhi	IN	2025-05-01
C-0040	Retail-Core	Delhi	IN	2023-11-11
C-0041	Retail-Core	Hyderabad	IN	2024-06-17
C-0042	Retail-Core	Mumbai	IN	2023-06-13
C-0043	Retail-Core	Bengaluru	IN	2023-03-05
C-0044	Retail-Core	Pune	IN	2024-09-19
C-0045	Retail-Core	Pune	IN	2024-01-05
C-0046	Retail-Core	Delhi	IN	2025-08-17
C-0047	Retail-Core	Bengaluru	IN	2024-02-14
C-0048	Retail-Core	Pune	IN	2024-05-02
C-0049	Retail-Core	Bengaluru	IN	2023-04-27
C-0050	Retail-Core	Pune	IN	2025-08-22
C-0051	Retail-Core	Mumbai	IN	2023-05-07
C-0052	Retail-Core	Chennai	IN	2025-09-12
C-0053	Retail-Core	Chennai	IN	2023-07-28
C-0054	Retail-Core	Pune	IN	2025-04-14
C-0055	Retail-Core	Hyderabad	IN	2024-02-16
C-0056	Retail-Core	Mumbai	IN	2023-05-04
C-0057	Retail-Core	Pune	IN	2023-02-28
C-0058	Retail-Core	Bengaluru	IN	2024-04-17
C-0059	Retail-Core	Chennai	IN	2023-06-16
C-0060	Retail-Core	Pune	IN	2024-08-09
C-0061	Retail-Core	Hyderabad	IN	2024-11-07
C-0062	Retail-Core	Hyderabad	IN	2024-11-06
C-0063	Retail-Core	Mumbai	IN	2024-05-24
C-0064	Retail-Core	Delhi	IN	2025-03-02
C-0065	Retail-Core	Hyderabad	IN	2025-07-12
C-0066	Retail-Core	Chennai	IN	2023-12-05
C-0067	Retail-Core	Pune	IN	2023-10-17
C-0068	Retail-Core	Pune	IN	2025-08-11
C-0069	Retail-Core	Bengaluru	IN	2024-01-28
C-0070	Retail-Core	Hyderabad	IN	2024-10-19
C-0071	Retail-Core	Hyderabad	IN	2024-10-18
C-0072	Retail-Core	Chennai	IN	2024-07-19
C-0073	Retail-Core	Delhi	IN	2024-10-24
C-0074	Retail-Core	Mumbai	IN	2024-07-21
C-0075	Retail-Core	Chennai	IN	2023-04-11
C-0076	Retail-Core	Hyderabad	IN	2025-06-19
C-0077	Retail-Core	Hyderabad	IN	2023-03-03
C-0078	Retail-Core	Bengaluru	IN	2024-03-18
C-0079	Retail-Core	Bengaluru	IN	2024-06-05
C-0080	Retail-Core	Hyderabad	IN	2024-05-17
C-0081	Retail-Core	Hyderabad	IN	2024-04-19
C-0082	Retail-Core	Bengaluru	IN	2024-09-04
C-0083	Retail-Core	Delhi	IN	2024-06-08
C-0084	Retail-Core	Pune	IN	2024-02-20
C-0085	Retail-Core	Chennai	IN	2023-06-04
C-0086	Retail-Core	Chennai	IN	2023-07-15
C-0087	Retail-Core	Pune	IN	2025-01-18
C-0088	Retail-Core	Bengaluru	IN	2023-06-25
C-0089	Retail-Core	Delhi	IN	2023-01-16
C-0090	Retail-Core	Delhi	IN	2024-09-23
C-0091	Retail-Core	Hyderabad	IN	2025-11-25
C-0092	Retail-Core	Chennai	IN	2025-06-23
C-0093	Retail-Core	Mumbai	IN	2024-03-24
C-0094	Retail-Core	Hyderabad	IN	2023-11-12
C-0095	Retail-Core	Mumbai	IN	2024-05-13
C-0096	Retail-Core	Hyderabad	IN	2023-06-10
C-0097	Retail-Core	Pune	IN	2025-05-15
C-0098	Retail-Core	Chennai	IN	2024-09-27
C-0099	Retail-Core	Pune	IN	2023-12-26
C-0100	Retail-Core	Hyderabad	IN	2023-12-20
C-0101	Retail-Core	Hyderabad	IN	2024-09-12
C-0102	Retail-Core	Hyderabad	IN	2024-10-01
C-0103	Retail-Core	Chennai	IN	2024-09-28
C-0104	Retail-Core	Delhi	IN	2024-10-20
C-0105	Retail-Core	Hyderabad	IN	2024-11-17
C-0106	Retail-Core	Bengaluru	IN	2024-05-07
C-0107	Retail-Core	Pune	IN	2024-06-20
C-0108	Retail-Core	Mumbai	IN	2025-04-25
C-0109	Retail-Core	Bengaluru	IN	2025-01-11
C-0110	Retail-Core	Mumbai	IN	2025-01-21
C-0111	Retail-Core	Pune	IN	2024-10-08
C-0112	Retail-Core	Pune	IN	2025-07-02
C-0113	Retail-Core	Bengaluru	IN	2024-10-01
C-0114	Retail-Core	Mumbai	IN	2025-06-16
C-0115	Retail-Core	Chennai	IN	2025-08-04
C-0116	Retail-Core	Delhi	IN	2024-11-10
C-0117	Retail-Core	Hyderabad	IN	2023-03-17
C-0118	Retail-Core	Mumbai	IN	2024-11-10
C-0119	Retail-Core	Mumbai	IN	2023-02-14
C-0120	Retail-Core	Pune	IN	2024-10-05
C-0121	Retail-Core	Chennai	IN	2025-03-22
C-0122	Retail-Core	Pune	IN	2024-09-05
C-0123	Retail-Core	Pune	IN	2023-08-20
C-0124	Retail-Core	Pune	IN	2023-03-04
C-0125	Retail-Core	Chennai	IN	2024-01-24
C-0126	Retail-Core	Mumbai	IN	2023-07-03
C-0127	Retail-Core	Chennai	IN	2023-03-25
C-0128	Retail-Core	Chennai	IN	2023-03-27
C-0129	Retail-Core	Delhi	IN	2024-10-24
C-0130	Retail-Core	Chennai	IN	2024-07-04
C-0131	Retail-Core	Delhi	IN	2025-02-12
C-0132	Retail-Core	Pune	IN	2023-10-12
C-0133	Retail-Core	Chennai	IN	2025-10-07
C-0134	Retail-Core	Pune	IN	2024-10-27
C-0135	Retail-Core	Pune	IN	2023-04-19
C-0136	Retail-Core	Pune	IN	2025-03-04
C-0137	Retail-Core	Hyderabad	IN	2023-04-26
C-0138	Retail-Core	Bengaluru	IN	2023-12-03
C-0139	Retail-Core	Pune	IN	2025-12-09
C-0140	Retail-Core	Bengaluru	IN	2024-03-01
C-0141	Retail-Core	Bengaluru	IN	2024-12-02
C-0142	Retail-Core	Chennai	IN	2024-08-08
C-0143	Retail-Core	Pune	IN	2025-07-18
C-0144	Retail-Core	Mumbai	IN	2024-02-03
C-0145	Retail-Core	Chennai	IN	2023-01-14
C-0146	Retail-Core	Delhi	IN	2023-01-27
C-0147	Retail-Core	Pune	IN	2024-04-04
C-0148	Retail-Core	Delhi	IN	2024-11-14
C-0149	Retail-Core	Chennai	IN	2025-11-11
C-0150	Retail-Core	Pune	IN	2025-01-20
C-0151	Retail-Plus	Mumbai	IN	2025-03-13
C-0152	Retail-Plus	Pune	IN	2025-01-04
C-0153	Retail-Plus	Mumbai	IN	2025-08-05
C-0154	Retail-Plus	Mumbai	IN	2024-11-24
C-0155	Retail-Plus	Chennai	IN	2024-01-25
C-0156	Retail-Plus	Bengaluru	IN	2023-04-15
C-0157	Retail-Plus	Mumbai	IN	2024-11-05
C-0158	Retail-Plus	Mumbai	IN	2023-04-23
C-0159	Retail-Plus	Delhi	IN	2023-10-09
C-0160	Retail-Plus	Chennai	IN	2025-03-10
C-0161	Retail-Plus	Pune	IN	2024-06-27
C-0162	Retail-Plus	Delhi	IN	2024-01-27
C-0163	Retail-Plus	Bengaluru	IN	2025-06-04
C-0164	Retail-Plus	Bengaluru	IN	2024-06-19
C-0165	Retail-Plus	Delhi	IN	2025-04-20
C-0166	Retail-Plus	Bengaluru	IN	2023-11-14
C-0167	Retail-Plus	Hyderabad	IN	2025-10-26
C-0168	Retail-Plus	Mumbai	IN	2024-10-01
C-0169	Retail-Plus	Hyderabad	IN	2024-06-08
C-0170	Retail-Plus	Pune	IN	2024-08-13
C-0171	Retail-Plus	Hyderabad	IN	2025-05-06
C-0172	Retail-Plus	Delhi	IN	2024-02-03
C-0173	Retail-Plus	Pune	IN	2023-01-20
C-0174	Retail-Plus	Mumbai	IN	2025-03-04
C-0175	Retail-Plus	Mumbai	IN	2024-10-17
C-0176	Retail-Plus	Bengaluru	IN	2023-01-11
C-0177	Retail-Plus	Delhi	IN	2023-05-24
C-0178	Retail-Plus	Chennai	IN	2024-07-07
C-0179	Retail-Plus	Bengaluru	IN	2024-10-25
C-0180	Retail-Plus	Chennai	IN	2023-06-20
C-0181	Retail-Plus	Delhi	IN	2023-01-18
C-0182	Retail-Plus	Chennai	IN	2025-11-21
C-0183	Retail-Plus	Delhi	IN	2024-11-18
C-0184	Retail-Plus	Mumbai	IN	2025-11-10
C-0185	Retail-Plus	Delhi	IN	2024-04-27
C-0186	Retail-Plus	Delhi	IN	2024-03-15
C-0187	Retail-Plus	Pune	IN	2024-07-06
C-0188	Retail-Plus	Hyderabad	IN	2025-11-02
C-0189	Retail-Plus	Delhi	IN	2024-04-17
C-0190	Retail-Plus	Delhi	IN	2024-08-11
C-0191	Retail-Plus	Delhi	IN	2025-06-17
C-0192	Retail-Plus	Delhi	IN	2023-05-02
C-0193	Retail-Plus	Bengaluru	IN	2025-07-01
C-0194	Retail-Plus	Hyderabad	IN	2025-04-19
C-0195	Retail-Plus	Delhi	IN	2023-04-24
C-0196	Retail-Plus	Mumbai	IN	2023-08-19
C-0197	Retail-Plus	Pune	IN	2024-09-26
C-0198	Retail-Plus	Hyderabad	IN	2025-03-19
C-0199	Retail-Plus	Chennai	IN	2025-09-12
C-0200	Retail-Plus	Chennai	IN	2023-08-14
C-0201	Retail-Plus	Chennai	IN	2023-04-17
C-0202	Retail-Plus	Chennai	IN	2023-08-16
C-0203	Retail-Plus	Bengaluru	IN	2024-01-23
C-0204	Retail-Plus	Chennai	IN	2023-05-11
C-0205	Retail-Plus	Pune	IN	2023-12-01
C-0206	Retail-Plus	Hyderabad	IN	2023-09-15
C-0207	Retail-Plus	Chennai	IN	2025-07-23
C-0208	Retail-Plus	Bengaluru	IN	2023-05-03
C-0209	Retail-Plus	Chennai	IN	2025-07-28
C-0210	Retail-Plus	Delhi	IN	2023-06-10
C-0211	Retail-Plus	Chennai	IN	2023-11-06
C-0212	Retail-Plus	Mumbai	IN	2025-06-10
C-0213	Retail-Plus	Bengaluru	IN	2023-07-10
C-0214	Retail-Plus	Hyderabad	IN	2024-05-24
C-0215	Retail-Plus	Bengaluru	IN	2023-10-20
C-0216	Retail-Plus	Mumbai	IN	2023-01-01
C-0217	Retail-Plus	Hyderabad	IN	2024-01-21
C-0218	Retail-Plus	Hyderabad	IN	2024-06-27
C-0219	Retail-Plus	Delhi	IN	2024-09-19
C-0220	Retail-Plus	Chennai	IN	2024-08-28
C-0221	Retail-Plus	Chennai	IN	2024-10-05
C-0222	Retail-Plus	Mumbai	IN	2024-08-11
C-0223	Retail-Plus	Mumbai	IN	2024-01-11
C-0224	Retail-Plus	Bengaluru	IN	2023-02-24
C-0225	Retail-Plus	Chennai	IN	2024-08-15
C-0226	Retail-Plus	Mumbai	IN	2023-01-01
C-0227	Retail-Plus	Bengaluru	IN	2023-11-04
C-0228	Retail-Plus	Delhi	IN	2024-08-14
C-0229	Retail-Plus	Bengaluru	IN	2024-02-24
C-0230	Retail-Plus	Bengaluru	IN	2024-12-16
C-0231	Retail-Plus	Pune	IN	2024-05-03
C-0232	Retail-Plus	Bengaluru	IN	2025-05-05
C-0233	Retail-Plus	Pune	IN	2023-05-03
C-0234	Retail-Plus	Hyderabad	IN	2024-01-02
C-0235	Retail-Plus	Mumbai	IN	2024-09-06
C-0236	Retail-Plus	Pune	IN	2024-04-23
C-0237	Retail-Plus	Chennai	IN	2023-12-13
C-0238	Retail-Plus	Delhi	IN	2024-11-14
C-0239	Retail-Plus	Delhi	IN	2025-03-23
C-0240	Retail-Plus	Bengaluru	IN	2025-09-08
C-0241	Retail-Plus	Chennai	IN	2024-11-21
C-0242	Retail-Plus	Mumbai	IN	2023-03-23
C-0243	Retail-Plus	Hyderabad	IN	2023-11-06
C-0244	Retail-Plus	Chennai	IN	2023-01-27
C-0245	Retail-Plus	Mumbai	IN	2024-07-19
C-0246	Retail-Plus	Pune	IN	2025-06-22
C-0247	Retail-Plus	Chennai	IN	2024-06-05
C-0248	Retail-Plus	Chennai	IN	2024-10-28
C-0249	Retail-Plus	Chennai	IN	2025-09-12
C-0250	Retail-Plus	Mumbai	IN	2025-05-03
C-0251	Retail-Plus	Delhi	IN	2024-01-09
C-0252	Retail-Plus	Chennai	IN	2025-03-05
C-0253	Retail-Plus	Pune	IN	2025-10-02
C-0254	Retail-Plus	Pune	IN	2024-09-15
C-0255	Retail-Plus	Mumbai	IN	2023-11-09
C-0256	Retail-Plus	Hyderabad	IN	2023-04-04
C-0257	Retail-Plus	Delhi	IN	2024-10-21
C-0258	Retail-Plus	Mumbai	IN	2024-06-20
C-0259	Retail-Plus	Delhi	IN	2024-07-18
C-0260	Retail-Plus	Bengaluru	IN	2023-12-09
C-0261	Retail-Plus	Delhi	IN	2025-08-12
C-0262	Retail-Plus	Chennai	IN	2024-09-05
C-0263	Retail-Plus	Bengaluru	IN	2025-01-24
C-0264	Retail-Plus	Mumbai	IN	2025-08-01
C-0265	Retail-Plus	Bengaluru	IN	2024-09-27
C-0266	Retail-Plus	Bengaluru	IN	2025-09-24
C-0267	Retail-Plus	Chennai	IN	2024-04-20
C-0268	Retail-Plus	Delhi	IN	2024-09-03
C-0269	Retail-Plus	Bengaluru	IN	2023-08-09
C-0270	Retail-Plus	Delhi	IN	2023-09-09
C-0271	Business	Delhi	IN	2023-08-20
C-0272	Business	Pune	IN	2023-09-11
C-0273	Business	Chennai	IN	2023-12-28
C-0274	Business	Delhi	IN	2025-03-01
C-0275	Business	Mumbai	IN	2024-08-15
C-0276	Business	Chennai	IN	2023-11-08
C-0277	Business	Bengaluru	IN	2023-07-05
C-0278	Business	Delhi	IN	2024-02-21
C-0279	Business	Delhi	IN	2025-04-15
C-0280	Business	Delhi	IN	2024-10-26
C-0281	Business	Delhi	IN	2024-09-27
C-0282	Business	Hyderabad	IN	2024-10-06
C-0283	Business	Chennai	IN	2023-01-17
C-0284	Business	Delhi	IN	2023-04-22
C-0285	Business	Bengaluru	IN	2025-06-20
C-0286	Business	Delhi	IN	2024-06-01
C-0287	Business	Chennai	IN	2023-10-12
C-0288	Business	Delhi	IN	2025-09-15
C-0289	Business	Delhi	IN	2024-04-13
C-0290	Business	Delhi	IN	2023-02-28
C-0291	Business	Pune	IN	2024-12-27
C-0292	Business	Mumbai	IN	2024-02-11
C-0293	Business	Bengaluru	IN	2023-07-06
C-0294	Business	Chennai	IN	2025-10-27
C-0295	Business	Chennai	IN	2025-03-22
C-0296	Business	Bengaluru	IN	2025-10-24
C-0297	Business	Mumbai	IN	2025-10-02
C-0298	Business	Hyderabad	IN	2023-04-14
C-0299	Business	Bengaluru	IN	2024-12-25
C-0300	Business	Bengaluru	IN	2024-09-27
C-0301	Business	Delhi	IN	2024-04-02
C-0302	Business	Delhi	IN	2023-10-25
C-0303	Business	Hyderabad	IN	2025-06-13
C-0304	Business	Pune	IN	2024-07-20
C-0305	Business	Chennai	IN	2024-11-10
C-0306	Business	Pune	IN	2024-09-10
C-0307	Business	Chennai	IN	2025-09-01
C-0308	Business	Pune	IN	2023-01-14
C-0309	Business	Chennai	IN	2023-06-05
C-0310	Business	Chennai	IN	2023-12-09
C-0311	Student	Chennai	IN	2024-10-23
C-0312	Student	Chennai	IN	2023-08-23
C-0313	Student	Chennai	IN	2024-10-02
C-0314	Student	Chennai	IN	2024-11-15
C-0315	Student	Pune	IN	2023-09-19
C-0316	Student	Delhi	IN	2023-03-05
C-0317	Student	Bengaluru	IN	2025-07-13
C-0318	Student	Delhi	IN	2024-12-13
C-0319	Student	Bengaluru	IN	2024-02-06
C-0320	Student	Hyderabad	IN	2023-03-27
C-0321	Student	Mumbai	IN	2023-07-15
C-0322	Student	Chennai	IN	2023-10-01
C-0323	Student	Mumbai	IN	2025-11-08
C-0324	Student	Mumbai	IN	2023-09-06
C-0325	Student	Chennai	IN	2023-09-02
C-0326	Student	Hyderabad	IN	2024-07-27
C-0327	Student	Bengaluru	IN	2025-02-11
C-0328	Student	Delhi	IN	2023-08-16
C-0329	Student	Mumbai	IN	2023-05-11
C-0330	Student	Chennai	IN	2023-05-26
C-0331	Student	Bengaluru	IN	2023-07-24
C-0332	Student	Chennai	IN	2025-03-20
C-0333	Student	Bengaluru	IN	2025-05-05
C-0334	Student	Pune	IN	2023-07-14
C-0335	Student	Pune	IN	2024-12-24
C-0336	Student	Bengaluru	IN	2025-08-03
C-0337	Student	Chennai	IN	2025-01-06
C-0338	Student	Delhi	IN	2025-03-22
C-0339	Student	Mumbai	IN	2023-05-13
C-0340	Student	Mumbai	IN	2025-05-24
\.

COPY orders (order_id, customer_id, order_date, quarter, channel, amount, status) FROM stdin;
KR-00001	C-0316	2026-04-20	Q1	web	520	returned
KR-00002	C-0323	2026-05-19	Q1	app	800	delivered
KR-00003	C-0322	2026-06-08	Q1	store	800	cancelled
KR-00004	C-0325	2026-04-24	Q1	app	1310	delivered
KR-00005	C-0333	2026-05-27	Q1	app	1380	delivered
KR-00006	C-0323	2026-06-25	Q1	app	970	cancelled
KR-00007	C-0315	2026-04-03	Q1	store	1310	delivered
KR-00008	C-0331	2026-05-18	Q1	app	1070	delivered
KR-00009	C-0335	2026-06-20	Q1	app	900	delivered
KR-00010	C-0333	2026-04-27	Q1	web	1450	cancelled
KR-00011	C-0315	2026-05-20	Q1	app	1050	returned
KR-00012	C-0323	2026-06-12	Q1	web	1480	delivered
KR-00013	C-0337	2026-04-09	Q1	app	710	returned
KR-00014	C-0315	2026-05-11	Q1	web	1080	delivered
KR-00015	C-0338	2026-06-06	Q1	web	660	cancelled
KR-00016	C-0338	2026-04-26	Q1	store	610	delivered
KR-00017	C-0329	2026-05-28	Q1	store	860	delivered
KR-00018	C-0313	2026-06-05	Q1	app	940	cancelled
KR-00019	C-0312	2026-04-25	Q1	store	530	delivered
KR-00020	C-0316	2026-05-15	Q1	store	470	delivered
KR-00021	C-0328	2026-06-03	Q1	app	1050	delivered
KR-00022	C-0333	2026-04-16	Q1	app	900	delivered
KR-00023	C-0338	2026-05-17	Q1	app	1470	delivered
KR-00024	C-0325	2026-06-01	Q1	store	1070	delivered
KR-00025	C-0326	2026-04-01	Q1	store	1420	delivered
KR-00026	C-0328	2026-05-26	Q1	web	1040	delivered
KR-00027	C-0316	2026-06-20	Q1	store	870	delivered
KR-00028	C-0283	2026-04-02	Q1	web	635000	delivered
KR-00029	C-0277	2026-05-22	Q1	store	1140000	delivered
KR-00030	C-0287	2026-06-08	Q1	store	212000	cancelled
KR-00031	C-0283	2026-04-13	Q1	web	1647000	returned
KR-00032	C-0290	2026-05-20	Q1	app	1661000	delivered
KR-00033	C-0271	2026-06-08	Q1	app	866000	returned
KR-00034	C-0272	2026-04-22	Q1	app	869000	returned
KR-00035	C-0273	2026-05-02	Q1	web	1197000	delivered
KR-00036	C-0282	2026-06-26	Q1	web	1046000	delivered
KR-00037	C-0304	2026-04-11	Q1	app	1153000	delivered
KR-00038	C-0283	2026-05-10	Q1	app	715000	delivered
KR-00039	C-0280	2026-06-23	Q1	app	881000	delivered
KR-00040	C-0310	2026-04-11	Q1	web	379000	delivered
KR-00041	C-0299	2026-05-27	Q1	store	1282000	delivered
KR-00042	C-0278	2026-06-04	Q1	app	1566000	returned
KR-00043	C-0279	2026-04-18	Q1	app	1245000	delivered
KR-00044	C-0303	2026-05-18	Q1	app	963000	cancelled
KR-00045	C-0306	2026-06-07	Q1	app	1645000	returned
KR-00046	C-0283	2026-04-15	Q1	app	1625000	cancelled
KR-00047	C-0274	2026-05-07	Q1	store	363000	returned
KR-00048	C-0275	2026-06-28	Q1	web	214000	returned
KR-00049	C-0284	2026-04-19	Q1	store	1023000	delivered
KR-00050	C-0291	2026-05-02	Q1	web	1118000	delivered
KR-00051	C-0296	2026-06-21	Q1	web	1648000	returned
KR-00052	C-0288	2026-04-21	Q1	store	1478000	delivered
KR-00053	C-0276	2026-05-06	Q1	web	715000	delivered
KR-00054	C-0308	2026-06-19	Q1	store	1367000	delivered
KR-00055	C-0276	2026-04-27	Q1	store	1407000	delivered
KR-00056	C-0286	2026-05-03	Q1	web	678000	cancelled
KR-00057	C-0296	2026-06-18	Q1	app	247000	returned
KR-00058	C-0282	2026-04-06	Q1	app	522000	returned
KR-00059	C-0280	2026-05-11	Q1	app	1752000	delivered
KR-00060	C-0307	2026-06-05	Q1	web	291000	cancelled
KR-00061	C-0273	2026-04-28	Q1	store	1090000	delivered
KR-00062	C-0285	2026-05-07	Q1	app	940000	cancelled
KR-00063	C-0290	2026-06-16	Q1	web	262000	returned
KR-00064	C-0290	2026-04-05	Q1	store	624000	cancelled
KR-00065	C-0280	2026-05-22	Q1	app	689000	delivered
KR-00066	C-0295	2026-06-06	Q1	store	255000	delivered
KR-00067	C-0274	2026-04-09	Q1	store	436000	delivered
KR-00068	C-0273	2026-05-20	Q1	app	644000	cancelled
KR-00069	C-0302	2026-06-12	Q1	store	1182000	delivered
KR-00070	C-0307	2026-04-14	Q1	store	209000	cancelled
KR-00071	C-0275	2026-05-23	Q1	store	1609000	delivered
KR-00072	C-0283	2026-06-13	Q1	web	1408000	delivered
KR-00073	C-0276	2026-04-15	Q1	web	1442000	delivered
KR-00074	C-0281	2026-05-13	Q1	web	1000000	returned
KR-00075	C-0281	2026-06-10	Q1	web	692000	delivered
KR-00076	C-0272	2026-04-20	Q1	store	1149000	delivered
KR-00077	C-0279	2026-05-08	Q1	app	536000	delivered
KR-00078	C-0294	2026-06-13	Q1	web	1068000	delivered
KR-00079	C-0277	2026-04-08	Q1	app	983000	delivered
KR-00080	C-0307	2026-05-22	Q1	web	518000	cancelled
KR-00081	C-0281	2026-06-08	Q1	web	804000	delivered
KR-00082	C-0292	2026-04-27	Q1	store	316000	delivered
KR-00083	C-0282	2026-05-06	Q1	web	691000	cancelled
KR-00084	C-0272	2026-06-17	Q1	web	1615000	delivered
KR-00085	C-0305	2026-04-07	Q1	web	209000	delivered
KR-00086	C-0276	2026-05-11	Q1	app	356000	delivered
KR-00087	C-0290	2026-06-09	Q1	web	1565000	cancelled
KR-00088	C-0283	2026-04-10	Q1	web	700000	delivered
KR-00089	C-0283	2026-05-15	Q1	app	1029000	cancelled
KR-00090	C-0294	2026-06-03	Q1	web	380000	delivered
KR-00091	C-0296	2026-04-07	Q1	web	425000	cancelled
KR-00092	C-0294	2026-05-13	Q1	app	490000	returned
KR-00093	C-0271	2026-06-08	Q1	web	1671000	returned
KR-00094	C-0273	2026-04-12	Q1	app	1696000	returned
KR-00095	C-0306	2026-05-15	Q1	store	484000	returned
KR-00096	C-0285	2026-06-25	Q1	web	1481000	delivered
KR-00097	C-0308	2026-04-04	Q1	app	438000	returned
KR-00098	C-0283	2026-05-09	Q1	web	360000	returned
KR-00099	C-0302	2026-06-23	Q1	web	567000	returned
KR-00100	C-0282	2026-04-12	Q1	web	400000	delivered
KR-00101	C-0276	2026-05-17	Q1	store	283000	delivered
KR-00102	C-0279	2026-06-01	Q1	store	553000	delivered
KR-00103	C-0298	2026-04-01	Q1	store	880000	returned
KR-00104	C-0279	2026-05-22	Q1	web	1127000	delivered
KR-00105	C-0300	2026-06-02	Q1	app	1720000	delivered
KR-00106	C-0282	2026-04-05	Q1	store	323000	delivered
KR-00107	C-0296	2026-05-16	Q1	web	1526000	delivered
KR-00108	C-0275	2026-06-13	Q1	store	1622000	delivered
KR-00109	C-0271	2026-04-24	Q1	web	636000	returned
KR-00110	C-0283	2026-05-16	Q1	web	366000	returned
KR-00111	C-0276	2026-06-07	Q1	app	1011000	delivered
KR-00112	C-0282	2026-04-04	Q1	web	320000	returned
KR-00113	C-0295	2026-05-09	Q1	web	1485000	delivered
KR-00114	C-0289	2026-06-10	Q1	app	1174000	delivered
KR-00115	C-0286	2026-04-06	Q1	app	768000	delivered
KR-00116	C-0280	2026-05-05	Q1	web	634000	cancelled
KR-00117	C-0287	2026-06-07	Q1	web	494000	returned
KR-00118	C-0299	2026-04-04	Q1	web	1367000	cancelled
KR-00119	C-0282	2026-05-21	Q1	store	346000	delivered
KR-00120	C-0282	2026-06-28	Q1	app	518000	delivered
KR-00121	C-0273	2026-04-23	Q1	web	1799000	delivered
KR-00122	C-0274	2026-05-02	Q1	web	1023000	delivered
KR-00123	C-0271	2026-06-12	Q1	app	799000	delivered
KR-00124	C-0291	2026-04-28	Q1	app	12277440	delivered
KR-00125	C-0161	2026-04-12	Q1	store	3520	delivered
KR-00126	C-0237	2026-05-07	Q1	store	1860	delivered
KR-00127	C-0166	2026-06-12	Q1	store	1520	delivered
KR-00128	C-0247	2026-04-21	Q1	store	2600	delivered
KR-00129	C-0164	2026-05-16	Q1	web	3920	delivered
KR-00130	C-0151	2026-06-09	Q1	app	2200	returned
KR-00131	C-0260	2026-04-21	Q1	app	4450	delivered
KR-00132	C-0185	2026-05-11	Q1	store	3040	delivered
KR-00133	C-0190	2026-06-27	Q1	app	2840	returned
KR-00134	C-0188	2026-04-02	Q1	store	3980	delivered
KR-00135	C-0171	2026-05-24	Q1	app	2210	delivered
KR-00136	C-0265	2026-06-06	Q1	app	3110	delivered
KR-00137	C-0158	2026-04-21	Q1	store	1610	delivered
KR-00138	C-0173	2026-05-10	Q1	web	3410	delivered
KR-00139	C-0260	2026-06-27	Q1	store	3870	cancelled
KR-00140	C-0154	2026-04-22	Q1	app	3130	cancelled
KR-00141	C-0265	2026-05-22	Q1	store	2540	returned
KR-00142	C-0234	2026-06-23	Q1	store	3280	cancelled
KR-00143	C-0261	2026-04-25	Q1	app	1720	cancelled
KR-00144	C-0176	2026-05-25	Q1	app	1310	cancelled
KR-00145	C-0167	2026-06-19	Q1	web	2220	returned
KR-00146	C-0204	2026-04-20	Q1	app	1430	cancelled
KR-00147	C-0173	2026-05-08	Q1	web	3520	returned
KR-00148	C-0176	2026-06-14	Q1	store	1420	delivered
KR-00149	C-0229	2026-04-01	Q1	store	3680	delivered
KR-00150	C-0247	2026-05-24	Q1	store	3840	delivered
KR-00151	C-0185	2026-06-10	Q1	app	2690	delivered
KR-00152	C-0187	2026-04-26	Q1	app	2230	delivered
KR-00153	C-0201	2026-05-03	Q1	store	3840	delivered
KR-00154	C-0250	2026-06-02	Q1	web	2560	delivered
KR-00155	C-0230	2026-04-22	Q1	web	3190	delivered
KR-00156	C-0225	2026-05-11	Q1	store	1970	delivered
KR-00157	C-0174	2026-06-15	Q1	store	2740	delivered
KR-00158	C-0257	2026-04-15	Q1	web	3310	delivered
KR-00159	C-0164	2026-05-07	Q1	store	3230	cancelled
KR-00160	C-0242	2026-06-24	Q1	store	4220	cancelled
KR-00161	C-0197	2026-04-26	Q1	store	1690	delivered
KR-00162	C-0187	2026-05-27	Q1	app	1960	cancelled
KR-00163	C-0169	2026-06-19	Q1	app	1810	cancelled
KR-00164	C-0211	2026-04-18	Q1	web	1220	cancelled
KR-00165	C-0208	2026-05-09	Q1	store	1720	returned
KR-00166	C-0234	2026-06-03	Q1	web	2120	delivered
KR-00167	C-0268	2026-04-28	Q1	store	2100	delivered
KR-00168	C-0227	2026-05-24	Q1	web	4330	delivered
KR-00169	C-0208	2026-06-05	Q1	store	2830	cancelled
KR-00170	C-0184	2026-04-07	Q1	app	1840	delivered
KR-00171	C-0185	2026-05-03	Q1	app	1660	delivered
KR-00172	C-0194	2026-06-01	Q1	store	4500	cancelled
KR-00173	C-0186	2026-04-17	Q1	app	2460	returned
KR-00174	C-0216	2026-05-04	Q1	store	3960	delivered
KR-00175	C-0245	2026-06-27	Q1	web	2760	cancelled
KR-00176	C-0266	2026-04-20	Q1	store	1340	delivered
KR-00177	C-0175	2026-05-17	Q1	app	3640	delivered
KR-00178	C-0179	2026-06-12	Q1	app	1360	delivered
KR-00179	C-0172	2026-04-22	Q1	web	3730	delivered
KR-00180	C-0266	2026-05-13	Q1	store	2370	delivered
KR-00181	C-0242	2026-06-26	Q1	app	3790	delivered
KR-00182	C-0210	2026-04-08	Q1	app	1460	returned
KR-00183	C-0152	2026-05-03	Q1	app	3170	returned
KR-00184	C-0250	2026-06-18	Q1	web	1230	delivered
KR-00185	C-0218	2026-04-12	Q1	app	1320	cancelled
KR-00186	C-0177	2026-05-12	Q1	store	3320	delivered
KR-00187	C-0251	2026-06-19	Q1	web	4300	cancelled
KR-00188	C-0223	2026-04-08	Q1	app	3450	delivered
KR-00189	C-0173	2026-05-26	Q1	app	2390	delivered
KR-00190	C-0191	2026-06-16	Q1	web	3740	cancelled
KR-00191	C-0257	2026-04-13	Q1	app	1320	cancelled
KR-00192	C-0184	2026-05-19	Q1	app	1900	returned
KR-00193	C-0247	2026-06-28	Q1	web	1450	returned
KR-00194	C-0159	2026-04-25	Q1	store	1230	returned
KR-00195	C-0177	2026-05-27	Q1	store	4000	delivered
KR-00196	C-0151	2026-06-16	Q1	store	4090	delivered
KR-00197	C-0191	2026-04-04	Q1	web	3650	delivered
KR-00198	C-0165	2026-05-27	Q1	app	1640	delivered
KR-00199	C-0239	2026-06-02	Q1	app	1820	returned
KR-00200	C-0266	2026-04-26	Q1	app	1250	cancelled
KR-00201	C-0234	2026-05-20	Q1	app	2510	delivered
KR-00202	C-0156	2026-06-18	Q1	app	3370	delivered
KR-00203	C-0177	2026-04-26	Q1	web	2660	delivered
KR-00204	C-0254	2026-05-09	Q1	app	2530	cancelled
KR-00205	C-0152	2026-06-12	Q1	store	3650	returned
KR-00206	C-0173	2026-04-03	Q1	web	3860	delivered
KR-00207	C-0187	2026-05-24	Q1	web	1300	cancelled
KR-00208	C-0219	2026-06-08	Q1	app	1550	delivered
KR-00209	C-0232	2026-04-15	Q1	store	2690	delivered
KR-00210	C-0239	2026-05-26	Q1	store	1610	delivered
KR-00211	C-0254	2026-06-16	Q1	web	1620	delivered
KR-00212	C-0180	2026-04-16	Q1	store	4100	delivered
KR-00213	C-0165	2026-05-10	Q1	web	2040	delivered
KR-00214	C-0160	2026-06-07	Q1	web	2770	delivered
KR-00215	C-0153	2026-04-27	Q1	store	4300	delivered
KR-00216	C-0210	2026-05-16	Q1	web	2350	cancelled
KR-00217	C-0222	2026-06-18	Q1	web	1920	delivered
KR-00218	C-0235	2026-04-13	Q1	app	3270	delivered
KR-00219	C-0179	2026-05-28	Q1	store	2870	cancelled
KR-00220	C-0219	2026-06-05	Q1	app	3760	delivered
KR-00221	C-0230	2026-04-19	Q1	web	2730	delivered
KR-00222	C-0177	2026-05-18	Q1	store	3640	delivered
KR-00223	C-0194	2026-06-10	Q1	store	4080	cancelled
KR-00224	C-0265	2026-04-25	Q1	store	2070	delivered
KR-00225	C-0177	2026-05-06	Q1	web	1540	delivered
KR-00226	C-0178	2026-06-16	Q1	app	1840	cancelled
KR-00227	C-0262	2026-04-07	Q1	app	1310	returned
KR-00228	C-0252	2026-05-06	Q1	app	2430	returned
KR-00229	C-0154	2026-06-10	Q1	store	2990	delivered
KR-00230	C-0162	2026-04-03	Q1	web	2070	delivered
KR-00231	C-0157	2026-05-23	Q1	app	4050	returned
KR-00232	C-0202	2026-06-16	Q1	app	3840	delivered
KR-00233	C-0227	2026-04-10	Q1	app	1920	delivered
KR-00234	C-0252	2026-05-03	Q1	store	3790	returned
KR-00235	C-0155	2026-06-05	Q1	app	1600	delivered
KR-00236	C-0193	2026-04-18	Q1	store	1580	cancelled
KR-00237	C-0167	2026-05-17	Q1	app	1400	delivered
KR-00238	C-0234	2026-06-04	Q1	web	2520	delivered
KR-00239	C-0173	2026-04-18	Q1	web	1240	delivered
KR-00240	C-0179	2026-05-20	Q1	store	1720	returned
KR-00241	C-0184	2026-06-15	Q1	app	2830	returned
KR-00242	C-0183	2026-04-28	Q1	web	3800	cancelled
KR-00243	C-0227	2026-05-03	Q1	store	2430	delivered
KR-00244	C-0227	2026-06-12	Q1	app	3750	delivered
KR-00245	C-0165	2026-04-17	Q1	app	2910	cancelled
KR-00246	C-0158	2026-05-02	Q1	app	3870	delivered
KR-00247	C-0171	2026-06-25	Q1	app	4130	delivered
KR-00248	C-0172	2026-04-27	Q1	web	3130	delivered
KR-00249	C-0190	2026-05-10	Q1	app	4260	delivered
KR-00250	C-0160	2026-06-18	Q1	store	3060	delivered
KR-00251	C-0213	2026-04-14	Q1	store	2190	delivered
KR-00252	C-0184	2026-05-16	Q1	app	2200	delivered
KR-00253	C-0175	2026-06-03	Q1	app	2680	delivered
KR-00254	C-0153	2026-04-25	Q1	store	2580	delivered
KR-00255	C-0239	2026-05-05	Q1	store	3770	delivered
KR-00256	C-0184	2026-06-02	Q1	web	3400	delivered
KR-00257	C-0164	2026-04-07	Q1	app	1840	delivered
KR-00258	C-0244	2026-05-07	Q1	web	1670	delivered
KR-00259	C-0188	2026-06-19	Q1	web	2730	delivered
KR-00260	C-0151	2026-04-22	Q1	store	1400	delivered
KR-00261	C-0219	2026-05-24	Q1	web	2600	returned
KR-00262	C-0188	2026-06-23	Q1	store	1840	delivered
KR-00263	C-0269	2026-04-17	Q1	web	2840	delivered
KR-00264	C-0224	2026-05-18	Q1	app	3800	delivered
KR-00265	C-0152	2026-06-07	Q1	store	2980	delivered
KR-00266	C-0192	2026-04-20	Q1	store	3260	delivered
KR-00267	C-0185	2026-05-05	Q1	web	2290	delivered
KR-00268	C-0152	2026-06-08	Q1	app	1680	delivered
KR-00269	C-0219	2026-04-25	Q1	app	1910	cancelled
KR-00270	C-0157	2026-05-26	Q1	app	2650	returned
KR-00271	C-0219	2026-06-17	Q1	app	4430	delivered
KR-00272	C-0167	2026-04-16	Q1	app	2140	returned
KR-00273	C-0228	2026-05-04	Q1	app	3620	delivered
KR-00274	C-0237	2026-06-08	Q1	app	2700	returned
KR-00275	C-0151	2026-04-13	Q1	app	1240	delivered
KR-00276	C-0162	2026-05-02	Q1	store	1970	delivered
KR-00277	C-0165	2026-06-18	Q1	app	3810	delivered
KR-00278	C-0174	2026-04-03	Q1	store	2600	returned
KR-00279	C-0217	2026-05-22	Q1	app	4080	delivered
KR-00280	C-0174	2026-06-26	Q1	store	3490	delivered
KR-00281	C-0257	2026-04-05	Q1	app	2030	delivered
KR-00282	C-0216	2026-05-06	Q1	store	2480	cancelled
KR-00283	C-0237	2026-06-21	Q1	store	3590	delivered
KR-00284	C-0189	2026-04-27	Q1	web	4460	delivered
KR-00285	C-0226	2026-05-09	Q1	store	1820	delivered
KR-00286	C-0194	2026-06-17	Q1	store	1850	returned
KR-00287	C-0156	2026-04-17	Q1	app	1340	delivered
KR-00288	C-0261	2026-05-15	Q1	web	1610	delivered
KR-00289	C-0229	2026-06-17	Q1	web	2060	delivered
KR-00290	C-0154	2026-04-10	Q1	app	2870	returned
KR-00291	C-0160	2026-05-22	Q1	store	3490	cancelled
KR-00292	C-0183	2026-06-19	Q1	app	4060	delivered
KR-00293	C-0232	2026-04-18	Q1	web	3860	returned
KR-00294	C-0220	2026-05-10	Q1	web	3450	delivered
KR-00295	C-0267	2026-06-05	Q1	store	2200	cancelled
KR-00296	C-0179	2026-04-01	Q1	web	3990	delivered
KR-00297	C-0165	2026-05-21	Q1	store	1730	delivered
KR-00298	C-0187	2026-06-01	Q1	web	2160	delivered
KR-00299	C-0257	2026-04-15	Q1	app	4020	delivered
KR-00300	C-0167	2026-05-23	Q1	web	2160	cancelled
KR-00301	C-0250	2026-06-06	Q1	web	1790	delivered
KR-00302	C-0168	2026-04-15	Q1	app	1600	cancelled
KR-00303	C-0226	2026-05-25	Q1	store	4130	returned
KR-00304	C-0186	2026-06-12	Q1	app	2430	delivered
KR-00305	C-0173	2026-04-02	Q1	app	1750	delivered
KR-00306	C-0209	2026-05-28	Q1	web	4420	cancelled
KR-00307	C-0183	2026-06-20	Q1	web	4330	delivered
KR-00308	C-0238	2026-04-10	Q1	store	3740	delivered
KR-00309	C-0162	2026-05-26	Q1	app	3920	delivered
KR-00310	C-0174	2026-06-05	Q1	web	2760	cancelled
KR-00311	C-0191	2026-04-24	Q1	app	2540	cancelled
KR-00312	C-0223	2026-05-18	Q1	app	3670	delivered
KR-00313	C-0189	2026-06-12	Q1	app	2180	delivered
KR-00314	C-0200	2026-04-05	Q1	app	4010	delivered
KR-00315	C-0182	2026-05-12	Q1	store	3390	delivered
KR-00316	C-0222	2026-06-13	Q1	web	1390	cancelled
KR-00317	C-0252	2026-04-08	Q1	web	2910	delivered
KR-00318	C-0166	2026-05-25	Q1	store	2780	delivered
KR-00319	C-0246	2026-06-11	Q1	store	3650	delivered
KR-00320	C-0259	2026-04-16	Q1	app	2520	delivered
KR-00321	C-0172	2026-05-15	Q1	store	3220	delivered
KR-00322	C-0222	2026-06-24	Q1	app	3260	cancelled
KR-00323	C-0155	2026-04-26	Q1	app	1800	returned
KR-00324	C-0172	2026-05-13	Q1	web	2180	delivered
KR-00325	C-0169	2026-06-14	Q1	web	2430	delivered
KR-00326	C-0210	2026-04-17	Q1	app	1470	delivered
KR-00327	C-0248	2026-05-01	Q1	app	3030	returned
KR-00328	C-0153	2026-06-12	Q1	store	2120	delivered
KR-00329	C-0185	2026-04-21	Q1	app	3880	delivered
KR-00330	C-0183	2026-05-25	Q1	web	1450	cancelled
KR-00331	C-0152	2026-06-11	Q1	web	1920	delivered
KR-00332	C-0176	2026-04-10	Q1	app	3850	delivered
KR-00333	C-0182	2026-05-06	Q1	app	1290	delivered
KR-00334	C-0162	2026-06-09	Q1	web	2540	delivered
KR-00335	C-0159	2026-04-09	Q1	web	3450	delivered
KR-00336	C-0183	2026-05-24	Q1	web	2670	delivered
KR-00337	C-0204	2026-06-04	Q1	store	2920	delivered
KR-00338	C-0210	2026-04-09	Q1	app	2900	delivered
KR-00339	C-0182	2026-05-27	Q1	web	4470	delivered
KR-00340	C-0137	2026-04-08	Q1	web	1870	delivered
KR-00341	C-0144	2026-05-04	Q1	web	1020	cancelled
KR-00342	C-0014	2026-06-14	Q1	store	2240	returned
KR-00343	C-0022	2026-04-08	Q1	web	2790	delivered
KR-00344	C-0077	2026-05-05	Q1	web	930	delivered
KR-00345	C-0009	2026-06-01	Q1	web	2910	returned
KR-00346	C-0140	2026-04-07	Q1	store	2620	delivered
KR-00347	C-0054	2026-05-12	Q1	web	1300	delivered
KR-00348	C-0015	2026-06-06	Q1	store	1480	delivered
KR-00349	C-0035	2026-04-24	Q1	web	1740	delivered
KR-00350	C-0008	2026-05-12	Q1	store	2700	returned
KR-00351	C-0110	2026-06-22	Q1	store	2540	delivered
KR-00352	C-0049	2026-04-15	Q1	app	840	delivered
KR-00353	C-0021	2026-05-28	Q1	app	1380	cancelled
KR-00354	C-0122	2026-06-02	Q1	web	2480	delivered
KR-00355	C-0018	2026-04-28	Q1	store	1430	returned
KR-00356	C-0104	2026-05-11	Q1	web	920	delivered
KR-00357	C-0019	2026-06-26	Q1	app	2360	delivered
KR-00358	C-0001	2026-04-05	Q1	web	1640	delivered
KR-00359	C-0085	2026-05-26	Q1	app	2070	returned
KR-00360	C-0042	2026-06-06	Q1	store	1220	delivered
KR-00361	C-0066	2026-04-27	Q1	web	2580	delivered
KR-00362	C-0009	2026-05-19	Q1	web	2850	cancelled
KR-00363	C-0010	2026-06-04	Q1	web	2070	returned
KR-00364	C-0022	2026-04-13	Q1	store	2590	cancelled
KR-00365	C-0086	2026-05-22	Q1	app	1870	delivered
KR-00366	C-0089	2026-06-07	Q1	app	2560	delivered
KR-00367	C-0093	2026-04-04	Q1	store	1740	delivered
KR-00368	C-0054	2026-05-12	Q1	store	2670	delivered
KR-00369	C-0035	2026-06-10	Q1	store	2760	delivered
KR-00370	C-0115	2026-04-03	Q1	app	1480	delivered
KR-00371	C-0047	2026-05-18	Q1	app	990	returned
KR-00372	C-0126	2026-06-13	Q1	app	1160	delivered
KR-00373	C-0107	2026-04-19	Q1	store	1630	delivered
KR-00374	C-0009	2026-05-13	Q1	app	2910	delivered
KR-00375	C-0123	2026-06-24	Q1	app	3000	delivered
KR-00376	C-0036	2026-04-16	Q1	store	1120	returned
KR-00377	C-0014	2026-05-17	Q1	store	1580	delivered
KR-00378	C-0044	2026-06-11	Q1	app	2760	delivered
KR-00379	C-0128	2026-04-25	Q1	store	1620	delivered
KR-00380	C-0021	2026-05-15	Q1	app	1950	returned
KR-00381	C-0017	2026-06-25	Q1	store	1890	delivered
KR-00382	C-0084	2026-04-05	Q1	web	1780	returned
KR-00383	C-0031	2026-05-09	Q1	store	960	delivered
KR-00384	C-0138	2026-06-15	Q1	app	1480	delivered
KR-00385	C-0091	2026-04-27	Q1	app	2000	delivered
KR-00386	C-0054	2026-05-17	Q1	app	1980	delivered
KR-00387	C-0021	2026-06-22	Q1	app	970	delivered
KR-00388	C-0148	2026-04-08	Q1	store	1340	delivered
KR-00389	C-0034	2026-05-24	Q1	web	2690	delivered
KR-00390	C-0049	2026-06-18	Q1	app	2090	cancelled
KR-00391	C-0028	2026-04-01	Q1	web	1130	delivered
KR-00392	C-0112	2026-05-04	Q1	app	990	delivered
KR-00393	C-0011	2026-06-05	Q1	store	2090	delivered
KR-00394	C-0033	2026-04-19	Q1	web	1690	returned
KR-00395	C-0013	2026-05-12	Q1	store	2920	delivered
KR-00396	C-0010	2026-06-08	Q1	web	1990	delivered
KR-00397	C-0040	2026-04-20	Q1	web	2510	cancelled
KR-00398	C-0026	2026-05-28	Q1	app	2690	returned
KR-00399	C-0031	2026-06-25	Q1	app	1470	delivered
KR-00400	C-0046	2026-04-10	Q1	app	1090	delivered
KR-00401	C-0044	2026-05-09	Q1	web	1340	returned
KR-00402	C-0011	2026-06-14	Q1	app	2950	delivered
KR-00403	C-0124	2026-04-27	Q1	web	2460	delivered
KR-00404	C-0037	2026-05-08	Q1	app	2880	delivered
KR-00405	C-0028	2026-06-18	Q1	store	2620	delivered
KR-00406	C-0044	2026-04-15	Q1	app	1970	cancelled
KR-00407	C-0075	2026-05-26	Q1	store	1840	delivered
KR-00408	C-0038	2026-06-10	Q1	app	2430	delivered
KR-00409	C-0047	2026-04-13	Q1	store	1910	delivered
KR-00410	C-0112	2026-05-05	Q1	app	1040	delivered
KR-00411	C-0088	2026-06-14	Q1	store	960	delivered
KR-00412	C-0005	2026-04-05	Q1	app	1990	returned
KR-00413	C-0002	2026-05-16	Q1	web	1560	cancelled
KR-00414	C-0134	2026-06-20	Q1	store	890	delivered
KR-00415	C-0117	2026-04-19	Q1	web	1760	cancelled
KR-00416	C-0020	2026-05-12	Q1	web	2940	delivered
KR-00417	C-0044	2026-06-07	Q1	web	800	delivered
KR-00418	C-0040	2026-04-05	Q1	store	2930	returned
KR-00419	C-0008	2026-05-06	Q1	web	1520	delivered
KR-00420	C-0112	2026-06-05	Q1	store	1280	delivered
KR-00421	C-0136	2026-04-15	Q1	web	1670	delivered
KR-00422	C-0060	2026-05-20	Q1	app	1470	delivered
KR-00423	C-0099	2026-06-14	Q1	store	1180	delivered
KR-00424	C-0038	2026-04-21	Q1	web	1170	returned
KR-00425	C-0060	2026-05-05	Q1	app	2600	delivered
KR-00426	C-0043	2026-06-09	Q1	app	1660	returned
KR-00427	C-0040	2026-04-27	Q1	web	2540	delivered
KR-00428	C-0017	2026-05-06	Q1	web	2280	delivered
KR-00429	C-0020	2026-06-28	Q1	app	2900	returned
KR-00430	C-0076	2026-04-12	Q1	store	1550	delivered
KR-00431	C-0040	2026-05-20	Q1	app	2110	delivered
KR-00432	C-0111	2026-06-28	Q1	app	2910	delivered
KR-00433	C-0027	2026-04-14	Q1	store	1920	delivered
KR-00434	C-0031	2026-05-11	Q1	app	1840	delivered
KR-00435	C-0023	2026-06-04	Q1	web	1630	cancelled
KR-00436	C-0038	2026-04-28	Q1	web	1090	delivered
KR-00437	C-0026	2026-05-23	Q1	app	2500	delivered
KR-00438	C-0012	2026-06-04	Q1	app	1800	delivered
KR-00439	C-0051	2026-04-15	Q1	web	1960	delivered
KR-00440	C-0020	2026-05-19	Q1	app	850	delivered
KR-00441	C-0102	2026-06-07	Q1	app	2190	returned
KR-00442	C-0100	2026-04-28	Q1	app	2240	returned
KR-00443	C-0073	2026-05-14	Q1	web	1460	delivered
KR-00444	C-0110	2026-06-14	Q1	web	1310	returned
KR-00445	C-0146	2026-04-07	Q1	web	2130	delivered
KR-00446	C-0019	2026-05-25	Q1	web	1120	delivered
KR-00447	C-0003	2026-06-05	Q1	web	990	delivered
KR-00448	C-0104	2026-04-16	Q1	web	2670	delivered
KR-00449	C-0035	2026-05-08	Q1	app	2150	cancelled
KR-00450	C-0047	2026-06-14	Q1	app	2760	delivered
KR-00451	C-0125	2026-04-17	Q1	web	820	cancelled
KR-00452	C-0025	2026-05-05	Q1	store	2340	delivered
KR-00453	C-0020	2026-06-22	Q1	app	2930	returned
KR-00454	C-0007	2026-04-15	Q1	store	2230	returned
KR-00455	C-0025	2026-05-10	Q1	store	2420	delivered
KR-00456	C-0058	2026-06-18	Q1	app	810	delivered
KR-00457	C-0145	2026-04-25	Q1	store	2690	delivered
KR-00458	C-0044	2026-05-26	Q1	store	1190	delivered
KR-00459	C-0033	2026-06-20	Q1	app	2180	delivered
KR-00460	C-0136	2026-04-14	Q1	store	2700	delivered
KR-00461	C-0075	2026-05-12	Q1	app	1490	delivered
KR-00462	C-0002	2026-06-07	Q1	web	1670	cancelled
KR-00463	C-0029	2026-04-18	Q1	store	2600	returned
KR-00464	C-0021	2026-05-18	Q1	store	2560	delivered
KR-00465	C-0019	2026-06-17	Q1	app	1880	delivered
KR-00466	C-0003	2026-04-11	Q1	store	1380	delivered
KR-00467	C-0081	2026-05-21	Q1	web	1070	delivered
KR-00468	C-0078	2026-06-18	Q1	web	1750	delivered
KR-00469	C-0060	2026-04-16	Q1	store	1310	delivered
KR-00470	C-0021	2026-05-26	Q1	app	2300	delivered
KR-00471	C-0133	2026-06-24	Q1	app	2660	returned
KR-00472	C-0094	2026-04-23	Q1	web	2250	delivered
KR-00473	C-0096	2026-05-08	Q1	web	1560	returned
KR-00474	C-0020	2026-06-21	Q1	store	1740	returned
KR-00475	C-0037	2026-04-17	Q1	store	1650	delivered
KR-00476	C-0077	2026-05-12	Q1	store	1620	returned
KR-00477	C-0086	2026-06-07	Q1	web	1110	cancelled
KR-00478	C-0084	2026-04-16	Q1	store	2670	cancelled
KR-00479	C-0127	2026-05-06	Q1	app	1080	delivered
KR-00480	C-0058	2026-06-14	Q1	app	2040	delivered
KR-00481	C-0071	2026-04-13	Q1	web	2090	delivered
KR-00482	C-0089	2026-05-28	Q1	web	2560	delivered
KR-00483	C-0033	2026-06-01	Q1	store	2930	delivered
KR-00484	C-0003	2026-04-03	Q1	store	2470	returned
KR-00485	C-0147	2026-05-24	Q1	web	1590	delivered
KR-00486	C-0026	2026-06-12	Q1	app	2110	delivered
KR-00487	C-0029	2026-04-10	Q1	app	1480	returned
KR-00488	C-0095	2026-05-11	Q1	store	2940	cancelled
KR-00489	C-0020	2026-06-06	Q1	web	2570	delivered
KR-00490	C-0012	2026-04-12	Q1	web	970	delivered
KR-00491	C-0146	2026-05-08	Q1	store	2150	cancelled
KR-00492	C-0144	2026-06-04	Q1	web	1320	cancelled
KR-00493	C-0108	2026-04-11	Q1	web	1270	delivered
KR-00494	C-0007	2026-05-03	Q1	store	1650	delivered
KR-00495	C-0079	2026-06-19	Q1	web	1680	delivered
KR-00496	C-0060	2026-04-03	Q1	store	2050	delivered
KR-00497	C-0008	2026-05-17	Q1	store	2330	cancelled
KR-00498	C-0128	2026-06-24	Q1	app	2170	delivered
KR-00499	C-0084	2026-04-26	Q1	app	1950	delivered
KR-00500	C-0046	2026-05-03	Q1	web	1220	cancelled
KR-00501	C-0040	2026-06-09	Q1	web	1320	cancelled
KR-00502	C-0024	2026-04-09	Q1	store	2710	returned
KR-00503	C-0022	2026-05-03	Q1	store	1260	delivered
KR-00504	C-0003	2026-06-19	Q1	web	1430	returned
KR-00505	C-0012	2026-04-07	Q1	store	2410	cancelled
KR-00506	C-0136	2026-05-22	Q1	web	2540	returned
KR-00507	C-0037	2026-06-25	Q1	web	2300	delivered
KR-00508	C-0103	2026-04-07	Q1	web	1660	delivered
KR-00509	C-0091	2026-05-23	Q1	web	1050	delivered
KR-00510	C-0083	2026-06-25	Q1	web	1480	delivered
KR-00511	C-0010	2026-04-04	Q1	store	1710	delivered
KR-00512	C-0050	2026-05-08	Q1	app	870	delivered
KR-00513	C-0086	2026-06-06	Q1	app	2830	delivered
KR-00514	C-0087	2026-04-27	Q1	app	2970	delivered
KR-00515	C-0051	2026-05-26	Q1	web	1780	delivered
KR-00516	C-0050	2026-06-27	Q1	web	1180	delivered
KR-00517	C-0048	2026-04-27	Q1	web	1640	cancelled
KR-00518	C-0121	2026-05-17	Q1	store	2350	cancelled
KR-00519	C-0068	2026-06-02	Q1	app	1660	delivered
KR-00520	C-0002	2026-04-20	Q1	store	800	delivered
KR-00521	C-0040	2026-05-23	Q1	web	1060	returned
KR-00522	C-0143	2026-06-21	Q1	store	1140	delivered
KR-00523	C-0047	2026-04-08	Q1	app	1280	delivered
KR-00524	C-0127	2026-05-11	Q1	web	890	returned
KR-00525	C-0058	2026-06-06	Q1	store	920	cancelled
KR-00526	C-0036	2026-04-11	Q1	web	2830	delivered
KR-00527	C-0036	2026-05-02	Q1	web	2560	delivered
KR-00528	C-0032	2026-06-22	Q1	web	2510	delivered
KR-00529	C-0119	2026-04-11	Q1	web	1530	delivered
KR-00530	C-0058	2026-05-17	Q1	web	2510	delivered
KR-00531	C-0027	2026-06-13	Q1	app	2000	delivered
KR-00532	C-0031	2026-04-06	Q1	store	800	returned
KR-00533	C-0136	2026-05-07	Q1	store	1220	delivered
KR-00534	C-0018	2026-06-12	Q1	web	1560	delivered
KR-00535	C-0050	2026-04-22	Q1	app	2700	delivered
KR-00536	C-0017	2026-05-18	Q1	app	1970	returned
KR-00537	C-0007	2026-06-08	Q1	app	1270	returned
KR-00538	C-0020	2026-04-06	Q1	store	1330	returned
KR-00539	C-0338	2026-07-08	Q2	web	850	delivered
KR-00540	C-0340	2026-08-20	Q2	store	590	returned
KR-00541	C-0320	2026-09-15	Q2	web	1160	delivered
KR-00542	C-0332	2026-07-27	Q2	app	790	delivered
KR-00543	C-0319	2026-08-09	Q2	store	680	delivered
KR-00544	C-0311	2026-09-01	Q2	app	960	delivered
KR-00545	C-0323	2026-07-24	Q2	app	680	delivered
KR-00546	C-0317	2026-08-19	Q2	app	500	delivered
KR-00547	C-0316	2026-09-27	Q2	app	970	delivered
KR-00548	C-0325	2026-07-26	Q2	app	1200	returned
KR-00549	C-0334	2026-08-25	Q2	app	970	delivered
KR-00550	C-0319	2026-09-16	Q2	web	1480	delivered
KR-00551	C-0314	2026-07-15	Q2	web	1500	delivered
KR-00552	C-0316	2026-08-12	Q2	web	880	delivered
KR-00553	C-0314	2026-09-26	Q2	app	1470	delivered
KR-00554	C-0322	2026-07-01	Q2	web	810	delivered
KR-00555	C-0313	2026-08-15	Q2	app	770	delivered
KR-00556	C-0320	2026-09-08	Q2	store	530	returned
KR-00557	C-0315	2026-07-22	Q2	app	930	delivered
KR-00558	C-0334	2026-08-08	Q2	store	1180	cancelled
KR-00559	C-0340	2026-09-02	Q2	app	1030	delivered
KR-00560	C-0319	2026-07-27	Q2	web	1240	delivered
KR-00561	C-0319	2026-08-24	Q2	app	900	delivered
KR-00562	C-0335	2026-09-21	Q2	store	750	delivered
KR-00563	C-0320	2026-07-20	Q2	app	940	delivered
KR-00564	C-0314	2026-08-18	Q2	store	410	delivered
KR-00565	C-0312	2026-09-05	Q2	app	830	returned
KR-00566	C-0313	2026-07-26	Q2	web	490	delivered
KR-00567	C-0311	2026-08-22	Q2	web	960	returned
KR-00568	C-0329	2026-09-17	Q2	store	960	delivered
KR-00569	C-0317	2026-07-12	Q2	app	650	returned
KR-00570	C-0319	2026-08-07	Q2	store	1410	delivered
KR-00571	C-0315	2026-09-25	Q2	store	1320	returned
KR-00572	C-0332	2026-07-11	Q2	store	550	returned
KR-00573	C-0317	2026-08-11	Q2	web	1300	delivered
KR-00574	C-0311	2026-09-05	Q2	store	640	delivered
KR-00575	C-0336	2026-07-05	Q2	store	1100	delivered
KR-00576	C-0337	2026-08-04	Q2	store	1390	cancelled
KR-00577	C-0278	2026-07-21	Q2	store	927000	delivered
KR-00578	C-0273	2026-08-20	Q2	app	950000	cancelled
KR-00579	C-0310	2026-09-13	Q2	app	750000	cancelled
KR-00580	C-0274	2026-07-22	Q2	store	855000	delivered
KR-00581	C-0276	2026-08-20	Q2	store	1170000	cancelled
KR-00582	C-0289	2026-09-21	Q2	web	770000	delivered
KR-00583	C-0280	2026-07-16	Q2	store	376000	delivered
KR-00584	C-0310	2026-08-28	Q2	app	792000	cancelled
KR-00585	C-0289	2026-09-15	Q2	app	1228000	returned
KR-00586	C-0293	2026-07-25	Q2	app	604000	returned
KR-00587	C-0271	2026-08-25	Q2	store	1310000	returned
KR-00588	C-0284	2026-09-11	Q2	store	831000	returned
KR-00589	C-0294	2026-07-02	Q2	store	1488000	cancelled
KR-00590	C-0273	2026-08-03	Q2	app	1683000	delivered
KR-00591	C-0275	2026-09-06	Q2	web	1123000	returned
KR-00592	C-0293	2026-07-28	Q2	web	517000	delivered
KR-00593	C-0297	2026-08-15	Q2	web	1127000	returned
KR-00594	C-0306	2026-09-10	Q2	store	827000	delivered
KR-00595	C-0295	2026-07-23	Q2	store	401000	delivered
KR-00596	C-0275	2026-08-27	Q2	web	1078000	delivered
KR-00597	C-0280	2026-09-11	Q2	web	1168000	cancelled
KR-00598	C-0276	2026-07-20	Q2	app	1613000	delivered
KR-00599	C-0272	2026-08-21	Q2	store	524000	delivered
KR-00600	C-0306	2026-09-28	Q2	app	481000	delivered
KR-00601	C-0282	2026-07-22	Q2	app	1040000	returned
KR-00602	C-0275	2026-08-09	Q2	app	1299000	delivered
KR-00603	C-0271	2026-09-10	Q2	web	367000	delivered
KR-00604	C-0284	2026-07-22	Q2	web	1042000	returned
KR-00605	C-0294	2026-08-08	Q2	app	279000	cancelled
KR-00606	C-0272	2026-09-16	Q2	store	534000	delivered
KR-00607	C-0282	2026-07-22	Q2	app	221000	returned
KR-00608	C-0281	2026-08-03	Q2	app	917000	delivered
KR-00609	C-0300	2026-09-23	Q2	store	1258000	delivered
KR-00610	C-0280	2026-07-27	Q2	web	278000	cancelled
KR-00611	C-0279	2026-08-03	Q2	web	536000	delivered
KR-00612	C-0280	2026-09-24	Q2	web	354000	cancelled
KR-00613	C-0308	2026-07-19	Q2	web	212000	returned
KR-00614	C-0307	2026-08-18	Q2	web	409000	delivered
KR-00615	C-0284	2026-09-17	Q2	web	636000	delivered
KR-00616	C-0296	2026-07-21	Q2	app	230000	cancelled
KR-00617	C-0293	2026-08-01	Q2	web	1352000	returned
KR-00618	C-0287	2026-09-18	Q2	web	1168000	cancelled
KR-00619	C-0293	2026-07-12	Q2	store	1290000	returned
KR-00620	C-0274	2026-08-18	Q2	store	1074000	delivered
KR-00621	C-0273	2026-09-23	Q2	store	913000	delivered
KR-00622	C-0295	2026-07-16	Q2	store	1312000	delivered
KR-00623	C-0304	2026-08-03	Q2	app	471000	delivered
KR-00624	C-0273	2026-09-17	Q2	web	1089000	delivered
KR-00625	C-0280	2026-07-14	Q2	store	1776000	delivered
KR-00626	C-0304	2026-08-06	Q2	store	1229000	returned
KR-00627	C-0281	2026-09-10	Q2	app	301000	delivered
KR-00628	C-0295	2026-07-27	Q2	store	555000	delivered
KR-00629	C-0288	2026-08-03	Q2	web	580000	cancelled
KR-00630	C-0292	2026-09-07	Q2	web	352000	delivered
KR-00631	C-0290	2026-07-13	Q2	store	431000	returned
KR-00632	C-0280	2026-08-21	Q2	app	273000	delivered
KR-00633	C-0276	2026-09-12	Q2	store	972000	delivered
KR-00634	C-0274	2026-07-07	Q2	web	1001000	delivered
KR-00635	C-0295	2026-08-14	Q2	app	433000	delivered
KR-00636	C-0283	2026-09-15	Q2	app	1778000	returned
KR-00637	C-0288	2026-07-26	Q2	store	1428000	cancelled
KR-00638	C-0303	2026-08-13	Q2	app	573000	delivered
KR-00639	C-0273	2026-09-24	Q2	web	1484000	delivered
KR-00640	C-0307	2026-07-16	Q2	store	1025000	delivered
KR-00641	C-0290	2026-08-11	Q2	store	763000	delivered
KR-00642	C-0279	2026-09-04	Q2	web	525000	delivered
KR-00643	C-0307	2026-07-23	Q2	store	832000	delivered
KR-00644	C-0302	2026-08-05	Q2	web	225000	cancelled
KR-00645	C-0275	2026-09-19	Q2	store	803000	returned
KR-00646	C-0272	2026-07-11	Q2	app	533000	delivered
KR-00647	C-0308	2026-08-01	Q2	app	573000	delivered
KR-00648	C-0275	2026-09-11	Q2	web	468000	delivered
KR-00649	C-0305	2026-07-15	Q2	app	1561000	delivered
KR-00650	C-0279	2026-08-01	Q2	store	1785000	delivered
KR-00651	C-0293	2026-09-27	Q2	web	1187000	delivered
KR-00652	C-0277	2026-07-23	Q2	app	1251000	returned
KR-00653	C-0277	2026-08-16	Q2	web	804000	delivered
KR-00654	C-0278	2026-09-14	Q2	store	1791000	delivered
KR-00655	C-0276	2026-07-11	Q2	web	408000	delivered
KR-00656	C-0305	2026-08-17	Q2	store	983000	returned
KR-00657	C-0306	2026-09-05	Q2	web	1737000	delivered
KR-00658	C-0279	2026-07-08	Q2	store	256000	delivered
KR-00659	C-0275	2026-08-04	Q2	web	1173000	delivered
KR-00660	C-0282	2026-09-25	Q2	app	657000	cancelled
KR-00661	C-0309	2026-07-28	Q2	store	1158000	delivered
KR-00662	C-0286	2026-08-09	Q2	store	1007000	delivered
KR-00663	C-0288	2026-09-11	Q2	app	426000	returned
KR-00664	C-0309	2026-07-27	Q2	app	288000	cancelled
KR-00665	C-0296	2026-08-07	Q2	app	1254000	cancelled
KR-00666	C-0275	2026-09-20	Q2	web	214000	returned
KR-00667	C-0286	2026-07-13	Q2	app	19857600	delivered
KR-00668	C-0161	2026-07-12	Q2	app	4200	returned
KR-00669	C-0161	2026-08-13	Q2	web	3100	delivered
KR-00670	C-0161	2026-09-14	Q2	app	1900	delivered
KR-00671	C-0171	2026-07-12	Q2	web	3800	returned
KR-00672	C-0171	2026-08-13	Q2	app	2600	delivered
KR-00673	C-0171	2026-09-14	Q2	web	1400	returned
KR-00674	C-0175	2026-07-12	Q2	web	4400	delivered
KR-00675	C-0175	2026-08-13	Q2	store	2900	delivered
KR-00676	C-0175	2026-09-14	Q2	web	1600	delivered
KR-00677	C-0213	2026-07-16	Q2	store	2290	cancelled
KR-00678	C-0212	2026-08-05	Q2	store	1230	delivered
KR-00679	C-0239	2026-09-20	Q2	store	2670	delivered
KR-00680	C-0164	2026-07-28	Q2	app	4170	delivered
KR-00681	C-0263	2026-08-21	Q2	app	3690	delivered
KR-00682	C-0160	2026-09-19	Q2	store	2520	cancelled
KR-00683	C-0211	2026-07-16	Q2	store	4360	delivered
KR-00684	C-0181	2026-08-11	Q2	web	2430	cancelled
KR-00685	C-0197	2026-09-23	Q2	store	3600	delivered
KR-00686	C-0238	2026-07-19	Q2	app	2400	cancelled
KR-00687	C-0234	2026-08-19	Q2	store	2930	delivered
KR-00688	C-0213	2026-09-05	Q2	app	1920	delivered
KR-00689	C-0216	2026-07-23	Q2	app	4300	delivered
KR-00690	C-0184	2026-08-26	Q2	app	3490	delivered
KR-00691	C-0269	2026-09-11	Q2	store	1700	delivered
KR-00692	C-0181	2026-07-05	Q2	app	3340	delivered
KR-00693	C-0222	2026-08-12	Q2	web	2820	returned
KR-00694	C-0159	2026-09-21	Q2	web	1660	delivered
KR-00695	C-0154	2026-07-17	Q2	app	3220	returned
KR-00696	C-0157	2026-08-14	Q2	web	2200	delivered
KR-00697	C-0186	2026-09-07	Q2	store	1570	delivered
KR-00698	C-0155	2026-07-19	Q2	app	4410	delivered
KR-00699	C-0189	2026-08-13	Q2	store	3480	delivered
KR-00700	C-0194	2026-09-21	Q2	web	3570	cancelled
KR-00701	C-0198	2026-07-03	Q2	app	1850	delivered
KR-00702	C-0183	2026-08-05	Q2	app	1280	returned
KR-00703	C-0224	2026-09-01	Q2	store	3920	delivered
KR-00704	C-0187	2026-07-07	Q2	store	2530	delivered
KR-00705	C-0206	2026-08-04	Q2	app	3480	delivered
KR-00706	C-0212	2026-09-09	Q2	app	3190	cancelled
KR-00707	C-0177	2026-07-24	Q2	web	4350	delivered
KR-00708	C-0153	2026-08-02	Q2	web	1730	delivered
KR-00709	C-0154	2026-09-12	Q2	store	4150	delivered
KR-00710	C-0236	2026-07-17	Q2	store	4500	returned
KR-00711	C-0173	2026-08-13	Q2	web	4320	returned
KR-00712	C-0167	2026-09-14	Q2	store	3480	delivered
KR-00713	C-0156	2026-07-22	Q2	store	3240	returned
KR-00714	C-0238	2026-08-21	Q2	store	1410	delivered
KR-00715	C-0156	2026-09-11	Q2	app	4120	returned
KR-00716	C-0188	2026-07-02	Q2	store	2660	delivered
KR-00717	C-0151	2026-08-28	Q2	app	2540	returned
KR-00718	C-0170	2026-09-08	Q2	web	3990	delivered
KR-00719	C-0248	2026-07-10	Q2	store	3970	cancelled
KR-00720	C-0197	2026-08-06	Q2	web	1820	delivered
KR-00721	C-0240	2026-09-04	Q2	web	4040	delivered
KR-00722	C-0242	2026-07-12	Q2	app	3350	delivered
KR-00723	C-0188	2026-08-23	Q2	web	4380	delivered
KR-00724	C-0239	2026-09-15	Q2	web	4000	delivered
KR-00725	C-0183	2026-07-13	Q2	web	4150	delivered
KR-00726	C-0167	2026-08-17	Q2	store	3220	delivered
KR-00727	C-0152	2026-09-05	Q2	app	3350	delivered
KR-00728	C-0183	2026-07-21	Q2	web	1710	delivered
KR-00729	C-0151	2026-08-04	Q2	app	4350	cancelled
KR-00730	C-0254	2026-09-04	Q2	web	2230	returned
KR-00731	C-0269	2026-07-05	Q2	web	3430	delivered
KR-00732	C-0169	2026-08-17	Q2	app	2140	delivered
KR-00733	C-0169	2026-09-20	Q2	web	2200	returned
KR-00734	C-0185	2026-07-18	Q2	web	1900	delivered
KR-00735	C-0155	2026-08-16	Q2	web	2740	cancelled
KR-00736	C-0205	2026-09-21	Q2	web	1990	delivered
KR-00737	C-0191	2026-07-26	Q2	store	2210	returned
KR-00738	C-0224	2026-08-25	Q2	app	3790	delivered
KR-00739	C-0185	2026-09-02	Q2	web	1450	returned
KR-00740	C-0181	2026-07-11	Q2	web	1350	delivered
KR-00741	C-0239	2026-08-23	Q2	store	3370	cancelled
KR-00742	C-0231	2026-09-01	Q2	web	1340	delivered
KR-00743	C-0212	2026-07-16	Q2	app	4130	returned
KR-00744	C-0196	2026-08-14	Q2	store	2380	cancelled
KR-00745	C-0219	2026-09-16	Q2	app	1920	delivered
KR-00746	C-0165	2026-07-03	Q2	web	3110	delivered
KR-00747	C-0164	2026-08-03	Q2	app	3490	delivered
KR-00748	C-0245	2026-09-04	Q2	web	1590	cancelled
KR-00749	C-0270	2026-07-17	Q2	web	4330	delivered
KR-00750	C-0181	2026-08-13	Q2	store	1580	delivered
KR-00751	C-0252	2026-09-16	Q2	app	3150	returned
KR-00752	C-0168	2026-07-21	Q2	store	3720	delivered
KR-00753	C-0170	2026-08-21	Q2	store	4150	delivered
KR-00754	C-0174	2026-09-12	Q2	web	3780	returned
KR-00755	C-0184	2026-07-25	Q2	app	4090	returned
KR-00756	C-0186	2026-08-27	Q2	web	2500	delivered
KR-00757	C-0261	2026-09-27	Q2	app	1940	delivered
KR-00758	C-0244	2026-07-12	Q2	store	1300	delivered
KR-00759	C-0205	2026-08-13	Q2	app	3410	delivered
KR-00760	C-0194	2026-09-15	Q2	store	2740	returned
KR-00761	C-0170	2026-07-22	Q2	web	2520	delivered
KR-00762	C-0166	2026-08-07	Q2	store	1520	delivered
KR-00763	C-0212	2026-09-22	Q2	store	2110	delivered
KR-00764	C-0172	2026-07-02	Q2	web	3030	delivered
KR-00765	C-0160	2026-08-27	Q2	web	4160	delivered
KR-00766	C-0219	2026-09-28	Q2	store	4470	delivered
KR-00767	C-0170	2026-07-25	Q2	app	3930	delivered
KR-00768	C-0179	2026-08-06	Q2	store	4150	delivered
KR-00769	C-0264	2026-09-20	Q2	web	3540	delivered
KR-00770	C-0190	2026-07-27	Q2	web	2670	returned
KR-00771	C-0162	2026-08-04	Q2	app	3600	returned
KR-00772	C-0216	2026-09-20	Q2	store	2540	delivered
KR-00773	C-0164	2026-07-02	Q2	web	3090	delivered
KR-00774	C-0208	2026-08-04	Q2	app	2810	delivered
KR-00775	C-0229	2026-09-05	Q2	app	2330	delivered
KR-00776	C-0238	2026-07-11	Q2	store	2060	cancelled
KR-00777	C-0188	2026-08-08	Q2	store	2560	returned
KR-00778	C-0259	2026-09-05	Q2	web	3200	cancelled
KR-00779	C-0167	2026-07-02	Q2	web	3690	delivered
KR-00780	C-0158	2026-08-11	Q2	web	2190	delivered
KR-00781	C-0237	2026-09-12	Q2	store	2030	delivered
KR-00782	C-0151	2026-07-22	Q2	app	2250	delivered
KR-00783	C-0170	2026-08-24	Q2	store	3240	delivered
KR-00784	C-0170	2026-09-15	Q2	store	3910	returned
KR-00785	C-0152	2026-07-23	Q2	app	1610	cancelled
KR-00786	C-0197	2026-08-07	Q2	app	4380	returned
KR-00787	C-0240	2026-09-06	Q2	store	1710	returned
KR-00788	C-0152	2026-07-07	Q2	app	3950	cancelled
KR-00789	C-0156	2026-08-20	Q2	store	2360	returned
KR-00790	C-0163	2026-09-05	Q2	web	1220	delivered
KR-00791	C-0160	2026-07-15	Q2	store	3180	delivered
KR-00792	C-0151	2026-08-04	Q2	app	1770	delivered
KR-00793	C-0152	2026-09-21	Q2	store	3530	returned
KR-00794	C-0180	2026-07-24	Q2	web	3810	delivered
KR-00795	C-0156	2026-08-02	Q2	web	2470	returned
KR-00796	C-0153	2026-09-26	Q2	app	1920	delivered
KR-00797	C-0168	2026-07-20	Q2	web	3200	delivered
KR-00798	C-0167	2026-08-19	Q2	app	4210	cancelled
KR-00799	C-0211	2026-09-06	Q2	app	1970	cancelled
KR-00800	C-0249	2026-07-19	Q2	app	1570	returned
KR-00801	C-0180	2026-08-26	Q2	web	4280	delivered
KR-00802	C-0231	2026-09-11	Q2	app	3570	delivered
KR-00803	C-0243	2026-07-03	Q2	store	1350	cancelled
KR-00804	C-0265	2026-08-28	Q2	app	2980	cancelled
KR-00805	C-0160	2026-09-08	Q2	web	3840	delivered
KR-00806	C-0251	2026-07-14	Q2	web	4490	returned
KR-00807	C-0157	2026-08-05	Q2	web	4010	delivered
KR-00808	C-0003	2026-07-16	Q2	app	2630	delivered
KR-00809	C-0044	2026-08-14	Q2	store	1370	returned
KR-00810	C-0047	2026-09-27	Q2	app	2770	delivered
KR-00811	C-0090	2026-07-14	Q2	web	1900	returned
KR-00812	C-0136	2026-08-22	Q2	app	1340	returned
KR-00813	C-0039	2026-09-18	Q2	store	1110	delivered
KR-00814	C-0011	2026-07-27	Q2	app	1610	cancelled
KR-00815	C-0006	2026-08-28	Q2	app	1770	delivered
KR-00816	C-0031	2026-09-16	Q2	app	1960	cancelled
KR-00817	C-0031	2026-07-19	Q2	store	2790	delivered
KR-00818	C-0041	2026-08-09	Q2	app	830	delivered
KR-00819	C-0040	2026-09-12	Q2	app	2590	delivered
KR-00820	C-0010	2026-07-10	Q2	app	1000	delivered
KR-00821	C-0080	2026-08-26	Q2	store	1020	delivered
KR-00822	C-0011	2026-09-27	Q2	store	1390	returned
KR-00823	C-0030	2026-07-12	Q2	web	950	delivered
KR-00824	C-0035	2026-08-27	Q2	app	2080	returned
KR-00825	C-0018	2026-09-09	Q2	web	1610	delivered
KR-00826	C-0040	2026-07-07	Q2	app	830	delivered
KR-00827	C-0079	2026-08-26	Q2	store	950	delivered
KR-00828	C-0046	2026-09-09	Q2	web	1730	delivered
KR-00829	C-0109	2026-07-19	Q2	app	930	delivered
KR-00830	C-0024	2026-08-05	Q2	store	2920	cancelled
KR-00831	C-0111	2026-09-24	Q2	app	1450	delivered
KR-00832	C-0124	2026-07-22	Q2	app	2920	returned
KR-00833	C-0071	2026-08-03	Q2	web	2750	delivered
KR-00834	C-0029	2026-09-08	Q2	app	840	delivered
KR-00835	C-0039	2026-07-08	Q2	app	1910	delivered
KR-00836	C-0030	2026-08-22	Q2	web	1960	delivered
KR-00837	C-0017	2026-09-05	Q2	web	1200	cancelled
KR-00838	C-0039	2026-07-20	Q2	store	1270	delivered
KR-00839	C-0035	2026-08-03	Q2	web	1140	cancelled
KR-00840	C-0147	2026-09-08	Q2	app	2250	delivered
KR-00841	C-0039	2026-07-17	Q2	web	2810	delivered
KR-00842	C-0006	2026-08-09	Q2	app	2720	cancelled
KR-00843	C-0118	2026-09-12	Q2	app	1300	delivered
KR-00844	C-0047	2026-07-18	Q2	web	2730	delivered
KR-00845	C-0108	2026-08-12	Q2	store	1370	delivered
KR-00846	C-0041	2026-09-04	Q2	web	1870	cancelled
KR-00847	C-0043	2026-07-02	Q2	store	2150	delivered
KR-00848	C-0042	2026-08-22	Q2	app	2810	delivered
KR-00849	C-0023	2026-09-10	Q2	web	2010	cancelled
KR-00850	C-0040	2026-07-21	Q2	app	2510	delivered
KR-00851	C-0044	2026-08-18	Q2	web	1880	delivered
KR-00852	C-0052	2026-09-19	Q2	web	1210	returned
KR-00853	C-0042	2026-07-22	Q2	store	2150	delivered
KR-00854	C-0007	2026-08-11	Q2	app	980	delivered
KR-00855	C-0040	2026-09-06	Q2	web	820	delivered
KR-00856	C-0049	2026-07-08	Q2	web	2690	delivered
KR-00857	C-0003	2026-08-15	Q2	web	810	cancelled
KR-00858	C-0112	2026-09-15	Q2	app	1290	delivered
KR-00859	C-0002	2026-07-05	Q2	app	2670	delivered
KR-00860	C-0128	2026-08-17	Q2	app	1910	delivered
KR-00861	C-0034	2026-09-22	Q2	store	1760	delivered
KR-00862	C-0010	2026-07-16	Q2	web	1830	delivered
KR-00863	C-0098	2026-08-07	Q2	app	2030	cancelled
KR-00864	C-0035	2026-09-15	Q2	store	2430	delivered
KR-00865	C-0053	2026-07-10	Q2	store	1410	delivered
KR-00866	C-0060	2026-08-04	Q2	store	2980	returned
KR-00867	C-0007	2026-09-02	Q2	store	2120	returned
KR-00868	C-0070	2026-07-17	Q2	store	1470	delivered
KR-00869	C-0036	2026-08-14	Q2	store	1340	delivered
KR-00870	C-0024	2026-09-10	Q2	store	1270	delivered
KR-00871	C-0104	2026-07-28	Q2	store	1130	returned
KR-00872	C-0126	2026-08-10	Q2	store	2130	delivered
KR-00873	C-0037	2026-09-07	Q2	web	840	cancelled
KR-00874	C-0137	2026-07-06	Q2	store	2520	delivered
KR-00875	C-0085	2026-08-25	Q2	store	1540	delivered
KR-00876	C-0117	2026-09-24	Q2	app	1400	delivered
KR-00877	C-0032	2026-07-08	Q2	store	1850	delivered
KR-00878	C-0027	2026-08-13	Q2	web	1120	cancelled
KR-00879	C-0041	2026-09-28	Q2	app	1740	delivered
KR-00880	C-0054	2026-07-08	Q2	store	1910	delivered
KR-00881	C-0049	2026-08-12	Q2	store	2550	delivered
KR-00882	C-0019	2026-09-04	Q2	store	1140	cancelled
KR-00883	C-0131	2026-07-03	Q2	web	2650	delivered
KR-00884	C-0026	2026-08-13	Q2	web	2610	delivered
KR-00885	C-0016	2026-09-10	Q2	store	2550	returned
KR-00886	C-0056	2026-07-07	Q2	app	1970	cancelled
KR-00887	C-0021	2026-08-01	Q2	app	950	delivered
KR-00888	C-0072	2026-09-03	Q2	app	2990	cancelled
KR-00889	C-0140	2026-07-01	Q2	web	1850	cancelled
KR-00890	C-0142	2026-08-20	Q2	web	2850	returned
KR-00891	C-0068	2026-09-22	Q2	store	2650	delivered
KR-00892	C-0040	2026-07-04	Q2	web	920	cancelled
KR-00893	C-0108	2026-08-02	Q2	store	860	cancelled
KR-00894	C-0049	2026-09-15	Q2	store	1260	delivered
KR-00895	C-0010	2026-07-12	Q2	web	2920	delivered
KR-00896	C-0045	2026-08-05	Q2	app	2690	delivered
KR-00897	C-0033	2026-09-22	Q2	app	2880	delivered
KR-00898	C-0046	2026-07-23	Q2	store	1670	delivered
KR-00899	C-0095	2026-08-23	Q2	app	1470	delivered
KR-00900	C-0060	2026-09-19	Q2	app	1140	returned
KR-00901	C-0050	2026-07-24	Q2	store	830	delivered
KR-00902	C-0038	2026-08-14	Q2	store	1680	cancelled
KR-00903	C-0124	2026-09-05	Q2	app	1230	cancelled
KR-00904	C-0127	2026-07-10	Q2	web	2030	returned
KR-00905	C-0018	2026-08-11	Q2	app	2830	cancelled
KR-00906	C-0029	2026-09-08	Q2	store	2060	cancelled
KR-00907	C-0111	2026-07-26	Q2	app	2810	delivered
KR-00908	C-0066	2026-08-22	Q2	app	3000	delivered
KR-00909	C-0030	2026-09-15	Q2	app	1270	cancelled
KR-00910	C-0016	2026-07-18	Q2	web	2280	delivered
KR-00911	C-0001	2026-08-06	Q2	app	1200	cancelled
KR-00912	C-0024	2026-09-08	Q2	web	870	cancelled
KR-00913	C-0016	2026-07-16	Q2	web	1950	delivered
KR-00914	C-0092	2026-08-14	Q2	app	1980	delivered
KR-00915	C-0048	2026-09-08	Q2	web	2870	returned
KR-00916	C-0041	2026-07-07	Q2	store	1010	delivered
KR-00917	C-0045	2026-08-10	Q2	app	2510	delivered
KR-00918	C-0006	2026-09-11	Q2	store	2230	delivered
KR-00919	C-0011	2026-07-22	Q2	store	2240	delivered
KR-00920	C-0116	2026-08-14	Q2	web	2630	delivered
KR-00921	C-0066	2026-09-07	Q2	app	960	delivered
KR-00922	C-0146	2026-07-02	Q2	app	2050	delivered
KR-00923	C-0004	2026-08-11	Q2	web	1410	returned
KR-00924	C-0074	2026-09-28	Q2	store	2810	delivered
KR-00925	C-0022	2026-07-06	Q2	web	2220	cancelled
KR-00926	C-0046	2026-08-23	Q2	web	2790	cancelled
KR-00927	C-0132	2026-09-27	Q2	app	1920	delivered
KR-00928	C-0041	2026-07-14	Q2	web	2990	returned
KR-00929	C-0100	2026-08-27	Q2	store	1840	returned
KR-00930	C-0034	2026-09-02	Q2	app	2050	returned
KR-00931	C-0010	2026-07-08	Q2	store	2090	delivered
KR-00932	C-0095	2026-08-01	Q2	app	2600	returned
KR-00933	C-0005	2026-09-09	Q2	store	1910	cancelled
KR-00934	C-0037	2026-07-07	Q2	web	1700	delivered
KR-00935	C-0129	2026-08-06	Q2	app	1620	returned
KR-00936	C-0022	2026-09-24	Q2	web	1300	delivered
KR-00937	C-0050	2026-07-23	Q2	store	1820	delivered
KR-00938	C-0082	2026-08-19	Q2	web	2340	delivered
KR-00939	C-0040	2026-09-21	Q2	app	1110	delivered
KR-00940	C-0030	2026-07-23	Q2	web	1620	returned
KR-00941	C-0010	2026-08-03	Q2	web	2810	cancelled
KR-00942	C-0050	2026-09-16	Q2	web	1320	returned
KR-00943	C-0023	2026-07-05	Q2	app	1320	delivered
KR-00944	C-0041	2026-08-09	Q2	store	1770	delivered
KR-00945	C-0017	2026-09-20	Q2	store	1900	delivered
KR-00946	C-0034	2026-07-27	Q2	store	2930	delivered
KR-00947	C-0010	2026-08-15	Q2	store	1270	delivered
KR-00948	C-0050	2026-09-07	Q2	web	2760	delivered
KR-00949	C-0147	2026-07-03	Q2	store	2530	delivered
KR-00950	C-0127	2026-08-19	Q2	store	1000	cancelled
KR-00951	C-0054	2026-09-11	Q2	app	1090	delivered
KR-00952	C-0014	2026-07-02	Q2	web	1050	delivered
KR-00953	C-0040	2026-08-07	Q2	store	2890	delivered
KR-00954	C-0067	2026-09-04	Q2	app	2120	returned
KR-00955	C-0094	2026-07-09	Q2	app	2910	delivered
KR-00956	C-0089	2026-08-05	Q2	app	2380	cancelled
KR-00957	C-0010	2026-09-24	Q2	web	1990	delivered
KR-00958	C-0131	2026-07-05	Q2	app	2050	cancelled
KR-00959	C-0116	2026-08-04	Q2	app	2140	delivered
KR-00960	C-0023	2026-09-16	Q2	app	1240	delivered
KR-00961	C-0042	2026-07-01	Q2	web	1730	returned
KR-00962	C-0040	2026-08-17	Q2	store	1880	delivered
KR-00963	C-0070	2026-09-25	Q2	store	1260	delivered
KR-00964	C-0011	2026-07-18	Q2	store	1220	delivered
KR-00965	C-0033	2026-08-10	Q2	store	1280	returned
KR-00966	C-0041	2026-09-23	Q2	web	2250	cancelled
KR-00967	C-0037	2026-07-11	Q2	web	2870	delivered
KR-00968	C-0118	2026-08-24	Q2	store	2290	delivered
KR-00969	C-0005	2026-09-19	Q2	web	1070	returned
KR-00970	C-0103	2026-07-23	Q2	store	2770	delivered
KR-00971	C-0044	2026-08-17	Q2	store	1290	delivered
KR-00972	C-0015	2026-09-10	Q2	store	1400	delivered
KR-00973	C-0033	2026-07-02	Q2	store	1990	delivered
KR-00974	C-0091	2026-08-02	Q2	web	2180	cancelled
KR-00975	C-0029	2026-09-12	Q2	app	2950	cancelled
KR-00976	C-0011	2026-07-19	Q2	web	2470	delivered
KR-00977	C-0121	2026-08-02	Q2	web	2930	delivered
KR-00978	C-0142	2026-09-06	Q2	web	2900	delivered
KR-00979	C-0092	2026-07-22	Q2	store	970	delivered
KR-00980	C-0032	2026-08-22	Q2	web	1160	cancelled
KR-00981	C-0032	2026-09-23	Q2	store	1920	delivered
KR-00982	C-0017	2026-07-16	Q2	store	2460	delivered
KR-00983	C-0051	2026-08-26	Q2	store	2640	delivered
KR-00984	C-0096	2026-09-25	Q2	store	1650	returned
KR-00985	C-0139	2026-07-28	Q2	app	2310	delivered
KR-00986	C-0033	2026-08-17	Q2	web	1530	cancelled
KR-00987	C-0113	2026-09-17	Q2	app	1400	cancelled
KR-00988	C-0013	2026-07-02	Q2	store	1400	delivered
KR-00989	C-0006	2026-08-09	Q2	app	2910	delivered
KR-00990	C-0111	2026-09-22	Q2	store	1600	delivered
KR-00991	C-0132	2026-07-20	Q2	web	2620	delivered
KR-00992	C-0150	2026-08-18	Q2	store	2410	delivered
KR-00993	C-0139	2026-09-11	Q2	store	2710	delivered
KR-00994	C-0004	2026-07-09	Q2	app	1710	delivered
KR-00995	C-0013	2026-08-22	Q2	store	2870	delivered
KR-00996	C-0121	2026-09-21	Q2	app	1190	delivered
KR-00997	C-0113	2026-07-07	Q2	web	2900	delivered
KR-00998	C-0108	2026-08-05	Q2	store	870	delivered
KR-00999	C-0108	2026-09-16	Q2	web	880	delivered
KR-01000	C-0033	2026-07-17	Q2	web	1430	delivered
\.

COPY campaigns (campaign_id, name, start_date, end_date, segment) FROM stdin;
CMP-MONSOON-26	Monsoon Sale	2026-08-05	2026-08-19	Retail-Plus
\.

COPY payments (payment_id, order_id, paid_date, amount, method, instalment_no) FROM stdin;
P-00001	KR-00001	2026-04-22	520	card	1
P-00002	KR-00001	2026-04-22	520	card	1
P-00003	KR-00002	2026-05-21	800	card	1
P-00004	KR-00002	2026-05-21	800	card	1
P-00005	KR-00003	2026-06-10	800	card	1
P-00006	KR-00003	2026-06-10	800	card	1
P-00007	KR-00004	2026-04-26	1310	card	1
P-00008	KR-00005	2026-05-28	1380	upi	1
P-00009	KR-00006	2026-06-27	970	card	1
P-00010	KR-00007	2026-04-05	1310	netbanking	1
P-00011	KR-00008	2026-05-20	1070	card	1
P-00012	KR-00009	2026-06-22	900	card	1
P-00013	KR-00009	2026-06-22	900	card	1
P-00014	KR-00010	2026-04-28	1450	card	1
P-00015	KR-00011	2026-05-22	1050	upi	1
P-00016	KR-00012	2026-06-14	1480	netbanking	1
P-00017	KR-00013	2026-04-11	710	card	1
P-00018	KR-00013	2026-04-11	710	card	1
P-00019	KR-00014	2026-05-13	1080	wallet	1
P-00020	KR-00015	2026-06-08	660	card	1
P-00021	KR-00015	2026-06-08	660	card	1
P-00022	KR-00016	2026-04-28	610	card	1
P-00023	KR-00016	2026-04-28	610	card	1
P-00024	KR-00017	2026-05-28	860	card	1
P-00025	KR-00017	2026-05-28	860	card	1
P-00026	KR-00018	2026-06-07	940	wallet	1
P-00027	KR-00019	2026-04-27	530	card	1
P-00028	KR-00019	2026-04-27	530	card	1
P-00029	KR-00020	2026-05-17	470	card	1
P-00030	KR-00020	2026-05-17	470	card	1
P-00031	KR-00021	2026-06-05	1050	card	1
P-00032	KR-00022	2026-04-18	900	card	1
P-00033	KR-00022	2026-04-18	900	card	1
P-00034	KR-00023	2026-05-19	1470	upi	1
P-00035	KR-00024	2026-06-03	1070	upi	1
P-00036	KR-00025	2026-04-03	1420	netbanking	1
P-00037	KR-00026	2026-05-28	1040	card	1
P-00038	KR-00027	2026-06-22	870	card	1
P-00039	KR-00027	2026-06-22	870	card	1
P-00040	KR-00028	2026-04-04	381000	netbanking	1
P-00041	KR-00028	2026-04-04	254000	upi	2
P-00042	KR-00029	2026-05-24	684000	upi	1
P-00043	KR-00029	2026-05-24	456000	upi	2
P-00044	KR-00030	2026-06-10	127200	upi	1
P-00045	KR-00030	2026-06-10	84800	upi	2
P-00046	KR-00031	2026-04-15	988200	upi	1
P-00047	KR-00031	2026-04-15	658800	upi	2
P-00048	KR-00032	2026-05-22	996600	wallet	1
P-00049	KR-00032	2026-05-22	664400	netbanking	2
P-00050	KR-00033	2026-06-10	519600	upi	1
P-00051	KR-00033	2026-06-10	346400	wallet	2
P-00052	KR-00034	2026-04-24	521400	upi	1
P-00053	KR-00034	2026-04-24	347600	wallet	2
P-00054	KR-00035	2026-05-04	718200	upi	1
P-00055	KR-00035	2026-05-04	478800	card	2
P-00056	KR-00036	2026-06-28	627600	netbanking	1
P-00057	KR-00036	2026-06-28	418400	wallet	2
P-00058	KR-00037	2026-04-13	691800	card	1
P-00059	KR-00037	2026-04-13	461200	netbanking	2
P-00060	KR-00038	2026-05-12	429000	card	1
P-00061	KR-00038	2026-05-12	286000	card	2
P-00062	KR-00039	2026-06-25	528600	card	1
P-00063	KR-00039	2026-06-25	352400	upi	2
P-00064	KR-00040	2026-04-13	227400	card	1
P-00065	KR-00040	2026-04-13	151600	netbanking	2
P-00066	KR-00041	2026-05-28	769200	netbanking	1
P-00067	KR-00041	2026-05-28	512800	card	2
P-00068	KR-00042	2026-06-06	939600	wallet	1
P-00069	KR-00042	2026-06-06	626400	card	2
P-00070	KR-00043	2026-04-20	747000	wallet	1
P-00071	KR-00043	2026-04-20	498000	netbanking	2
P-00072	KR-00044	2026-05-20	577800	netbanking	1
P-00073	KR-00044	2026-05-20	385200	upi	2
P-00074	KR-00045	2026-06-09	987000	netbanking	1
P-00075	KR-00045	2026-06-09	658000	upi	2
P-00076	KR-00046	2026-04-17	975000	wallet	1
P-00077	KR-00046	2026-04-17	650000	card	2
P-00078	KR-00047	2026-05-09	217800	card	1
P-00079	KR-00047	2026-05-09	145200	card	2
P-00080	KR-00048	2026-06-28	128400	upi	1
P-00081	KR-00048	2026-06-28	85600	netbanking	2
P-00082	KR-00049	2026-04-21	613800	netbanking	1
P-00083	KR-00049	2026-04-21	409200	wallet	2
P-00084	KR-00050	2026-05-04	670800	card	1
P-00085	KR-00050	2026-05-04	447200	card	2
P-00086	KR-00051	2026-06-23	988800	wallet	1
P-00087	KR-00051	2026-06-23	659200	card	2
P-00088	KR-00052	2026-04-23	886800	upi	1
P-00089	KR-00052	2026-04-23	591200	netbanking	2
P-00090	KR-00053	2026-05-08	429000	wallet	1
P-00091	KR-00053	2026-05-08	286000	upi	2
P-00092	KR-00054	2026-06-21	820200	netbanking	1
P-00093	KR-00054	2026-06-21	546800	upi	2
P-00094	KR-00055	2026-04-28	844200	netbanking	1
P-00095	KR-00055	2026-04-28	562800	card	2
P-00096	KR-00056	2026-05-05	406800	wallet	1
P-00097	KR-00056	2026-05-05	271200	card	2
P-00098	KR-00057	2026-06-20	148200	card	1
P-00099	KR-00057	2026-06-20	98800	card	2
P-00100	KR-00058	2026-04-08	313200	upi	1
P-00101	KR-00058	2026-04-08	208800	wallet	2
P-00102	KR-00059	2026-05-13	1051200	card	1
P-00103	KR-00059	2026-05-13	700800	netbanking	2
P-00104	KR-00060	2026-06-07	174600	upi	1
P-00105	KR-00060	2026-06-07	116400	netbanking	2
P-00106	KR-00061	2026-04-28	654000	netbanking	1
P-00107	KR-00061	2026-04-28	436000	netbanking	2
P-00108	KR-00062	2026-05-09	564000	wallet	1
P-00109	KR-00062	2026-05-09	376000	upi	2
P-00110	KR-00063	2026-06-18	157200	card	1
P-00111	KR-00063	2026-06-18	104800	card	2
P-00112	KR-00064	2026-04-07	374400	wallet	1
P-00113	KR-00064	2026-04-07	249600	netbanking	2
P-00114	KR-00065	2026-05-24	413400	wallet	1
P-00115	KR-00065	2026-05-24	275600	wallet	2
P-00116	KR-00066	2026-06-08	153000	card	1
P-00117	KR-00066	2026-06-08	102000	netbanking	2
P-00118	KR-00067	2026-04-11	261600	wallet	1
P-00119	KR-00067	2026-04-11	174400	card	2
P-00120	KR-00068	2026-05-22	386400	card	1
P-00121	KR-00068	2026-05-22	257600	netbanking	2
P-00122	KR-00069	2026-06-14	709200	upi	1
P-00123	KR-00069	2026-06-14	472800	card	2
P-00124	KR-00070	2026-04-16	125400	netbanking	1
P-00125	KR-00070	2026-04-16	83600	netbanking	2
P-00126	KR-00071	2026-05-25	965400	netbanking	1
P-00127	KR-00071	2026-05-25	643600	wallet	2
P-00128	KR-00072	2026-06-15	844800	wallet	1
P-00129	KR-00072	2026-06-15	563200	wallet	2
P-00130	KR-00073	2026-04-17	865200	wallet	1
P-00131	KR-00073	2026-04-17	576800	upi	2
P-00132	KR-00074	2026-05-15	600000	card	1
P-00133	KR-00074	2026-05-15	400000	netbanking	2
P-00134	KR-00075	2026-06-12	415200	upi	1
P-00135	KR-00075	2026-06-12	276800	wallet	2
P-00136	KR-00076	2026-04-22	689400	wallet	1
P-00137	KR-00076	2026-04-22	459600	upi	2
P-00138	KR-00077	2026-05-10	321600	wallet	1
P-00139	KR-00077	2026-05-10	214400	card	2
P-00140	KR-00078	2026-06-15	640800	card	1
P-00141	KR-00078	2026-06-15	427200	netbanking	2
P-00142	KR-00079	2026-04-10	589800	netbanking	1
P-00143	KR-00079	2026-04-10	393200	upi	2
P-00144	KR-00080	2026-05-24	310800	card	1
P-00145	KR-00080	2026-05-24	207200	wallet	2
P-00146	KR-00081	2026-06-10	482400	card	1
P-00147	KR-00081	2026-06-10	321600	card	2
P-00148	KR-00082	2026-04-28	189600	upi	1
P-00149	KR-00082	2026-04-28	126400	netbanking	2
P-00150	KR-00083	2026-05-08	414600	card	1
P-00151	KR-00083	2026-05-08	276400	card	2
P-00152	KR-00084	2026-06-19	969000	netbanking	1
P-00153	KR-00084	2026-06-19	646000	netbanking	2
P-00154	KR-00085	2026-04-09	125400	wallet	1
P-00155	KR-00085	2026-04-09	83600	wallet	2
P-00156	KR-00086	2026-05-13	213600	wallet	1
P-00157	KR-00086	2026-05-13	142400	netbanking	2
P-00158	KR-00087	2026-06-11	939000	upi	1
P-00159	KR-00087	2026-06-11	626000	card	2
P-00160	KR-00088	2026-04-12	420000	card	1
P-00161	KR-00088	2026-04-12	280000	upi	2
P-00162	KR-00089	2026-05-17	617400	upi	1
P-00163	KR-00089	2026-05-17	411600	netbanking	2
P-00164	KR-00090	2026-06-05	228000	wallet	1
P-00165	KR-00090	2026-06-05	152000	netbanking	2
P-00166	KR-00091	2026-04-09	255000	card	1
P-00167	KR-00091	2026-04-09	170000	upi	2
P-00168	KR-00092	2026-05-15	294000	upi	1
P-00169	KR-00092	2026-05-15	196000	upi	2
P-00170	KR-00093	2026-06-10	1002600	wallet	1
P-00171	KR-00093	2026-06-10	668400	upi	2
P-00172	KR-00094	2026-04-14	1017600	upi	1
P-00173	KR-00094	2026-04-14	678400	card	2
P-00174	KR-00095	2026-05-17	290400	upi	1
P-00175	KR-00095	2026-05-17	193600	netbanking	2
P-00176	KR-00096	2026-06-27	888600	wallet	1
P-00177	KR-00096	2026-06-27	592400	card	2
P-00178	KR-00097	2026-04-06	262800	netbanking	1
P-00179	KR-00097	2026-04-06	175200	wallet	2
P-00180	KR-00098	2026-05-11	216000	card	1
P-00181	KR-00098	2026-05-11	144000	netbanking	2
P-00182	KR-00099	2026-06-25	340200	netbanking	1
P-00183	KR-00099	2026-06-25	226800	upi	2
P-00184	KR-00100	2026-04-14	240000	card	1
P-00185	KR-00100	2026-04-14	160000	upi	2
P-00186	KR-00101	2026-05-19	169800	upi	1
P-00187	KR-00101	2026-05-19	113200	card	2
P-00188	KR-00102	2026-06-03	331800	upi	1
P-00189	KR-00102	2026-06-03	221200	wallet	2
P-00190	KR-00103	2026-04-03	528000	upi	1
P-00191	KR-00103	2026-04-03	352000	wallet	2
P-00192	KR-00104	2026-05-24	676200	wallet	1
P-00193	KR-00104	2026-05-24	450800	upi	2
P-00194	KR-00105	2026-06-04	1032000	card	1
P-00195	KR-00105	2026-06-04	688000	wallet	2
P-00196	KR-00106	2026-04-07	193800	netbanking	1
P-00197	KR-00106	2026-04-07	129200	wallet	2
P-00198	KR-00107	2026-05-18	915600	card	1
P-00199	KR-00107	2026-05-18	610400	card	2
P-00200	KR-00108	2026-06-15	973200	card	1
P-00201	KR-00108	2026-06-15	648800	netbanking	2
P-00202	KR-00109	2026-04-26	381600	card	1
P-00203	KR-00109	2026-04-26	254400	wallet	2
P-00204	KR-00110	2026-05-18	219600	upi	1
P-00205	KR-00110	2026-05-18	146400	wallet	2
P-00206	KR-00111	2026-06-09	606600	wallet	1
P-00207	KR-00111	2026-06-09	404400	netbanking	2
P-00208	KR-00112	2026-04-06	192000	wallet	1
P-00209	KR-00112	2026-04-06	128000	card	2
P-00210	KR-00113	2026-05-11	891000	upi	1
P-00211	KR-00113	2026-05-11	594000	wallet	2
P-00212	KR-00114	2026-06-12	704400	upi	1
P-00213	KR-00114	2026-06-12	469600	netbanking	2
P-00214	KR-00115	2026-04-08	460800	wallet	1
P-00215	KR-00115	2026-04-08	307200	netbanking	2
P-00216	KR-00116	2026-05-07	380400	card	1
P-00217	KR-00116	2026-05-07	253600	upi	2
P-00218	KR-00117	2026-06-09	296400	netbanking	1
P-00219	KR-00117	2026-06-09	197600	netbanking	2
P-00220	KR-00118	2026-04-06	820200	upi	1
P-00221	KR-00118	2026-04-06	546800	upi	2
P-00222	KR-00119	2026-05-23	207600	netbanking	1
P-00223	KR-00119	2026-05-23	138400	netbanking	2
P-00224	KR-00120	2026-06-28	310800	upi	1
P-00225	KR-00120	2026-06-28	207200	netbanking	2
P-00226	KR-00121	2026-04-25	1079400	upi	1
P-00227	KR-00121	2026-04-25	719600	wallet	2
P-00228	KR-00122	2026-05-04	613800	card	1
P-00229	KR-00122	2026-05-04	409200	upi	2
P-00230	KR-00123	2026-06-14	479400	netbanking	1
P-00231	KR-00123	2026-06-14	319600	card	2
P-00232	KR-00124	2026-04-28	7366464	upi	1
P-00233	KR-00124	2026-04-28	4910976	netbanking	2
P-00234	KR-00125	2026-04-14	2112	netbanking	1
P-00235	KR-00125	2026-04-14	1408	wallet	2
P-00236	KR-00126	2026-05-09	1860	card	1
P-00237	KR-00127	2026-06-14	1520	card	1
P-00238	KR-00128	2026-04-23	2600	card	1
P-00239	KR-00129	2026-05-18	2352	upi	1
P-00240	KR-00129	2026-05-18	1568	netbanking	2
P-00241	KR-00130	2026-06-11	2200	netbanking	1
P-00242	KR-00131	2026-04-23	2670	upi	1
P-00243	KR-00131	2026-04-23	1780	card	2
P-00244	KR-00132	2026-05-13	1824	card	1
P-00245	KR-00132	2026-05-13	1216	upi	2
P-00246	KR-00133	2026-06-28	1704	upi	1
P-00247	KR-00133	2026-06-28	1136	netbanking	2
P-00248	KR-00134	2026-04-04	2388	wallet	1
P-00249	KR-00134	2026-04-04	1592	wallet	2
P-00250	KR-00135	2026-05-26	2210	wallet	1
P-00251	KR-00136	2026-06-08	1866	netbanking	1
P-00252	KR-00136	2026-06-08	1244	card	2
P-00253	KR-00137	2026-04-23	1610	upi	1
P-00254	KR-00138	2026-05-12	2046	card	1
P-00255	KR-00138	2026-05-12	1364	card	2
P-00256	KR-00139	2026-06-28	2322	upi	1
P-00257	KR-00139	2026-06-28	1548	netbanking	2
P-00258	KR-00140	2026-04-24	1878	netbanking	1
P-00259	KR-00140	2026-04-24	1252	upi	2
P-00260	KR-00141	2026-05-24	2540	upi	1
P-00261	KR-00142	2026-06-25	1968	wallet	1
P-00262	KR-00142	2026-06-25	1312	card	2
P-00263	KR-00143	2026-04-27	1720	netbanking	1
P-00264	KR-00144	2026-05-27	1310	card	1
P-00265	KR-00145	2026-06-21	2220	netbanking	1
P-00266	KR-00146	2026-04-22	1430	upi	1
P-00267	KR-00147	2026-05-10	2112	wallet	1
P-00268	KR-00147	2026-05-10	1408	wallet	2
P-00269	KR-00148	2026-06-16	1420	wallet	1
P-00270	KR-00149	2026-04-03	2208	upi	1
P-00271	KR-00149	2026-04-03	1472	card	2
P-00272	KR-00150	2026-05-26	2304	upi	1
P-00273	KR-00150	2026-05-26	1536	wallet	2
P-00274	KR-00151	2026-06-12	2690	wallet	1
P-00275	KR-00152	2026-04-28	2230	wallet	1
P-00276	KR-00153	2026-05-05	2304	wallet	1
P-00277	KR-00153	2026-05-05	1536	netbanking	2
P-00278	KR-00154	2026-06-04	2560	wallet	1
P-00279	KR-00155	2026-04-24	1914	netbanking	1
P-00280	KR-00155	2026-04-24	1276	upi	2
P-00281	KR-00156	2026-05-13	1970	card	1
P-00282	KR-00157	2026-06-17	2740	netbanking	1
P-00283	KR-00158	2026-04-17	1986	wallet	1
P-00284	KR-00158	2026-04-17	1324	upi	2
P-00285	KR-00159	2026-05-09	1938	upi	1
P-00286	KR-00159	2026-05-09	1292	netbanking	2
P-00287	KR-00160	2026-06-26	2532	wallet	1
P-00288	KR-00160	2026-06-26	1688	netbanking	2
P-00289	KR-00161	2026-04-28	1690	wallet	1
P-00290	KR-00162	2026-05-28	1960	upi	1
P-00291	KR-00163	2026-06-21	1810	wallet	1
P-00292	KR-00164	2026-04-20	1220	wallet	1
P-00293	KR-00165	2026-05-11	1720	wallet	1
P-00294	KR-00166	2026-06-05	2120	card	1
P-00295	KR-00167	2026-04-28	2100	upi	1
P-00296	KR-00168	2026-05-26	2598	wallet	1
P-00297	KR-00168	2026-05-26	1732	upi	2
P-00298	KR-00169	2026-06-07	1698	netbanking	1
P-00299	KR-00169	2026-06-07	1132	netbanking	2
P-00300	KR-00170	2026-04-09	1840	card	1
P-00301	KR-00171	2026-05-05	1660	wallet	1
P-00302	KR-00172	2026-06-03	2700	upi	1
P-00303	KR-00172	2026-06-03	1800	netbanking	2
P-00304	KR-00173	2026-04-19	2460	netbanking	1
P-00305	KR-00174	2026-05-06	2376	wallet	1
P-00306	KR-00174	2026-05-06	1584	wallet	2
P-00307	KR-00175	2026-06-28	2760	card	1
P-00308	KR-00176	2026-04-22	1340	upi	1
P-00309	KR-00177	2026-05-19	2184	upi	1
P-00310	KR-00177	2026-05-19	1456	netbanking	2
P-00311	KR-00178	2026-06-14	1360	netbanking	1
P-00312	KR-00179	2026-04-24	2238	upi	1
P-00313	KR-00179	2026-04-24	1492	upi	2
P-00314	KR-00180	2026-05-15	2370	upi	1
P-00315	KR-00181	2026-06-28	2274	wallet	1
P-00316	KR-00181	2026-06-28	1516	card	2
P-00317	KR-00182	2026-04-10	1460	netbanking	1
P-00318	KR-00183	2026-05-05	1902	wallet	1
P-00319	KR-00183	2026-05-05	1268	upi	2
P-00320	KR-00184	2026-06-20	1230	wallet	1
P-00321	KR-00185	2026-04-14	1320	upi	1
P-00322	KR-00186	2026-05-14	1992	netbanking	1
P-00323	KR-00186	2026-05-14	1328	wallet	2
P-00324	KR-00187	2026-06-21	2580	netbanking	1
P-00325	KR-00187	2026-06-21	1720	wallet	2
P-00326	KR-00188	2026-04-10	2070	netbanking	1
P-00327	KR-00188	2026-04-10	1380	wallet	2
P-00328	KR-00189	2026-05-28	2390	netbanking	1
P-00329	KR-00190	2026-06-18	2244	card	1
P-00330	KR-00190	2026-06-18	1496	netbanking	2
P-00331	KR-00191	2026-04-15	1320	card	1
P-00332	KR-00192	2026-05-21	1900	upi	1
P-00333	KR-00193	2026-06-28	1450	netbanking	1
P-00334	KR-00194	2026-04-27	1230	netbanking	1
P-00335	KR-00195	2026-05-28	2400	upi	1
P-00336	KR-00195	2026-05-28	1600	upi	2
P-00337	KR-00196	2026-06-18	2454	wallet	1
P-00338	KR-00196	2026-06-18	1636	netbanking	2
P-00339	KR-00197	2026-04-06	2190	wallet	1
P-00340	KR-00197	2026-04-06	1460	upi	2
P-00341	KR-00198	2026-05-28	1640	wallet	1
P-00342	KR-00199	2026-06-04	1820	wallet	1
P-00343	KR-00200	2026-04-28	1250	card	1
P-00344	KR-00201	2026-05-22	2510	netbanking	1
P-00345	KR-00202	2026-06-20	2022	upi	1
P-00346	KR-00202	2026-06-20	1348	upi	2
P-00347	KR-00203	2026-04-28	2660	card	1
P-00348	KR-00204	2026-05-11	2530	wallet	1
P-00349	KR-00205	2026-06-14	2190	upi	1
P-00350	KR-00205	2026-06-14	1460	upi	2
P-00351	KR-00206	2026-04-05	2316	upi	1
P-00352	KR-00206	2026-04-05	1544	card	2
P-00353	KR-00207	2026-05-26	1300	wallet	1
P-00354	KR-00208	2026-06-10	1550	wallet	1
P-00355	KR-00209	2026-04-17	2690	upi	1
P-00356	KR-00210	2026-05-28	1610	netbanking	1
P-00357	KR-00211	2026-06-18	1620	wallet	1
P-00358	KR-00212	2026-04-18	2460	upi	1
P-00359	KR-00212	2026-04-18	1640	card	2
P-00360	KR-00213	2026-05-12	2040	card	1
P-00361	KR-00214	2026-06-09	2770	card	1
P-00362	KR-00215	2026-04-28	2580	card	1
P-00363	KR-00215	2026-04-28	1720	card	2
P-00364	KR-00216	2026-05-18	2350	netbanking	1
P-00365	KR-00217	2026-06-20	1920	wallet	1
P-00366	KR-00218	2026-04-15	1962	card	1
P-00367	KR-00218	2026-04-15	1308	netbanking	2
P-00368	KR-00219	2026-05-28	1722	upi	1
P-00369	KR-00219	2026-05-28	1148	upi	2
P-00370	KR-00220	2026-06-07	2256	card	1
P-00371	KR-00220	2026-06-07	1504	upi	2
P-00372	KR-00221	2026-04-21	2730	wallet	1
P-00373	KR-00222	2026-05-20	2184	wallet	1
P-00374	KR-00222	2026-05-20	1456	card	2
P-00375	KR-00223	2026-06-12	2448	netbanking	1
P-00376	KR-00223	2026-06-12	1632	netbanking	2
P-00377	KR-00224	2026-04-27	2070	upi	1
P-00378	KR-00225	2026-05-08	1540	wallet	1
P-00379	KR-00226	2026-06-18	1840	wallet	1
P-00380	KR-00227	2026-04-09	1310	upi	1
P-00381	KR-00228	2026-05-08	2430	wallet	1
P-00382	KR-00229	2026-06-12	1794	upi	1
P-00383	KR-00229	2026-06-12	1196	netbanking	2
P-00384	KR-00230	2026-04-05	2070	wallet	1
P-00385	KR-00231	2026-05-25	2430	netbanking	1
P-00386	KR-00231	2026-05-25	1620	upi	2
P-00387	KR-00232	2026-06-18	2304	card	1
P-00388	KR-00232	2026-06-18	1536	card	2
P-00389	KR-00233	2026-04-12	1920	card	1
P-00390	KR-00234	2026-05-05	2274	card	1
P-00391	KR-00234	2026-05-05	1516	wallet	2
P-00392	KR-00235	2026-06-07	1600	card	1
P-00393	KR-00236	2026-04-20	1580	upi	1
P-00394	KR-00237	2026-05-19	1400	wallet	1
P-00395	KR-00238	2026-06-06	2520	upi	1
P-00396	KR-00239	2026-04-20	1240	upi	1
P-00397	KR-00240	2026-05-22	1720	card	1
P-00398	KR-00241	2026-06-17	1698	wallet	1
P-00399	KR-00241	2026-06-17	1132	upi	2
P-00400	KR-00242	2026-04-28	2280	upi	1
P-00401	KR-00242	2026-04-28	1520	card	2
P-00402	KR-00243	2026-05-05	2430	netbanking	1
P-00403	KR-00244	2026-06-14	2250	wallet	1
P-00404	KR-00244	2026-06-14	1500	netbanking	2
P-00405	KR-00245	2026-04-19	1746	netbanking	1
P-00406	KR-00245	2026-04-19	1164	upi	2
P-00407	KR-00246	2026-05-04	2322	upi	1
P-00408	KR-00246	2026-05-04	1548	card	2
P-00409	KR-00247	2026-06-27	2478	wallet	1
P-00410	KR-00247	2026-06-27	1652	upi	2
P-00411	KR-00248	2026-04-28	1878	upi	1
P-00412	KR-00248	2026-04-28	1252	card	2
P-00413	KR-00249	2026-05-12	2556	wallet	1
P-00414	KR-00249	2026-05-12	1704	wallet	2
P-00415	KR-00250	2026-06-20	1836	netbanking	1
P-00416	KR-00250	2026-06-20	1224	card	2
P-00417	KR-00251	2026-04-16	2190	wallet	1
P-00418	KR-00252	2026-05-18	2200	upi	1
P-00419	KR-00253	2026-06-05	2680	wallet	1
P-00420	KR-00254	2026-04-27	2580	netbanking	1
P-00421	KR-00255	2026-05-07	2262	upi	1
P-00422	KR-00255	2026-05-07	1508	wallet	2
P-00423	KR-00256	2026-06-04	2040	netbanking	1
P-00424	KR-00256	2026-06-04	1360	netbanking	2
P-00425	KR-00257	2026-04-09	1840	card	1
P-00426	KR-00258	2026-05-09	1670	netbanking	1
P-00427	KR-00259	2026-06-21	2730	card	1
P-00428	KR-00260	2026-04-24	1400	wallet	1
P-00429	KR-00261	2026-05-26	2600	wallet	1
P-00430	KR-00262	2026-06-25	1840	upi	1
P-00431	KR-00263	2026-04-19	1704	card	1
P-00432	KR-00263	2026-04-19	1136	card	2
P-00433	KR-00264	2026-05-20	2280	upi	1
P-00434	KR-00264	2026-05-20	1520	netbanking	2
P-00435	KR-00265	2026-06-09	1788	netbanking	1
P-00436	KR-00265	2026-06-09	1192	upi	2
P-00437	KR-00266	2026-04-22	1956	card	1
P-00438	KR-00266	2026-04-22	1304	card	2
P-00439	KR-00267	2026-05-07	2290	wallet	1
P-00440	KR-00268	2026-06-10	1680	netbanking	1
P-00441	KR-00269	2026-04-27	1910	netbanking	1
P-00442	KR-00270	2026-05-28	2650	wallet	1
P-00443	KR-00271	2026-06-19	2658	card	1
P-00444	KR-00271	2026-06-19	1772	wallet	2
P-00445	KR-00272	2026-04-18	2140	wallet	1
P-00446	KR-00273	2026-05-06	2172	netbanking	1
P-00447	KR-00273	2026-05-06	1448	netbanking	2
P-00448	KR-00274	2026-06-10	2700	netbanking	1
P-00449	KR-00275	2026-04-15	1240	upi	1
P-00450	KR-00276	2026-05-04	1970	wallet	1
P-00451	KR-00277	2026-06-20	2286	upi	1
P-00452	KR-00277	2026-06-20	1524	card	2
P-00453	KR-00278	2026-04-05	2600	netbanking	1
P-00454	KR-00279	2026-05-24	2448	card	1
P-00455	KR-00279	2026-05-24	1632	netbanking	2
P-00456	KR-00280	2026-06-28	2094	card	1
P-00457	KR-00280	2026-06-28	1396	netbanking	2
P-00458	KR-00281	2026-04-07	2030	netbanking	1
P-00459	KR-00282	2026-05-08	2480	card	1
P-00460	KR-00283	2026-06-23	2154	wallet	1
P-00461	KR-00283	2026-06-23	1436	wallet	2
P-00462	KR-00284	2026-04-28	2676	wallet	1
P-00463	KR-00284	2026-04-28	1784	card	2
P-00464	KR-00285	2026-05-11	1820	netbanking	1
P-00465	KR-00286	2026-06-19	1850	card	1
P-00466	KR-00287	2026-04-19	1340	netbanking	1
P-00467	KR-00288	2026-05-17	1610	upi	1
P-00468	KR-00289	2026-06-19	2060	wallet	1
P-00469	KR-00290	2026-04-12	1722	wallet	1
P-00470	KR-00290	2026-04-12	1148	netbanking	2
P-00471	KR-00291	2026-05-24	2094	netbanking	1
P-00472	KR-00291	2026-05-24	1396	netbanking	2
P-00473	KR-00292	2026-06-21	2436	upi	1
P-00474	KR-00292	2026-06-21	1624	upi	2
P-00475	KR-00293	2026-04-20	2316	netbanking	1
P-00476	KR-00293	2026-04-20	1544	card	2
P-00477	KR-00294	2026-05-12	2070	upi	1
P-00478	KR-00294	2026-05-12	1380	netbanking	2
P-00479	KR-00295	2026-06-07	2200	card	1
P-00480	KR-00296	2026-04-03	2394	netbanking	1
P-00481	KR-00296	2026-04-03	1596	upi	2
P-00482	KR-00297	2026-05-23	1730	card	1
P-00483	KR-00298	2026-06-03	2160	upi	1
P-00484	KR-00299	2026-04-17	2412	upi	1
P-00485	KR-00299	2026-04-17	1608	card	2
P-00486	KR-00300	2026-05-25	2160	wallet	1
P-00487	KR-00301	2026-06-08	1790	wallet	1
P-00488	KR-00302	2026-04-17	1600	card	1
P-00489	KR-00303	2026-05-27	2478	upi	1
P-00490	KR-00303	2026-05-27	1652	wallet	2
P-00491	KR-00304	2026-06-14	2430	netbanking	1
P-00492	KR-00305	2026-04-04	1750	netbanking	1
P-00493	KR-00306	2026-05-28	2652	wallet	1
P-00494	KR-00306	2026-05-28	1768	netbanking	2
P-00495	KR-00307	2026-06-22	2598	netbanking	1
P-00496	KR-00307	2026-06-22	1732	netbanking	2
P-00497	KR-00308	2026-04-12	2244	upi	1
P-00498	KR-00308	2026-04-12	1496	card	2
P-00499	KR-00309	2026-05-28	2352	netbanking	1
P-00500	KR-00309	2026-05-28	1568	wallet	2
P-00501	KR-00310	2026-06-07	2760	upi	1
P-00502	KR-00311	2026-04-26	2540	netbanking	1
P-00503	KR-00312	2026-05-20	2202	wallet	1
P-00504	KR-00312	2026-05-20	1468	card	2
P-00505	KR-00313	2026-06-14	2180	wallet	1
P-00506	KR-00314	2026-04-07	2406	netbanking	1
P-00507	KR-00314	2026-04-07	1604	wallet	2
P-00508	KR-00315	2026-05-14	2034	wallet	1
P-00509	KR-00315	2026-05-14	1356	wallet	2
P-00510	KR-00316	2026-06-15	1390	upi	1
P-00511	KR-00317	2026-04-10	1746	netbanking	1
P-00512	KR-00317	2026-04-10	1164	upi	2
P-00513	KR-00318	2026-05-27	2780	netbanking	1
P-00514	KR-00319	2026-06-13	2190	netbanking	1
P-00515	KR-00319	2026-06-13	1460	card	2
P-00516	KR-00320	2026-04-18	2520	card	1
P-00517	KR-00321	2026-05-17	1932	netbanking	1
P-00518	KR-00321	2026-05-17	1288	wallet	2
P-00519	KR-00322	2026-06-26	1956	netbanking	1
P-00520	KR-00322	2026-06-26	1304	wallet	2
P-00521	KR-00323	2026-04-28	1800	card	1
P-00522	KR-00324	2026-05-15	2180	upi	1
P-00523	KR-00325	2026-06-16	2430	upi	1
P-00524	KR-00326	2026-04-19	1470	netbanking	1
P-00525	KR-00327	2026-05-03	1818	upi	1
P-00526	KR-00327	2026-05-03	1212	upi	2
P-00527	KR-00328	2026-06-14	2120	netbanking	1
P-00528	KR-00329	2026-04-23	2328	wallet	1
P-00529	KR-00329	2026-04-23	1552	upi	2
P-00530	KR-00330	2026-05-27	1450	netbanking	1
P-00531	KR-00331	2026-06-13	1920	upi	1
P-00532	KR-00332	2026-04-12	2310	wallet	1
P-00533	KR-00332	2026-04-12	1540	netbanking	2
P-00534	KR-00333	2026-05-08	1290	netbanking	1
P-00535	KR-00334	2026-06-11	2540	wallet	1
P-00536	KR-00335	2026-04-11	2070	card	1
P-00537	KR-00335	2026-04-11	1380	card	2
P-00538	KR-00336	2026-05-26	2670	upi	1
P-00539	KR-00337	2026-06-06	1752	upi	1
P-00540	KR-00337	2026-06-06	1168	wallet	2
P-00541	KR-00338	2026-04-11	1740	netbanking	1
P-00542	KR-00338	2026-04-11	1160	card	2
P-00543	KR-00339	2026-05-28	2682	wallet	1
P-00544	KR-00339	2026-05-28	1788	card	2
P-00545	KR-00340	2026-04-10	1870	card	1
P-00546	KR-00341	2026-05-06	1020	upi	1
P-00547	KR-00342	2026-06-16	2240	netbanking	1
P-00548	KR-00343	2026-04-10	1674	card	1
P-00549	KR-00343	2026-04-10	1116	wallet	2
P-00550	KR-00344	2026-05-07	930	card	1
P-00551	KR-00345	2026-06-03	1746	wallet	1
P-00552	KR-00345	2026-06-03	1164	upi	2
P-00553	KR-00346	2026-04-09	2620	wallet	1
P-00554	KR-00347	2026-05-14	1300	upi	1
P-00555	KR-00348	2026-06-08	1480	netbanking	1
P-00556	KR-00349	2026-04-26	1740	wallet	1
P-00557	KR-00350	2026-05-14	2700	upi	1
P-00558	KR-00351	2026-06-24	2540	wallet	1
P-00559	KR-00352	2026-04-17	840	card	1
P-00560	KR-00352	2026-04-17	840	card	1
P-00561	KR-00353	2026-05-28	1380	upi	1
P-00562	KR-00354	2026-06-04	2480	upi	1
P-00563	KR-00355	2026-04-28	1430	upi	1
P-00564	KR-00356	2026-05-13	920	wallet	1
P-00565	KR-00357	2026-06-28	2360	upi	1
P-00566	KR-00358	2026-04-07	1640	netbanking	1
P-00567	KR-00359	2026-05-28	2070	card	1
P-00568	KR-00360	2026-06-08	1220	wallet	1
P-00569	KR-00361	2026-04-28	2580	wallet	1
P-00570	KR-00362	2026-05-21	1710	card	1
P-00571	KR-00362	2026-05-21	1140	card	2
P-00572	KR-00363	2026-06-06	2070	card	1
P-00573	KR-00364	2026-04-15	2590	wallet	1
P-00574	KR-00365	2026-05-24	1870	upi	1
P-00575	KR-00366	2026-06-09	2560	wallet	1
P-00576	KR-00367	2026-04-06	1740	upi	1
P-00577	KR-00368	2026-05-14	2670	upi	1
P-00578	KR-00369	2026-06-12	2760	upi	1
P-00579	KR-00370	2026-04-05	1480	card	1
P-00580	KR-00371	2026-05-20	990	upi	1
P-00581	KR-00372	2026-06-15	1160	wallet	1
P-00582	KR-00373	2026-04-21	1630	card	1
P-00583	KR-00374	2026-05-15	1746	netbanking	1
P-00584	KR-00374	2026-05-15	1164	wallet	2
P-00585	KR-00375	2026-06-26	1800	wallet	1
P-00586	KR-00375	2026-06-26	1200	card	2
P-00587	KR-00376	2026-04-18	1120	wallet	1
P-00588	KR-00377	2026-05-19	1580	upi	1
P-00589	KR-00378	2026-06-13	2760	card	1
P-00590	KR-00379	2026-04-27	1620	netbanking	1
P-00591	KR-00380	2026-05-17	1950	netbanking	1
P-00592	KR-00381	2026-06-27	1890	upi	1
P-00593	KR-00382	2026-04-07	1780	card	1
P-00594	KR-00383	2026-05-11	960	card	1
P-00595	KR-00384	2026-06-17	1480	wallet	1
P-00596	KR-00385	2026-04-28	2000	netbanking	1
P-00597	KR-00386	2026-05-19	1980	card	1
P-00598	KR-00387	2026-06-24	970	upi	1
P-00599	KR-00388	2026-04-10	1340	netbanking	1
P-00600	KR-00389	2026-05-26	2690	wallet	1
P-00601	KR-00390	2026-06-20	2090	netbanking	1
P-00602	KR-00391	2026-04-03	1130	card	1
P-00603	KR-00392	2026-05-06	990	card	1
P-00604	KR-00393	2026-06-07	2090	wallet	1
P-00605	KR-00394	2026-04-21	1690	upi	1
P-00606	KR-00395	2026-05-14	1752	wallet	1
P-00607	KR-00395	2026-05-14	1168	netbanking	2
P-00608	KR-00396	2026-06-10	1990	upi	1
P-00609	KR-00397	2026-04-22	2510	netbanking	1
P-00610	KR-00398	2026-05-28	2690	card	1
P-00611	KR-00399	2026-06-27	1470	card	1
P-00612	KR-00400	2026-04-12	1090	card	1
P-00613	KR-00401	2026-05-11	1340	card	1
P-00614	KR-00402	2026-06-16	1770	netbanking	1
P-00615	KR-00402	2026-06-16	1180	card	2
P-00616	KR-00403	2026-04-28	2460	wallet	1
P-00617	KR-00404	2026-05-10	1728	wallet	1
P-00618	KR-00404	2026-05-10	1152	card	2
P-00619	KR-00405	2026-06-20	2620	wallet	1
P-00620	KR-00406	2026-04-17	1970	netbanking	1
P-00621	KR-00407	2026-05-28	1840	card	1
P-00622	KR-00408	2026-06-12	2430	upi	1
P-00623	KR-00409	2026-04-15	1910	card	1
P-00624	KR-00410	2026-05-07	1040	card	1
P-00625	KR-00411	2026-06-16	960	card	1
P-00626	KR-00412	2026-04-07	1990	card	1
P-00627	KR-00413	2026-05-18	1560	card	1
P-00628	KR-00414	2026-06-22	890	card	1
P-00629	KR-00414	2026-06-22	890	card	1
P-00630	KR-00415	2026-04-21	1760	card	1
P-00631	KR-00416	2026-05-14	1764	wallet	1
P-00632	KR-00416	2026-05-14	1176	card	2
P-00633	KR-00417	2026-06-09	800	card	1
P-00634	KR-00417	2026-06-09	800	card	1
P-00635	KR-00418	2026-04-07	1758	upi	1
P-00636	KR-00418	2026-04-07	1172	netbanking	2
P-00637	KR-00419	2026-05-08	1520	card	1
P-00638	KR-00420	2026-06-07	1280	wallet	1
P-00639	KR-00421	2026-04-17	1670	netbanking	1
P-00640	KR-00422	2026-05-22	1470	upi	1
P-00641	KR-00423	2026-06-16	1180	upi	1
P-00642	KR-00424	2026-04-23	1170	wallet	1
P-00643	KR-00425	2026-05-07	2600	card	1
P-00644	KR-00426	2026-06-11	1660	netbanking	1
P-00645	KR-00427	2026-04-28	2540	card	1
P-00646	KR-00428	2026-05-08	2280	wallet	1
P-00647	KR-00429	2026-06-28	1740	card	1
P-00648	KR-00429	2026-06-28	1160	netbanking	2
P-00649	KR-00430	2026-04-14	1550	card	1
P-00650	KR-00431	2026-05-22	2110	upi	1
P-00651	KR-00432	2026-06-28	1746	wallet	1
P-00652	KR-00432	2026-06-28	1164	upi	2
P-00653	KR-00433	2026-04-16	1920	netbanking	1
P-00654	KR-00434	2026-05-13	1840	netbanking	1
P-00655	KR-00435	2026-06-06	1630	upi	1
P-00656	KR-00436	2026-04-28	1090	netbanking	1
P-00657	KR-00437	2026-05-25	2500	netbanking	1
P-00658	KR-00438	2026-06-06	1800	card	1
P-00659	KR-00439	2026-04-17	1960	upi	1
P-00660	KR-00440	2026-05-21	850	card	1
P-00661	KR-00440	2026-05-21	850	card	1
P-00662	KR-00441	2026-06-09	2190	netbanking	1
P-00663	KR-00442	2026-04-28	2240	netbanking	1
P-00664	KR-00443	2026-05-16	1460	netbanking	1
P-00665	KR-00444	2026-06-16	1310	wallet	1
P-00666	KR-00445	2026-04-09	2130	netbanking	1
P-00667	KR-00446	2026-05-27	1120	card	1
P-00668	KR-00447	2026-06-07	990	wallet	1
P-00669	KR-00448	2026-04-18	2670	upi	1
P-00670	KR-00449	2026-05-10	2150	wallet	1
P-00671	KR-00450	2026-06-16	2760	netbanking	1
P-00672	KR-00451	2026-04-19	820	card	1
P-00673	KR-00451	2026-04-19	820	card	1
P-00674	KR-00452	2026-05-07	2340	card	1
P-00675	KR-00453	2026-06-24	1758	netbanking	1
P-00676	KR-00453	2026-06-24	1172	netbanking	2
P-00677	KR-00454	2026-04-17	2230	netbanking	1
P-00678	KR-00455	2026-05-12	2420	upi	1
P-00679	KR-00456	2026-06-20	810	card	1
P-00680	KR-00456	2026-06-20	810	card	1
P-00681	KR-00457	2026-04-27	2690	card	1
P-00682	KR-00458	2026-05-28	1190	wallet	1
P-00683	KR-00459	2026-06-22	2180	netbanking	1
P-00684	KR-00460	2026-04-16	2700	upi	1
P-00685	KR-00461	2026-05-14	1490	card	1
P-00686	KR-00462	2026-06-09	1670	upi	1
P-00687	KR-00463	2026-04-20	2600	wallet	1
P-00688	KR-00464	2026-05-20	2560	card	1
P-00689	KR-00465	2026-06-19	1880	card	1
P-00690	KR-00466	2026-04-13	1380	card	1
P-00691	KR-00467	2026-05-23	1070	wallet	1
P-00692	KR-00468	2026-06-20	1750	wallet	1
P-00693	KR-00469	2026-04-18	1310	card	1
P-00694	KR-00470	2026-05-28	2300	card	1
P-00695	KR-00471	2026-06-26	2660	wallet	1
P-00696	KR-00472	2026-04-25	2250	card	1
P-00697	KR-00473	2026-05-10	1560	card	1
P-00698	KR-00474	2026-06-23	1740	card	1
P-00699	KR-00475	2026-04-19	1650	netbanking	1
P-00700	KR-00476	2026-05-14	1620	upi	1
P-00701	KR-00477	2026-06-09	1110	upi	1
P-00702	KR-00478	2026-04-18	2670	wallet	1
P-00703	KR-00479	2026-05-08	1080	upi	1
P-00704	KR-00480	2026-06-16	2040	wallet	1
P-00705	KR-00481	2026-04-15	2090	netbanking	1
P-00706	KR-00482	2026-05-28	2560	card	1
P-00707	KR-00483	2026-06-03	1758	card	1
P-00708	KR-00483	2026-06-03	1172	upi	2
P-00709	KR-00484	2026-04-05	2470	wallet	1
P-00710	KR-00485	2026-05-26	1590	netbanking	1
P-00711	KR-00486	2026-06-14	2110	card	1
P-00712	KR-00487	2026-04-12	1480	netbanking	1
P-00713	KR-00488	2026-05-13	1764	netbanking	1
P-00714	KR-00488	2026-05-13	1176	netbanking	2
P-00715	KR-00489	2026-06-08	2570	card	1
P-00716	KR-00490	2026-04-14	970	upi	1
P-00717	KR-00491	2026-05-10	2150	wallet	1
P-00718	KR-00492	2026-06-06	1320	card	1
P-00719	KR-00493	2026-04-13	1270	upi	1
P-00720	KR-00494	2026-05-05	1650	netbanking	1
P-00721	KR-00495	2026-06-21	1680	upi	1
P-00722	KR-00496	2026-04-05	2050	upi	1
P-00723	KR-00497	2026-05-19	2330	netbanking	1
P-00724	KR-00498	2026-06-26	2170	wallet	1
P-00725	KR-00499	2026-04-28	1950	upi	1
P-00726	KR-00500	2026-05-05	1220	wallet	1
P-00727	KR-00501	2026-06-11	1320	netbanking	1
P-00728	KR-00502	2026-04-11	2710	card	1
P-00729	KR-00503	2026-05-05	1260	wallet	1
P-00730	KR-00504	2026-06-21	1430	upi	1
P-00731	KR-00505	2026-04-09	2410	netbanking	1
P-00732	KR-00506	2026-05-24	2540	netbanking	1
P-00733	KR-00507	2026-06-27	2300	netbanking	1
P-00734	KR-00508	2026-04-09	1660	wallet	1
P-00735	KR-00509	2026-05-25	1050	wallet	1
P-00736	KR-00510	2026-06-27	1480	netbanking	1
P-00737	KR-00511	2026-04-06	1710	netbanking	1
P-00738	KR-00512	2026-05-10	870	card	1
P-00739	KR-00512	2026-05-10	870	card	1
P-00740	KR-00513	2026-06-08	1698	wallet	1
P-00741	KR-00513	2026-06-08	1132	upi	2
P-00742	KR-00514	2026-04-28	1782	wallet	1
P-00743	KR-00514	2026-04-28	1188	netbanking	2
P-00744	KR-00515	2026-05-28	1780	upi	1
P-00745	KR-00516	2026-06-28	1180	wallet	1
P-00746	KR-00517	2026-04-28	1640	card	1
P-00747	KR-00518	2026-05-19	2350	upi	1
P-00748	KR-00519	2026-06-04	1660	wallet	1
P-00749	KR-00520	2026-04-22	800	card	1
P-00750	KR-00520	2026-04-22	800	card	1
P-00751	KR-00521	2026-05-25	1060	card	1
P-00752	KR-00522	2026-06-23	1140	netbanking	1
P-00753	KR-00523	2026-04-10	1280	card	1
P-00754	KR-00524	2026-05-13	890	card	1
P-00755	KR-00524	2026-05-13	890	card	1
P-00756	KR-00525	2026-06-08	920	wallet	1
P-00757	KR-00526	2026-04-13	1698	netbanking	1
P-00758	KR-00526	2026-04-13	1132	card	2
P-00759	KR-00527	2026-05-04	2560	netbanking	1
P-00760	KR-00528	2026-06-24	2510	wallet	1
P-00761	KR-00529	2026-04-13	1530	upi	1
P-00762	KR-00530	2026-05-19	2510	card	1
P-00763	KR-00531	2026-06-15	2000	card	1
P-00764	KR-00532	2026-04-08	800	card	1
P-00765	KR-00532	2026-04-08	800	card	1
P-00766	KR-00533	2026-05-09	1220	wallet	1
P-00767	KR-00534	2026-06-14	1560	netbanking	1
P-00768	KR-00535	2026-04-24	2700	wallet	1
P-00769	KR-00536	2026-05-20	1970	card	1
P-00770	KR-00537	2026-06-10	1270	netbanking	1
P-00771	KR-00538	2026-04-08	1330	upi	1
P-00772	KR-00539	2026-07-10	850	card	1
P-00773	KR-00539	2026-07-10	850	card	1
P-00774	KR-00540	2026-08-22	590	card	1
P-00775	KR-00540	2026-08-22	590	card	1
P-00776	KR-00541	2026-09-17	1160	wallet	1
P-00777	KR-00542	2026-07-28	790	card	1
P-00778	KR-00542	2026-07-28	790	card	1
P-00779	KR-00543	2026-08-11	680	card	1
P-00780	KR-00543	2026-08-11	680	card	1
P-00781	KR-00544	2026-09-03	960	wallet	1
P-00782	KR-00545	2026-07-26	680	card	1
P-00783	KR-00545	2026-07-26	680	card	1
P-00784	KR-00546	2026-08-21	500	card	1
P-00785	KR-00546	2026-08-21	500	card	1
P-00786	KR-00547	2026-09-28	970	card	1
P-00787	KR-00548	2026-07-28	1200	netbanking	1
P-00788	KR-00549	2026-08-27	970	upi	1
P-00789	KR-00550	2026-09-18	1480	card	1
P-00790	KR-00551	2026-07-17	1500	wallet	1
P-00791	KR-00552	2026-08-14	880	card	1
P-00792	KR-00552	2026-08-14	880	card	1
P-00793	KR-00553	2026-09-28	1470	wallet	1
P-00794	KR-00554	2026-07-03	810	card	1
P-00795	KR-00554	2026-07-03	810	card	1
P-00796	KR-00555	2026-08-17	770	card	1
P-00797	KR-00555	2026-08-17	770	card	1
P-00798	KR-00556	2026-09-10	530	card	1
P-00799	KR-00556	2026-09-10	530	card	1
P-00800	KR-00557	2026-07-24	930	card	1
P-00801	KR-00558	2026-08-10	1180	card	1
P-00802	KR-00559	2026-09-04	1030	wallet	1
P-00803	KR-00560	2026-07-28	1240	wallet	1
P-00804	KR-00561	2026-08-26	900	card	1
P-00805	KR-00561	2026-08-26	900	card	1
P-00806	KR-00562	2026-09-23	750	card	1
P-00807	KR-00562	2026-09-23	750	card	1
P-00808	KR-00563	2026-07-22	940	netbanking	1
P-00809	KR-00564	2026-08-20	410	card	1
P-00810	KR-00564	2026-08-20	410	card	1
P-00811	KR-00565	2026-09-07	830	card	1
P-00812	KR-00565	2026-09-07	830	card	1
P-00813	KR-00566	2026-07-28	490	card	1
P-00814	KR-00566	2026-07-28	490	card	1
P-00815	KR-00567	2026-08-24	960	wallet	1
P-00816	KR-00568	2026-09-19	960	card	1
P-00817	KR-00569	2026-07-14	650	card	1
P-00818	KR-00569	2026-07-14	650	card	1
P-00819	KR-00570	2026-08-09	1410	card	1
P-00820	KR-00571	2026-09-27	1320	card	1
P-00821	KR-00572	2026-07-13	550	card	1
P-00822	KR-00572	2026-07-13	550	card	1
P-00823	KR-00573	2026-08-13	1300	card	1
P-00824	KR-00574	2026-09-07	640	card	1
P-00825	KR-00574	2026-09-07	640	card	1
P-00826	KR-00575	2026-07-07	1100	netbanking	1
P-00827	KR-00576	2026-08-06	1390	card	1
P-00828	KR-00577	2026-07-23	556200	upi	1
P-00829	KR-00577	2026-07-23	370800	upi	2
P-00830	KR-00578	2026-08-22	570000	wallet	1
P-00831	KR-00578	2026-08-22	380000	netbanking	2
P-00832	KR-00579	2026-09-15	450000	wallet	1
P-00833	KR-00579	2026-09-15	300000	card	2
P-00834	KR-00580	2026-07-24	513000	card	1
P-00835	KR-00580	2026-07-24	342000	netbanking	2
P-00836	KR-00581	2026-08-22	702000	card	1
P-00837	KR-00581	2026-08-22	468000	card	2
P-00838	KR-00582	2026-09-23	462000	netbanking	1
P-00839	KR-00582	2026-09-23	308000	netbanking	2
P-00840	KR-00583	2026-07-18	225600	wallet	1
P-00841	KR-00583	2026-07-18	150400	upi	2
P-00842	KR-00584	2026-08-28	475200	netbanking	1
P-00843	KR-00584	2026-08-28	316800	upi	2
P-00844	KR-00585	2026-09-17	736800	card	1
P-00845	KR-00585	2026-09-17	491200	netbanking	2
P-00846	KR-00586	2026-07-27	362400	card	1
P-00847	KR-00586	2026-07-27	241600	upi	2
P-00848	KR-00587	2026-08-27	786000	card	1
P-00849	KR-00587	2026-08-27	524000	card	2
P-00850	KR-00588	2026-09-13	498600	upi	1
P-00851	KR-00588	2026-09-13	332400	netbanking	2
P-00852	KR-00589	2026-07-04	892800	wallet	1
P-00853	KR-00589	2026-07-04	595200	wallet	2
P-00854	KR-00590	2026-08-05	1009800	upi	1
P-00855	KR-00590	2026-08-05	673200	upi	2
P-00856	KR-00591	2026-09-08	673800	card	1
P-00857	KR-00591	2026-09-08	449200	wallet	2
P-00858	KR-00592	2026-07-28	310200	upi	1
P-00859	KR-00592	2026-07-28	206800	card	2
P-00860	KR-00593	2026-08-17	676200	netbanking	1
P-00861	KR-00593	2026-08-17	450800	netbanking	2
P-00862	KR-00594	2026-09-12	496200	upi	1
P-00863	KR-00594	2026-09-12	330800	upi	2
P-00864	KR-00595	2026-07-25	240600	wallet	1
P-00865	KR-00595	2026-07-25	160400	upi	2
P-00866	KR-00596	2026-08-28	646800	card	1
P-00867	KR-00596	2026-08-28	431200	netbanking	2
P-00868	KR-00597	2026-09-13	700800	upi	1
P-00869	KR-00597	2026-09-13	467200	card	2
P-00870	KR-00598	2026-07-22	967800	netbanking	1
P-00871	KR-00598	2026-07-22	645200	upi	2
P-00872	KR-00599	2026-08-23	314400	wallet	1
P-00873	KR-00599	2026-08-23	209600	wallet	2
P-00874	KR-00600	2026-09-28	288600	upi	1
P-00875	KR-00600	2026-09-28	192400	wallet	2
P-00876	KR-00601	2026-07-24	624000	wallet	1
P-00877	KR-00601	2026-07-24	416000	netbanking	2
P-00878	KR-00602	2026-08-11	779400	upi	1
P-00879	KR-00602	2026-08-11	519600	card	2
P-00880	KR-00603	2026-09-12	220200	upi	1
P-00881	KR-00603	2026-09-12	146800	wallet	2
P-00882	KR-00604	2026-07-24	625200	upi	1
P-00883	KR-00604	2026-07-24	416800	card	2
P-00884	KR-00605	2026-08-10	167400	netbanking	1
P-00885	KR-00605	2026-08-10	111600	upi	2
P-00886	KR-00606	2026-09-18	320400	netbanking	1
P-00887	KR-00606	2026-09-18	213600	netbanking	2
P-00888	KR-00607	2026-07-24	132600	wallet	1
P-00889	KR-00607	2026-07-24	88400	wallet	2
P-00890	KR-00608	2026-08-05	550200	card	1
P-00891	KR-00608	2026-08-05	366800	upi	2
P-00892	KR-00609	2026-09-25	754800	netbanking	1
P-00893	KR-00609	2026-09-25	503200	upi	2
P-00894	KR-00610	2026-07-28	166800	netbanking	1
P-00895	KR-00610	2026-07-28	111200	netbanking	2
P-00896	KR-00611	2026-08-05	321600	card	1
P-00897	KR-00611	2026-08-05	214400	card	2
P-00898	KR-00612	2026-09-26	212400	netbanking	1
P-00899	KR-00612	2026-09-26	141600	upi	2
P-00900	KR-00613	2026-07-21	127200	upi	1
P-00901	KR-00613	2026-07-21	84800	netbanking	2
P-00902	KR-00614	2026-08-20	245400	netbanking	1
P-00903	KR-00614	2026-08-20	163600	wallet	2
P-00904	KR-00615	2026-09-19	381600	netbanking	1
P-00905	KR-00615	2026-09-19	254400	upi	2
P-00906	KR-00616	2026-07-23	138000	netbanking	1
P-00907	KR-00616	2026-07-23	92000	upi	2
P-00908	KR-00617	2026-08-03	811200	netbanking	1
P-00909	KR-00617	2026-08-03	540800	netbanking	2
P-00910	KR-00618	2026-09-20	700800	netbanking	1
P-00911	KR-00618	2026-09-20	467200	card	2
P-00912	KR-00619	2026-07-14	774000	netbanking	1
P-00913	KR-00619	2026-07-14	516000	upi	2
P-00914	KR-00620	2026-08-20	644400	wallet	1
P-00915	KR-00620	2026-08-20	429600	wallet	2
P-00916	KR-00621	2026-09-25	547800	card	1
P-00917	KR-00621	2026-09-25	365200	card	2
P-00918	KR-00622	2026-07-18	787200	card	1
P-00919	KR-00622	2026-07-18	524800	wallet	2
P-00920	KR-00623	2026-08-05	282600	card	1
P-00921	KR-00623	2026-08-05	188400	netbanking	2
P-00922	KR-00624	2026-09-19	653400	netbanking	1
P-00923	KR-00624	2026-09-19	435600	netbanking	2
P-00924	KR-00625	2026-07-16	1065600	netbanking	1
P-00925	KR-00625	2026-07-16	710400	netbanking	2
P-00926	KR-00626	2026-08-08	737400	netbanking	1
P-00927	KR-00626	2026-08-08	491600	wallet	2
P-00928	KR-00627	2026-09-12	180600	upi	1
P-00929	KR-00627	2026-09-12	120400	upi	2
P-00930	KR-00628	2026-07-28	333000	card	1
P-00931	KR-00628	2026-07-28	222000	upi	2
P-00932	KR-00629	2026-08-05	348000	wallet	1
P-00933	KR-00629	2026-08-05	232000	upi	2
P-00934	KR-00630	2026-09-09	211200	netbanking	1
P-00935	KR-00630	2026-09-09	140800	netbanking	2
P-00936	KR-00631	2026-07-15	258600	netbanking	1
P-00937	KR-00631	2026-07-15	172400	wallet	2
P-00938	KR-00632	2026-08-23	163800	netbanking	1
P-00939	KR-00632	2026-08-23	109200	card	2
P-00940	KR-00633	2026-09-14	583200	upi	1
P-00941	KR-00633	2026-09-14	388800	wallet	2
P-00942	KR-00634	2026-07-09	600600	netbanking	1
P-00943	KR-00634	2026-07-09	400400	upi	2
P-00944	KR-00635	2026-08-16	259800	wallet	1
P-00945	KR-00635	2026-08-16	173200	wallet	2
P-00946	KR-00636	2026-09-17	1066800	netbanking	1
P-00947	KR-00636	2026-09-17	711200	netbanking	2
P-00948	KR-00637	2026-07-28	856800	wallet	1
P-00949	KR-00637	2026-07-28	571200	card	2
P-00950	KR-00638	2026-08-15	343800	wallet	1
P-00951	KR-00638	2026-08-15	229200	card	2
P-00952	KR-00639	2026-09-26	890400	wallet	1
P-00953	KR-00639	2026-09-26	593600	card	2
P-00954	KR-00640	2026-07-18	615000	netbanking	1
P-00955	KR-00640	2026-07-18	410000	wallet	2
P-00956	KR-00641	2026-08-13	457800	wallet	1
P-00957	KR-00641	2026-08-13	305200	card	2
P-00958	KR-00642	2026-09-06	315000	upi	1
P-00959	KR-00642	2026-09-06	210000	card	2
P-00960	KR-00643	2026-07-25	499200	netbanking	1
P-00961	KR-00643	2026-07-25	332800	netbanking	2
P-00962	KR-00644	2026-08-07	135000	upi	1
P-00963	KR-00644	2026-08-07	90000	netbanking	2
P-00964	KR-00645	2026-09-21	481800	netbanking	1
P-00965	KR-00645	2026-09-21	321200	upi	2
P-00966	KR-00646	2026-07-13	319800	netbanking	1
P-00967	KR-00646	2026-07-13	213200	netbanking	2
P-00968	KR-00647	2026-08-03	343800	card	1
P-00969	KR-00647	2026-08-03	229200	upi	2
P-00970	KR-00648	2026-09-13	280800	netbanking	1
P-00971	KR-00648	2026-09-13	187200	wallet	2
P-00972	KR-00649	2026-07-17	936600	wallet	1
P-00973	KR-00649	2026-07-17	624400	wallet	2
P-00974	KR-00650	2026-08-03	1071000	card	1
P-00975	KR-00650	2026-08-03	714000	netbanking	2
P-00976	KR-00651	2026-09-28	712200	upi	1
P-00977	KR-00651	2026-09-28	474800	upi	2
P-00978	KR-00652	2026-07-25	750600	upi	1
P-00979	KR-00652	2026-07-25	500400	upi	2
P-00980	KR-00653	2026-08-18	482400	card	1
P-00981	KR-00653	2026-08-18	321600	netbanking	2
P-00982	KR-00654	2026-09-16	1074600	card	1
P-00983	KR-00654	2026-09-16	716400	upi	2
P-00984	KR-00655	2026-07-13	244800	card	1
P-00985	KR-00655	2026-07-13	163200	wallet	2
P-00986	KR-00656	2026-08-19	589800	netbanking	1
P-00987	KR-00656	2026-08-19	393200	card	2
P-00988	KR-00657	2026-09-07	1042200	card	1
P-00989	KR-00657	2026-09-07	694800	netbanking	2
P-00990	KR-00658	2026-07-10	153600	upi	1
P-00991	KR-00658	2026-07-10	102400	card	2
P-00992	KR-00659	2026-08-06	703800	wallet	1
P-00993	KR-00659	2026-08-06	469200	card	2
P-00994	KR-00660	2026-09-27	394200	netbanking	1
P-00995	KR-00660	2026-09-27	262800	netbanking	2
P-00996	KR-00661	2026-07-28	694800	upi	1
P-00997	KR-00661	2026-07-28	463200	netbanking	2
P-00998	KR-00662	2026-08-11	604200	upi	1
P-00999	KR-00662	2026-08-11	402800	card	2
P-01000	KR-00663	2026-09-13	255600	upi	1
P-01001	KR-00663	2026-09-13	170400	netbanking	2
P-01002	KR-00664	2026-07-28	172800	card	1
P-01003	KR-00664	2026-07-28	115200	upi	2
P-01004	KR-00665	2026-08-09	752400	netbanking	1
P-01005	KR-00665	2026-08-09	501600	netbanking	2
P-01006	KR-00666	2026-09-22	128400	upi	1
P-01007	KR-00666	2026-09-22	85600	card	2
P-01008	KR-00667	2026-07-15	11914560	netbanking	1
P-01009	KR-00667	2026-07-15	7943040	netbanking	2
P-01010	KR-00668	2026-07-14	2520	card	1
P-01011	KR-00668	2026-07-14	1680	netbanking	2
P-01012	KR-00669	2026-08-15	1860	card	1
P-01013	KR-00669	2026-08-15	1240	card	2
P-01014	KR-00670	2026-09-16	1900	upi	1
P-01015	KR-00671	2026-07-14	2280	netbanking	1
P-01016	KR-00671	2026-07-14	1520	upi	2
P-01017	KR-00672	2026-08-15	2600	upi	1
P-01018	KR-00673	2026-09-16	1400	wallet	1
P-01019	KR-00674	2026-07-14	2640	card	1
P-01020	KR-00674	2026-07-14	1760	upi	2
P-01021	KR-00675	2026-08-15	1740	card	1
P-01022	KR-00675	2026-08-15	1160	netbanking	2
P-01023	KR-00676	2026-09-16	1600	card	1
P-01024	KR-00677	2026-07-18	2290	upi	1
P-01025	KR-00678	2026-08-07	1230	card	1
P-01026	KR-00679	2026-09-22	2670	wallet	1
P-01027	KR-00680	2026-07-28	2502	wallet	1
P-01028	KR-00680	2026-07-28	1668	wallet	2
P-01029	KR-00681	2026-08-23	2214	netbanking	1
P-01030	KR-00681	2026-08-23	1476	card	2
P-01031	KR-00682	2026-09-21	2520	wallet	1
P-01032	KR-00683	2026-07-18	2616	wallet	1
P-01033	KR-00683	2026-07-18	1744	upi	2
P-01034	KR-00684	2026-08-13	2430	wallet	1
P-01035	KR-00685	2026-09-25	2160	wallet	1
P-01036	KR-00685	2026-09-25	1440	card	2
P-01037	KR-00686	2026-07-21	2400	netbanking	1
P-01038	KR-00687	2026-08-21	1758	card	1
P-01039	KR-00687	2026-08-21	1172	netbanking	2
P-01040	KR-00688	2026-09-07	1920	upi	1
P-01041	KR-00689	2026-07-25	2580	card	1
P-01042	KR-00689	2026-07-25	1720	netbanking	2
P-01043	KR-00690	2026-08-28	2094	wallet	1
P-01044	KR-00690	2026-08-28	1396	upi	2
P-01045	KR-00691	2026-09-13	1700	card	1
P-01046	KR-00692	2026-07-07	2004	netbanking	1
P-01047	KR-00692	2026-07-07	1336	netbanking	2
P-01048	KR-00693	2026-08-14	1692	wallet	1
P-01049	KR-00693	2026-08-14	1128	card	2
P-01050	KR-00694	2026-09-23	1660	upi	1
P-01051	KR-00695	2026-07-19	1932	upi	1
P-01052	KR-00695	2026-07-19	1288	upi	2
P-01053	KR-00696	2026-08-16	2200	wallet	1
P-01054	KR-00697	2026-09-09	1570	upi	1
P-01055	KR-00698	2026-07-21	2646	upi	1
P-01056	KR-00698	2026-07-21	1764	wallet	2
P-01057	KR-00699	2026-08-15	2088	upi	1
P-01058	KR-00699	2026-08-15	1392	upi	2
P-01059	KR-00700	2026-09-23	2142	upi	1
P-01060	KR-00700	2026-09-23	1428	upi	2
P-01061	KR-00701	2026-07-05	1850	netbanking	1
P-01062	KR-00702	2026-08-07	1280	card	1
P-01063	KR-00703	2026-09-03	2352	upi	1
P-01064	KR-00703	2026-09-03	1568	wallet	2
P-01065	KR-00704	2026-07-09	2530	card	1
P-01066	KR-00705	2026-08-06	2088	card	1
P-01067	KR-00705	2026-08-06	1392	wallet	2
P-01068	KR-00706	2026-09-11	1914	netbanking	1
P-01069	KR-00706	2026-09-11	1276	upi	2
P-01070	KR-00707	2026-07-26	2610	netbanking	1
P-01071	KR-00707	2026-07-26	1740	card	2
P-01072	KR-00708	2026-08-04	1730	card	1
P-01073	KR-00709	2026-09-14	2490	wallet	1
P-01074	KR-00709	2026-09-14	1660	upi	2
P-01075	KR-00710	2026-07-19	2700	upi	1
P-01076	KR-00710	2026-07-19	1800	upi	2
P-01077	KR-00711	2026-08-15	2592	wallet	1
P-01078	KR-00711	2026-08-15	1728	wallet	2
P-01079	KR-00712	2026-09-16	2088	upi	1
P-01080	KR-00712	2026-09-16	1392	card	2
P-01081	KR-00713	2026-07-24	1944	netbanking	1
P-01082	KR-00713	2026-07-24	1296	card	2
P-01083	KR-00714	2026-08-23	1410	upi	1
P-01084	KR-00715	2026-09-13	2472	wallet	1
P-01085	KR-00715	2026-09-13	1648	netbanking	2
P-01086	KR-00716	2026-07-04	2660	card	1
P-01087	KR-00717	2026-08-28	2540	netbanking	1
P-01088	KR-00718	2026-09-10	2394	netbanking	1
P-01089	KR-00718	2026-09-10	1596	wallet	2
P-01090	KR-00719	2026-07-12	2382	upi	1
P-01091	KR-00719	2026-07-12	1588	upi	2
P-01092	KR-00720	2026-08-08	1820	card	1
P-01093	KR-00721	2026-09-06	2424	netbanking	1
P-01094	KR-00721	2026-09-06	1616	upi	2
P-01095	KR-00722	2026-07-14	2010	wallet	1
P-01096	KR-00722	2026-07-14	1340	wallet	2
P-01097	KR-00723	2026-08-25	2628	upi	1
P-01098	KR-00723	2026-08-25	1752	wallet	2
P-01099	KR-00724	2026-09-17	2400	wallet	1
P-01100	KR-00724	2026-09-17	1600	netbanking	2
P-01101	KR-00725	2026-07-15	2490	netbanking	1
P-01102	KR-00725	2026-07-15	1660	upi	2
P-01103	KR-00726	2026-08-19	1932	wallet	1
P-01104	KR-00726	2026-08-19	1288	card	2
P-01105	KR-00727	2026-09-07	2010	wallet	1
P-01106	KR-00727	2026-09-07	1340	netbanking	2
P-01107	KR-00728	2026-07-23	1710	card	1
P-01108	KR-00729	2026-08-06	2610	wallet	1
P-01109	KR-00729	2026-08-06	1740	upi	2
P-01110	KR-00730	2026-09-06	2230	wallet	1
P-01111	KR-00731	2026-07-07	2058	card	1
P-01112	KR-00731	2026-07-07	1372	upi	2
P-01113	KR-00732	2026-08-19	2140	card	1
P-01114	KR-00733	2026-09-22	2200	netbanking	1
P-01115	KR-00734	2026-07-20	1900	wallet	1
P-01116	KR-00735	2026-08-18	2740	card	1
P-01117	KR-00736	2026-09-23	1990	netbanking	1
P-01118	KR-00737	2026-07-28	2210	netbanking	1
P-01119	KR-00738	2026-08-27	2274	card	1
P-01120	KR-00738	2026-08-27	1516	wallet	2
P-01121	KR-00739	2026-09-04	1450	upi	1
P-01122	KR-00740	2026-07-13	1350	card	1
P-01123	KR-00741	2026-08-25	2022	card	1
P-01124	KR-00741	2026-08-25	1348	wallet	2
P-01125	KR-00742	2026-09-03	1340	netbanking	1
P-01126	KR-00743	2026-07-18	2478	upi	1
P-01127	KR-00743	2026-07-18	1652	wallet	2
P-01128	KR-00744	2026-08-16	2380	netbanking	1
P-01129	KR-00745	2026-09-18	1920	upi	1
P-01130	KR-00746	2026-07-05	1866	netbanking	1
P-01131	KR-00746	2026-07-05	1244	netbanking	2
P-01132	KR-00747	2026-08-05	2094	netbanking	1
P-01133	KR-00747	2026-08-05	1396	wallet	2
P-01134	KR-00748	2026-09-06	1590	card	1
P-01135	KR-00749	2026-07-19	2598	wallet	1
P-01136	KR-00749	2026-07-19	1732	netbanking	2
P-01137	KR-00750	2026-08-15	1580	upi	1
P-01138	KR-00751	2026-09-18	1890	wallet	1
P-01139	KR-00751	2026-09-18	1260	card	2
P-01140	KR-00752	2026-07-23	2232	card	1
P-01141	KR-00752	2026-07-23	1488	wallet	2
P-01142	KR-00753	2026-08-23	2490	upi	1
P-01143	KR-00753	2026-08-23	1660	card	2
P-01144	KR-00754	2026-09-14	2268	wallet	1
P-01145	KR-00754	2026-09-14	1512	netbanking	2
P-01146	KR-00755	2026-07-27	2454	wallet	1
P-01147	KR-00755	2026-07-27	1636	upi	2
P-01148	KR-00756	2026-08-28	2500	upi	1
P-01149	KR-00757	2026-09-28	1940	upi	1
P-01150	KR-00758	2026-07-14	1300	wallet	1
P-01151	KR-00759	2026-08-15	2046	wallet	1
P-01152	KR-00759	2026-08-15	1364	netbanking	2
P-01153	KR-00760	2026-09-17	2740	card	1
P-01154	KR-00761	2026-07-24	2520	upi	1
P-01155	KR-00762	2026-08-09	1520	netbanking	1
P-01156	KR-00763	2026-09-24	2110	netbanking	1
P-01157	KR-00764	2026-07-04	1818	upi	1
P-01158	KR-00764	2026-07-04	1212	netbanking	2
P-01159	KR-00765	2026-08-28	2496	netbanking	1
P-01160	KR-00765	2026-08-28	1664	netbanking	2
P-01161	KR-00766	2026-09-28	2682	card	1
P-01162	KR-00766	2026-09-28	1788	upi	2
P-01163	KR-00767	2026-07-27	2358	netbanking	1
P-01164	KR-00767	2026-07-27	1572	upi	2
P-01165	KR-00768	2026-08-08	2490	upi	1
P-01166	KR-00768	2026-08-08	1660	wallet	2
P-01167	KR-00769	2026-09-22	2124	netbanking	1
P-01168	KR-00769	2026-09-22	1416	upi	2
P-01169	KR-00770	2026-07-28	2670	upi	1
P-01170	KR-00771	2026-08-06	2160	wallet	1
P-01171	KR-00771	2026-08-06	1440	upi	2
P-01172	KR-00772	2026-09-22	2540	wallet	1
P-01173	KR-00773	2026-07-04	1854	wallet	1
P-01174	KR-00773	2026-07-04	1236	upi	2
P-01175	KR-00774	2026-08-06	1686	card	1
P-01176	KR-00774	2026-08-06	1124	wallet	2
P-01177	KR-00775	2026-09-07	2330	netbanking	1
P-01178	KR-00776	2026-07-13	2060	wallet	1
P-01179	KR-00777	2026-08-10	2560	netbanking	1
P-01180	KR-00778	2026-09-07	1920	card	1
P-01181	KR-00778	2026-09-07	1280	upi	2
P-01182	KR-00779	2026-07-04	2214	netbanking	1
P-01183	KR-00779	2026-07-04	1476	card	2
P-01184	KR-00780	2026-08-13	2190	wallet	1
P-01185	KR-00781	2026-09-14	2030	card	1
P-01186	KR-00782	2026-07-24	2250	upi	1
P-01187	KR-00783	2026-08-26	1944	card	1
P-01188	KR-00783	2026-08-26	1296	upi	2
P-01189	KR-00784	2026-09-17	2346	card	1
P-01190	KR-00784	2026-09-17	1564	card	2
P-01191	KR-00785	2026-07-25	1610	wallet	1
P-01192	KR-00786	2026-08-09	2628	card	1
P-01193	KR-00786	2026-08-09	1752	card	2
P-01194	KR-00787	2026-09-08	1710	card	1
P-01195	KR-00788	2026-07-09	2370	wallet	1
P-01196	KR-00788	2026-07-09	1580	netbanking	2
P-01197	KR-00789	2026-08-22	2360	card	1
P-01198	KR-00790	2026-09-07	1220	upi	1
P-01199	KR-00791	2026-07-17	1908	upi	1
P-01200	KR-00791	2026-07-17	1272	netbanking	2
P-01201	KR-00792	2026-08-06	1770	card	1
P-01202	KR-00793	2026-09-23	2118	netbanking	1
P-01203	KR-00793	2026-09-23	1412	upi	2
P-01204	KR-00794	2026-07-26	2286	netbanking	1
P-01205	KR-00794	2026-07-26	1524	upi	2
P-01206	KR-00795	2026-08-04	2470	card	1
P-01207	KR-00796	2026-09-28	1920	netbanking	1
P-01208	KR-00797	2026-07-22	1920	card	1
P-01209	KR-00797	2026-07-22	1280	upi	2
P-01210	KR-00798	2026-08-21	2526	card	1
P-01211	KR-00798	2026-08-21	1684	wallet	2
P-01212	KR-00799	2026-09-08	1970	card	1
P-01213	KR-00800	2026-07-21	1570	upi	1
P-01214	KR-00801	2026-08-28	2568	netbanking	1
P-01215	KR-00801	2026-08-28	1712	wallet	2
P-01216	KR-00802	2026-09-13	2142	netbanking	1
P-01217	KR-00802	2026-09-13	1428	upi	2
P-01218	KR-00803	2026-07-05	1350	wallet	1
P-01219	KR-00804	2026-08-28	1788	wallet	1
P-01220	KR-00804	2026-08-28	1192	netbanking	2
P-01221	KR-00805	2026-09-10	2304	netbanking	1
P-01222	KR-00805	2026-09-10	1536	netbanking	2
P-01223	KR-00806	2026-07-16	2694	netbanking	1
P-01224	KR-00806	2026-07-16	1796	netbanking	2
P-01225	KR-00807	2026-08-07	2406	card	1
P-01226	KR-00807	2026-08-07	1604	wallet	2
P-01227	KR-00808	2026-07-18	2630	wallet	1
P-01228	KR-00809	2026-08-16	1370	wallet	1
P-01229	KR-00810	2026-09-28	2770	wallet	1
P-01230	KR-00811	2026-07-16	1900	upi	1
P-01231	KR-00812	2026-08-24	1340	upi	1
P-01232	KR-00813	2026-09-20	1110	card	1
P-01233	KR-00814	2026-07-28	1610	netbanking	1
P-01234	KR-00815	2026-08-28	1770	card	1
P-01235	KR-00816	2026-09-18	1960	wallet	1
P-01236	KR-00817	2026-07-21	1674	wallet	1
P-01237	KR-00817	2026-07-21	1116	wallet	2
P-01238	KR-00818	2026-08-11	830	card	1
P-01239	KR-00818	2026-08-11	830	card	1
P-01240	KR-00819	2026-09-14	2590	netbanking	1
P-01241	KR-00820	2026-07-12	1000	upi	1
P-01242	KR-00821	2026-08-28	1020	card	1
P-01243	KR-00822	2026-09-28	1390	card	1
P-01244	KR-00823	2026-07-14	950	netbanking	1
P-01245	KR-00824	2026-08-28	2080	card	1
P-01246	KR-00825	2026-09-11	1610	upi	1
P-01247	KR-00826	2026-07-09	830	card	1
P-01248	KR-00826	2026-07-09	830	card	1
P-01249	KR-00827	2026-08-28	950	upi	1
P-01250	KR-00828	2026-09-11	1730	card	1
P-01251	KR-00829	2026-07-21	930	netbanking	1
P-01252	KR-00830	2026-08-07	1752	upi	1
P-01253	KR-00830	2026-08-07	1168	upi	2
P-01254	KR-00831	2026-09-26	1450	upi	1
P-01255	KR-00832	2026-07-24	1752	wallet	1
P-01256	KR-00832	2026-07-24	1168	wallet	2
P-01257	KR-00833	2026-08-05	2750	card	1
P-01258	KR-00834	2026-09-10	840	card	1
P-01259	KR-00834	2026-09-10	840	card	1
P-01260	KR-00835	2026-07-10	1910	card	1
P-01261	KR-00836	2026-08-24	1960	upi	1
P-01262	KR-00837	2026-09-07	1200	card	1
P-01263	KR-00838	2026-07-22	1270	netbanking	1
P-01264	KR-00839	2026-08-05	1140	wallet	1
P-01265	KR-00840	2026-09-10	2250	card	1
P-01266	KR-00841	2026-07-19	1686	upi	1
P-01267	KR-00841	2026-07-19	1124	netbanking	2
P-01268	KR-00842	2026-08-11	2720	netbanking	1
P-01269	KR-00843	2026-09-14	1300	card	1
P-01270	KR-00844	2026-07-20	2730	upi	1
P-01271	KR-00845	2026-08-14	1370	card	1
P-01272	KR-00846	2026-09-06	1870	wallet	1
P-01273	KR-00847	2026-07-04	2150	netbanking	1
P-01274	KR-00848	2026-08-24	1686	wallet	1
P-01275	KR-00848	2026-08-24	1124	card	2
P-01276	KR-00849	2026-09-12	2010	card	1
P-01277	KR-00850	2026-07-23	2510	upi	1
P-01278	KR-00851	2026-08-20	1880	wallet	1
P-01279	KR-00852	2026-09-21	1210	netbanking	1
P-01280	KR-00853	2026-07-24	2150	wallet	1
P-01281	KR-00854	2026-08-13	980	wallet	1
P-01282	KR-00855	2026-09-08	820	card	1
P-01283	KR-00855	2026-09-08	820	card	1
P-01284	KR-00856	2026-07-10	2690	wallet	1
P-01285	KR-00857	2026-08-17	810	card	1
P-01286	KR-00857	2026-08-17	810	card	1
P-01287	KR-00858	2026-09-17	1290	netbanking	1
P-01288	KR-00859	2026-07-07	2670	upi	1
P-01289	KR-00860	2026-08-19	1910	card	1
P-01290	KR-00861	2026-09-24	1760	card	1
P-01291	KR-00862	2026-07-18	1830	upi	1
P-01292	KR-00863	2026-08-09	2030	upi	1
P-01293	KR-00864	2026-09-17	2430	wallet	1
P-01294	KR-00865	2026-07-12	1410	upi	1
P-01295	KR-00866	2026-08-06	1788	wallet	1
P-01296	KR-00866	2026-08-06	1192	upi	2
P-01297	KR-00867	2026-09-04	2120	wallet	1
P-01298	KR-00868	2026-07-19	1470	upi	1
P-01299	KR-00869	2026-08-16	1340	upi	1
P-01300	KR-00870	2026-09-12	1270	card	1
P-01301	KR-00871	2026-07-28	1130	upi	1
P-01302	KR-00872	2026-08-12	2130	wallet	1
P-01303	KR-00873	2026-09-09	840	card	1
P-01304	KR-00873	2026-09-09	840	card	1
P-01305	KR-00874	2026-07-08	2520	netbanking	1
P-01306	KR-00875	2026-08-27	1540	wallet	1
P-01307	KR-00876	2026-09-26	1400	wallet	1
P-01308	KR-00877	2026-07-10	1850	card	1
P-01309	KR-00878	2026-08-15	1120	card	1
P-01310	KR-00879	2026-09-28	1740	card	1
P-01311	KR-00880	2026-07-10	1910	netbanking	1
P-01312	KR-00881	2026-08-14	2550	upi	1
P-01313	KR-00882	2026-09-06	1140	card	1
P-01314	KR-00883	2026-07-05	2650	wallet	1
P-01315	KR-00884	2026-08-15	2610	wallet	1
P-01316	KR-00885	2026-09-12	2550	netbanking	1
P-01317	KR-00886	2026-07-09	1970	wallet	1
P-01318	KR-00887	2026-08-03	950	wallet	1
P-01319	KR-00888	2026-09-05	1794	netbanking	1
P-01320	KR-00888	2026-09-05	1196	netbanking	2
P-01321	KR-00889	2026-07-03	1850	upi	1
P-01322	KR-00890	2026-08-22	1710	upi	1
P-01323	KR-00890	2026-08-22	1140	card	2
P-01324	KR-00891	2026-09-24	2650	card	1
P-01325	KR-00892	2026-07-06	920	card	1
P-01326	KR-00892	2026-07-06	920	card	1
P-01327	KR-00893	2026-08-04	860	card	1
P-01328	KR-00893	2026-08-04	860	card	1
P-01329	KR-00894	2026-09-17	1260	card	1
P-01330	KR-00895	2026-07-14	1752	netbanking	1
P-01331	KR-00895	2026-07-14	1168	card	2
P-01332	KR-00896	2026-08-07	2690	netbanking	1
P-01333	KR-00897	2026-09-24	1728	netbanking	1
P-01334	KR-00897	2026-09-24	1152	wallet	2
P-01335	KR-00898	2026-07-25	1670	upi	1
P-01336	KR-00899	2026-08-25	1470	card	1
P-01337	KR-00900	2026-09-21	1140	card	1
P-01338	KR-00901	2026-07-26	830	card	1
P-01339	KR-00901	2026-07-26	830	card	1
P-01340	KR-00902	2026-08-16	1680	wallet	1
P-01341	KR-00903	2026-09-07	1230	netbanking	1
P-01342	KR-00904	2026-07-12	2030	netbanking	1
P-01343	KR-00905	2026-08-13	1698	card	1
P-01344	KR-00905	2026-08-13	1132	upi	2
P-01345	KR-00906	2026-09-10	2060	netbanking	1
P-01346	KR-00907	2026-07-28	1686	card	1
P-01347	KR-00907	2026-07-28	1124	netbanking	2
P-01348	KR-00908	2026-08-24	1800	wallet	1
P-01349	KR-00908	2026-08-24	1200	upi	2
P-01350	KR-00909	2026-09-17	1270	wallet	1
P-01351	KR-00910	2026-07-20	2280	netbanking	1
P-01352	KR-00911	2026-08-08	1200	netbanking	1
P-01353	KR-00912	2026-09-10	870	card	1
P-01354	KR-00912	2026-09-10	870	card	1
P-01355	KR-00913	2026-07-18	1950	netbanking	1
P-01356	KR-00914	2026-08-16	1980	wallet	1
P-01357	KR-00915	2026-09-10	1722	card	1
P-01358	KR-00915	2026-09-10	1148	upi	2
P-01359	KR-00916	2026-07-09	1010	netbanking	1
P-01360	KR-00917	2026-08-12	2510	netbanking	1
P-01361	KR-00918	2026-09-13	2230	card	1
P-01362	KR-00919	2026-07-24	2240	netbanking	1
P-01363	KR-00920	2026-08-16	2630	wallet	1
P-01364	KR-00921	2026-09-09	960	card	1
P-01365	KR-00922	2026-07-04	2050	upi	1
P-01366	KR-00923	2026-08-13	1410	netbanking	1
P-01367	KR-00924	2026-09-28	1686	netbanking	1
P-01368	KR-00924	2026-09-28	1124	netbanking	2
P-01369	KR-00925	2026-07-08	2220	upi	1
P-01370	KR-00926	2026-08-25	2790	upi	1
P-01371	KR-00927	2026-09-28	1920	upi	1
P-01372	KR-00928	2026-07-16	1794	card	1
P-01373	KR-00928	2026-07-16	1196	card	2
P-01374	KR-00929	2026-08-28	1840	netbanking	1
P-01375	KR-00930	2026-09-04	2050	wallet	1
P-01376	KR-00931	2026-07-10	2090	wallet	1
P-01377	KR-00932	2026-08-03	2600	netbanking	1
P-01378	KR-00933	2026-09-11	1910	wallet	1
P-01379	KR-00934	2026-07-09	1700	card	1
P-01380	KR-00935	2026-08-08	1620	netbanking	1
P-01381	KR-00936	2026-09-26	1300	upi	1
P-01382	KR-00937	2026-07-25	1820	wallet	1
P-01383	KR-00938	2026-08-21	2340	wallet	1
P-01384	KR-00939	2026-09-23	1110	upi	1
P-01385	KR-00940	2026-07-25	1620	wallet	1
P-01386	KR-00941	2026-08-05	1686	netbanking	1
P-01387	KR-00941	2026-08-05	1124	upi	2
P-01388	KR-00942	2026-09-18	1320	card	1
P-01389	KR-00943	2026-07-07	1320	card	1
P-01390	KR-00944	2026-08-11	1770	card	1
P-01391	KR-00945	2026-09-22	1900	card	1
P-01392	KR-00946	2026-07-28	1758	upi	1
P-01393	KR-00946	2026-07-28	1172	upi	2
P-01394	KR-00947	2026-08-17	1270	wallet	1
P-01395	KR-00948	2026-09-09	2760	wallet	1
P-01396	KR-00949	2026-07-05	2530	netbanking	1
P-01397	KR-00950	2026-08-21	1000	netbanking	1
P-01398	KR-00951	2026-09-13	1090	wallet	1
P-01399	KR-00952	2026-07-04	1050	netbanking	1
P-01400	KR-00953	2026-08-09	1734	upi	1
P-01401	KR-00953	2026-08-09	1156	netbanking	2
P-01402	KR-00954	2026-09-06	2120	card	1
P-01403	KR-00955	2026-07-11	1746	card	1
P-01404	KR-00955	2026-07-11	1164	card	2
P-01405	KR-00956	2026-08-07	2380	upi	1
P-01406	KR-00957	2026-09-26	1990	wallet	1
P-01407	KR-00958	2026-07-07	2050	wallet	1
P-01408	KR-00959	2026-08-06	2140	card	1
P-01409	KR-00960	2026-09-18	1240	upi	1
P-01410	KR-00961	2026-07-03	1730	wallet	1
P-01411	KR-00965	2026-08-12	1280	wallet	1
P-01412	KR-00966	2026-09-25	2250	card	1
P-01413	KR-00969	2026-09-21	1070	wallet	1
P-01414	KR-00974	2026-08-04	2180	card	1
P-01415	KR-00975	2026-09-14	1770	card	1
P-01416	KR-00975	2026-09-14	1180	netbanking	2
P-01417	KR-00980	2026-08-24	1160	upi	1
P-01418	KR-00984	2026-09-27	1650	wallet	1
P-01419	KR-00986	2026-08-19	1530	wallet	1
P-01420	KR-00987	2026-09-19	1400	upi	1
P-01421	KR-90000	2026-08-14	2000	wallet	1
P-01422	KR-90001	2026-08-14	2310	wallet	1
P-01423	KR-90002	2026-08-14	2620	wallet	1
P-01424	KR-90003	2026-08-14	2930	wallet	1
P-01425	KR-90004	2026-08-14	3240	wallet	1
P-01426	KR-90005	2026-08-14	3550	wallet	1
P-01427	KR-90006	2026-08-14	3860	wallet	1
P-01428	KR-90007	2026-08-14	4170	wallet	1
\.

COPY refunds (refund_id, order_id, refund_date, amount, reason) FROM stdin;
R-0001	KR-00001	2026-04-20	-520	wrong item
R-0002	KR-00011	2026-05-20	-1050	damaged
R-0003	KR-00013	2026-04-09	-710	wrong item
R-0004	KR-00031	2026-04-13	-1647000	damaged
R-0005	KR-00033	2026-06-08	-866000	late delivery
R-0006	KR-00034	2026-04-22	-869000	damaged
R-0007	KR-00042	2026-06-04	-1566000	wrong item
R-0008	KR-00045	2026-06-07	-1645000	wrong item
R-0009	KR-00047	2026-05-07	-363000	wrong item
R-0010	KR-00048	2026-06-28	-214000	late delivery
R-0011	KR-00051	2026-06-21	-1648000	damaged
R-0012	KR-00057	2026-06-18	-247000	late delivery
\.

COPY campaign_exposure (customer_id, campaign_id, exposed_date) FROM stdin;
C-0001	CMP-MONSOON-26	2026-08-03
C-0002	CMP-MONSOON-26	2026-08-03
C-0003	CMP-MONSOON-26	2026-08-03
C-0006	CMP-MONSOON-26	2026-08-03
C-0007	CMP-MONSOON-26	2026-08-03
C-0009	CMP-MONSOON-26	2026-08-03
C-0012	CMP-MONSOON-26	2026-08-03
C-0017	CMP-MONSOON-26	2026-08-03
C-0019	CMP-MONSOON-26	2026-08-03
C-0021	CMP-MONSOON-26	2026-08-03
C-0023	CMP-MONSOON-26	2026-08-03
C-0025	CMP-MONSOON-26	2026-08-03
C-0028	CMP-MONSOON-26	2026-08-03
C-0030	CMP-MONSOON-26	2026-08-03
C-0031	CMP-MONSOON-26	2026-08-03
C-0033	CMP-MONSOON-26	2026-08-03
C-0036	CMP-MONSOON-26	2026-08-03
C-0037	CMP-MONSOON-26	2026-08-03
C-0040	CMP-MONSOON-26	2026-08-03
C-0041	CMP-MONSOON-26	2026-08-03
C-0044	CMP-MONSOON-26	2026-08-03
C-0047	CMP-MONSOON-26	2026-08-03
C-0048	CMP-MONSOON-26	2026-08-03
C-0049	CMP-MONSOON-26	2026-08-03
C-0052	CMP-MONSOON-26	2026-08-03
C-0054	CMP-MONSOON-26	2026-08-03
C-0055	CMP-MONSOON-26	2026-08-03
C-0057	CMP-MONSOON-26	2026-08-03
C-0058	CMP-MONSOON-26	2026-08-03
C-0059	CMP-MONSOON-26	2026-08-03
C-0061	CMP-MONSOON-26	2026-08-03
C-0062	CMP-MONSOON-26	2026-08-03
C-0064	CMP-MONSOON-26	2026-08-03
C-0066	CMP-MONSOON-26	2026-08-03
C-0068	CMP-MONSOON-26	2026-08-03
C-0069	CMP-MONSOON-26	2026-08-03
C-0070	CMP-MONSOON-26	2026-08-03
C-0076	CMP-MONSOON-26	2026-08-03
C-0078	CMP-MONSOON-26	2026-08-03
C-0079	CMP-MONSOON-26	2026-08-03
C-0080	CMP-MONSOON-26	2026-08-03
C-0082	CMP-MONSOON-26	2026-08-03
C-0083	CMP-MONSOON-26	2026-08-03
C-0084	CMP-MONSOON-26	2026-08-03
C-0092	CMP-MONSOON-26	2026-08-03
C-0095	CMP-MONSOON-26	2026-08-03
C-0098	CMP-MONSOON-26	2026-08-03
C-0101	CMP-MONSOON-26	2026-08-03
C-0105	CMP-MONSOON-26	2026-08-03
C-0106	CMP-MONSOON-26	2026-08-03
C-0107	CMP-MONSOON-26	2026-08-03
C-0110	CMP-MONSOON-26	2026-08-03
C-0114	CMP-MONSOON-26	2026-08-03
C-0115	CMP-MONSOON-26	2026-08-03
C-0116	CMP-MONSOON-26	2026-08-03
C-0117	CMP-MONSOON-26	2026-08-03
C-0120	CMP-MONSOON-26	2026-08-03
C-0121	CMP-MONSOON-26	2026-08-03
C-0122	CMP-MONSOON-26	2026-08-03
C-0123	CMP-MONSOON-26	2026-08-03
C-0125	CMP-MONSOON-26	2026-08-03
C-0127	CMP-MONSOON-26	2026-08-03
C-0128	CMP-MONSOON-26	2026-08-03
C-0130	CMP-MONSOON-26	2026-08-03
C-0132	CMP-MONSOON-26	2026-08-03
C-0140	CMP-MONSOON-26	2026-08-03
C-0141	CMP-MONSOON-26	2026-08-03
C-0142	CMP-MONSOON-26	2026-08-03
C-0145	CMP-MONSOON-26	2026-08-03
C-0148	CMP-MONSOON-26	2026-08-03
C-0152	CMP-MONSOON-26	2026-08-03
C-0156	CMP-MONSOON-26	2026-08-03
C-0157	CMP-MONSOON-26	2026-08-03
C-0158	CMP-MONSOON-26	2026-08-03
C-0160	CMP-MONSOON-26	2026-08-03
C-0161	CMP-MONSOON-26	2026-08-03
C-0162	CMP-MONSOON-26	2026-08-03
C-0166	CMP-MONSOON-26	2026-08-03
C-0167	CMP-MONSOON-26	2026-08-03
C-0169	CMP-MONSOON-26	2026-08-03
C-0171	CMP-MONSOON-26	2026-08-03
C-0172	CMP-MONSOON-26	2026-08-03
C-0174	CMP-MONSOON-26	2026-08-03
C-0177	CMP-MONSOON-26	2026-08-03
C-0178	CMP-MONSOON-26	2026-08-03
C-0179	CMP-MONSOON-26	2026-08-03
C-0180	CMP-MONSOON-26	2026-08-03
C-0181	CMP-MONSOON-26	2026-08-03
C-0183	CMP-MONSOON-26	2026-08-03
C-0184	CMP-MONSOON-26	2026-08-03
C-0185	CMP-MONSOON-26	2026-08-03
C-0187	CMP-MONSOON-26	2026-08-03
C-0188	CMP-MONSOON-26	2026-08-03
C-0189	CMP-MONSOON-26	2026-08-03
C-0190	CMP-MONSOON-26	2026-08-03
C-0195	CMP-MONSOON-26	2026-08-03
C-0196	CMP-MONSOON-26	2026-08-03
C-0197	CMP-MONSOON-26	2026-08-03
C-0199	CMP-MONSOON-26	2026-08-03
C-0200	CMP-MONSOON-26	2026-08-03
C-0203	CMP-MONSOON-26	2026-08-03
C-0205	CMP-MONSOON-26	2026-08-03
C-0206	CMP-MONSOON-26	2026-08-03
C-0208	CMP-MONSOON-26	2026-08-03
C-0210	CMP-MONSOON-26	2026-08-03
C-0216	CMP-MONSOON-26	2026-08-03
C-0219	CMP-MONSOON-26	2026-08-03
C-0220	CMP-MONSOON-26	2026-08-03
C-0222	CMP-MONSOON-26	2026-08-03
C-0223	CMP-MONSOON-26	2026-08-03
C-0231	CMP-MONSOON-26	2026-08-03
C-0232	CMP-MONSOON-26	2026-08-03
C-0233	CMP-MONSOON-26	2026-08-03
C-0235	CMP-MONSOON-26	2026-08-03
C-0239	CMP-MONSOON-26	2026-08-03
C-0240	CMP-MONSOON-26	2026-08-03
C-0241	CMP-MONSOON-26	2026-08-03
C-0244	CMP-MONSOON-26	2026-08-03
C-0245	CMP-MONSOON-26	2026-08-03
C-0249	CMP-MONSOON-26	2026-08-03
C-0250	CMP-MONSOON-26	2026-08-03
C-0252	CMP-MONSOON-26	2026-08-03
C-0253	CMP-MONSOON-26	2026-08-03
C-0255	CMP-MONSOON-26	2026-08-03
C-0256	CMP-MONSOON-26	2026-08-03
C-0258	CMP-MONSOON-26	2026-08-03
C-0261	CMP-MONSOON-26	2026-08-03
C-0262	CMP-MONSOON-26	2026-08-03
C-0265	CMP-MONSOON-26	2026-08-03
C-0268	CMP-MONSOON-26	2026-08-03
C-0001	CMP-MONSOON-26	2026-08-11
C-0002	CMP-MONSOON-26	2026-08-11
C-0003	CMP-MONSOON-26	2026-08-11
C-0006	CMP-MONSOON-26	2026-08-11
C-0007	CMP-MONSOON-26	2026-08-11
C-0009	CMP-MONSOON-26	2026-08-11
\.

COPY plan_line (week_start, plan_revenue) FROM stdin;
2026-07-06	7569230
2026-07-13	7569230
2026-07-20	7569230
2026-07-27	7569230
2026-08-03	7569230
2026-08-10	7569230
2026-08-17	7569230
2026-08-24	7569230
2026-08-31	7569230
2026-09-07	7569230
2026-09-14	7569230
2026-09-21	7569230
2026-09-28	7569230
\.

-- Row counts this file must load, which Monday's first query checks.
--   customers: 340
--   orders: 1000
--   campaigns: 1
--   payments: 1428
--   refunds: 12
--   campaign_exposure: 136
--   plan_line: 13
