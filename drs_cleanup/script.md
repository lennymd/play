# Reformating DRS things

## What we have right now

Looking at the different files we have to match columns:

### Columns coming from DRS2024 conftool

"paperID","contribution_type","presentation_mode","authors","organisations","","title","","keywords","topics","","submitting_author","sa_organisation","sa_country","sa_region","","sa_email","sa_email2","all_emails","presenting_author","presenting_author_emails","presenting_author_cv","","studentpaper","extratext","extraoption","","","reviews_assigned","reviews_hidden_from_authors","reviews_received","","score_average","","acceptance_status","acceptance","","copyright_signature","copyright_signed_date","","external_resource","","paper_external_comment","paper_internal_comment","paper_comment_chair_to_author","","paper_submitted","paper_last_update","withdrawn"

### Columns in DRS2022

paperID,title,abstract,keywords,theme track,Mode,doi,doi link,,authors_formatted_1_name,Author 1_first name,Author 1_middle name,Author1_last name,authors_formatted_1_organisation,authors_formatted_1_email,authors_formatted_2_name,Author 2_first name,Author 2_middle name,Author2_last name,authors_formatted_2_organisation,authors_formatted_3_name,Author 3_first name,Author 3_middle name,Author3_last name,authors_formatted_3_organisation,authors_formatted_4_name,Author 4_first name,Author 4_middle name,Author4_last name,authors_formatted_4_organisation,authors_formatted_5_name,Author 5_first name,Author 5_middle name,Author5_last name,authors_formatted_5_organisation,authors_formatted_6_name,Author 6_first name,Author 6_middle name,Author6_last name,authors_formatted_6_organisation,authors_formatted_7_name,Author 7_first name,Author 7_middle name,Author7_last name,authors_formatted_7_organisation,authors_formatted_8_name,Author 8_first name,Author 8_middle name,Author8_last name,authors_formatted_8_organisation,authors_formatted_9_name,Author 9_first name,Author 9_middle name,Author9_last name,authors_formatted_9_organisation,authors_formatted_10_name,Author 10_first name,Author 10_middle name,Author10_last name,authors_formatted_10_organisation,authors_formatted_11_name,Author 11_first name,Author 11_middle name,Author11_last name,authors_formatted_11_organisation

## Columns in TI2023

title,fulltext_url,keywords,abstract,author1_fname,author1_mname,author1_lname,author1_suffix,author1_email,author1_institution,author1_is_corporate,author2_fname,author2_mname,author2_lname,author2_suffix,author2_email,author2_institution,author2_is_corporate,author3_fname,author3_mname,author3_lname,author3_suffix,author3_email,author3_institution,author3_is_corporate,author4_fname,author4_mname,author4_lname,author4_suffix,author4_email,author4_institution,author4_is_corporate,author5_fname,author5_mname,author5_lname,author5_suffix,author5_email,author5_institution,author5_is_corporate,author6_fname,author6_mname,author6_lname,author6_suffix,author6_email,author6_institution,author5_is_corporate,disciplines,city,comments,conference_dates,conference_title,conference_track,country,custom_citation,distribution_license,document_type,doi,doi_link,do_not_feature_this_article,editor_names,end_date,orcid,previous_versions,shortname,start_date,topics,update_reason

### The way columns have to map

- title: comes directly from form
- fulltext_url: comes from uploading the papers to the DL
- keywords: make them all lowercase and semicolon separated
- abstract: comes directly from form
- For each author in the paper we need: `author#_fname`,`author#_mname`,`author#_lname`,`author#_fnsuffixame`,`author#_email`,`author#_institution`,`author#_iscorporate`
- disciplines
- city
- comments
- conference_dates
- conference_title
- conference_track
- country
- custom_citation
- distribution_license
- document_type
- doi: comes from paperID
- doi_link: comes from DOI + paperID
- do_not_feature_this_article
- editor_names: Repeated
- orcid
- previous_versions
- shortname
- start_date
- end_date
- topics
- update_reason
