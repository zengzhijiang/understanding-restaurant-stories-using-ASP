# Understanding Restaurant Stories Using Answer Set Prolog (ASP) Theory of Intentions 
Enhanced an NLP application to provide a restaurant dining scenario with automatic actions using Logic AI. Coded and tested ASP rules in the Knowledge Base for action conditions and effects to manage various restaurant dining scenarios.

## Research Problem
Natural language understanding is a sub-field of AI that focuses on machine reading comprehension. In this work, we focus on the understanding of stories that narrate about the occurrence of a sequence of events. According to Schank and Abelson (1977), stories frequently narrate episodes related to stereotypical activities (i.e., sequences of actions normally performed in a certain order by one or more actors, according to cultural conventions). Some examples of stereotypical activities include dining in a restaurant, going to the doctor, going to the cinema, etc. A story mentioning a stereotypical activity is not required to state explicitly all of the actions that are part of it, as it is assumed that readers are capable of filling in the blanks with their own commonsense knowledge about the activity (Schank and Abelson 1977). This complicates the task of automating an understanding of such stories. It is even more difficult to understand stories that describe variations of the normal unfolding of stereotypical activities (e.g., a group of customers dining together, not just one customer alone; dining at a restaurant with a hostess and a waiter). Recent work by Inclezan et al. (2017) introduced a methodology for processing stories about stereotypical activities that can deal with normal and exceptional scenarios. Inclezan et al. illustrated and evaluated their methodology on stories about dining at a restaurant with table service. It remains to be investigated whether the methodology is easily applicable to restaurant stories with variations.

## Objectives
1. Determine whether the methodology developed by Inclezan et al. is easily applicable to restaurant scenarios including variations.
2. Adapt and extend the methodology by Inclezan et al. to process restaurant stories with variations, in addition to normal scenarios and scenarios with exceptions.

## Methods
1. Collect 20 stories involving dining at a restaurant with table service. These stories will be gathered (and possibly adapted) from the Internet or other written resources. Two thirds of the stories will be used for developing the methodology; the other third will be used for evaluating it.
2. Analyze the stories in the collection and categorize them as representing a normal scenario, an exception, or variation.
3. Write Answer Set Prolog rules to be added to the existing restaurant knowledge base to capture variations. As a minimum, the following variations should be captured: a group of customers dining together (instead of one customer only), dining at a restaurant where there is a host/hostess and a waiter.
4. Update the activities of each actor (with sub-activities and goals, as defined in the theory of intentions by Blount et al., 2015) in order to cover variations.
5. Apply the methodology in Inclezan et al. (2017) to demonstrate machine comprehension via question answering.
6. Evaluate the work on the collection of test stories.
7. Determine and document remaining challenges.
