ok, I've spent enough time looking at this to get very confused :)

Main reason being the bioportal meddra ontology has 75,000 classes but only 12 properties...

from ICH ICSR Specification:
"A new data element was added to allow for reporting of events/reactions as reported, and as MedDRA Lowest Level Terms (LLT) and Preferred Terms (PT).  The “as reported” and reaction term elements existed in the previous version.  A new element was added allowing inclusion of both LLT and PT in the ICSR...."
 "There are several data elements that are MedDRA controlled fields. MedDRA version should be included for each term used."
https://admin.ich.org/sites/default/files/inline-files/ICH_ICSR_Specification_version_2_3_0.doc

so (I could well be wrong) it looks like many (most?) of the *objects* of the statements can be mapped to the ontology, but the *properties* will still have to come from ICSR, some (most?) of the *subjects* may be classifiable as instances ontology terms

pulling a cheery term from the DTD:
<!ELEMENT patientdeathcause (patientdeathreportmeddraversion?, patientdeathreport?)>
<!ATTLIST patientdeathcause
	%lang.att;
>

seems a bit clunky for them to have included a *-meddraversion field, but it may well help pull out terms where a class mapping exists. 

The bioportal does have an API. I've not looked yet, but if they have consistent conventions for naming/numbering between ICSR and the ontology with a bit of string-tweaking it may be possible to pull out/potentially substitutes.




https://bioportal.bioontology.org/accounts/new





194794 1_ADR21Q2.nt
   268955 2__ADR21Q2.nt
   379193 3__ADR21Q2.nt
  1842942 total

https://bioportal.bioontology.org/ontologies/MEDDRA?p=classes&conceptid=http%3A%2F%2Fpurl.bioontology.org%2Fontology%2FMEDDRA%2F10016416#details

https://bioportal.bioontology.org/ontologies/MEDDRA?conceptid=http%3A%2F%2Fpurl.bioontology.org%2Fontology%2FMEDDRA%2F10059938&p=classes

how would you model those records





rapper -c -i ntriples 1_ADR21Q2.nt &> errs.txt


head -n 2000 1_ADR21Q2.nt > 2000.nt


tail -n +2095 1_ADR21Q2.nt | head -n 3 > err-lines.txt

8182

Notebook name
aws-neptune-timber

IAM role
AWSNeptuneNotebookRole-Lumberjack








i want to put my data in neptune but no time to learn the process, i can set it up and give you access on mine but need help figuring out the how to enter data/query etc
You sent
ok, I can have a go at that
Ronald
well i can create an instance of it, and give you a key?
Ronald
we need some rate first before you start spending time
Ronald
and some cap. alternatively we can publish a paper on it
Ronald
Ronald Reck
but im not sure you really care about papers
You sent
I'm not too bothered about papers - I did write one a few months ago, but doing it as a paper was really just to give myself an artificial deadline to get the material written up
You sent
rate - I really don't know. What's double minimum wage?
Ronald
let me look it up
Ronald
Ronald Reck
What is the minimum wage in Virginia in 2021?
$9.50 per hour. how about $25?
You sent
ok, sounds good
Ronald
i will make you a jira login before we start and make a cap of max money for now
Ronald
it easier to talk on the phone to give you a briefing since there is a bunch of background that is helpful but not essential
Ronald
its just data
Ronald
Ronald Reck
do you have some background with SKOS ?
You sent
some SKOS
Ronald
Ronald Reck
well the secondary task is helping me determine the structure to move Meddra to a SKOS structure
You sent
(heh, I think I got my name on a SKOS paper even though I didn't do any work towards it)
Ronald
if you can code great, otherwise we can do it with SPARQL update
Ronald
so Meddra exists, and has a hierarchy
Ronald
Ronald Reck
i wish it was in SKOS and think they are lame for not using it
You sent
right
Ronald
then the third task will be to move the Faers data i have RDFized to using Meddra markup but that is kinda down the road
Ronald
Ronald Reck
federal adverse reporting system
You sent
actually - before chatting phone (or vid if you prefer) - probably best if you give me a list of things like Meddra, Faers... that I can read about a bit
Ronald
Ronald Reck
this is when bad things happen in pharma they have to report it
You sent
and a hand-wavy idea of what you'd like me to do with them...
Ronald
Ronald Reck
the reports exist for public consumption
You sent
ok
Ronald
Ronald Reck
i made the XML into RDF and that is pretty much "done"
You sent
so explore Neptune; Meddra -> SKOS; Faers -> Meddra
Ronald
Ronald Reck
BINGO
You sent
You sent
brb, barky dog
Ronald
i will create a AWS neptune today and send you some credentials
Ronald
Ronald Reck
i sent the JIRA invite just now
You sent
hmm, sounded like a postie bark but can't see anyone - maybe just a cat and he's trying to fool me
Ronald
Ronald Reck
CLAUDIO!
You sent
lol
You sent
ok, I'm in https://rrecktek.atlassian.net/jira/software/projects/PHAR/boards/3
You sent
I'd better take him out for a bit - I've been at computer all morning, he's obviously bored
Ronald
Ronald Reck
yeah i dont have the tasks written yet
You sent
what time zone are you in?
Ronald
eastern
Ronald
its almost 9am
Ronald
what about you
Ronald
i work largely with Bosnia and Calcutta
Ronald
Ronald Reck
Jen's PHARMA4 is what i have been hot on if you see it
You sent
right-ho. Rome, Central European
Ronald
he has made a few versions and is a great coder
Ronald
i have know him about a decade and we worked same company (KODAK) for about 2 years
Ronald
so i download Faers and convert it, now i enter it in Virtusoso, my client uses Mark Logic which so far sucks
Ronald
my client creates their version of Faers internally but its easier to just use the public data
Ronald
Ronald Reck
the originate some Faers data, my client is Johnson and Johnson
You sent
ok
Ronald
its not huge, maybe 20 million records total
Ronald
Ronald Reck
like around 2 million a year
You sent
enough..!
Ronald
each record makes about 300 triples
Ronald
this is to show them a process, they dont want to process all that data
Ronald
Ronald Reck
i just do it so i am complete and to me its pretty managable
You sent
I've dipped into Virtuoso a good few times, MarkLogic rings a bell, maybe used it but would have been years ago

