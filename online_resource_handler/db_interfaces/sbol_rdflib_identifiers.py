import rdflib


class SBOLIdentifiers:
    def __init__(self):
        self.namespaces = Namespace()
        self.objects = Objects(self.namespaces)
        self.predicates = Predicates(self.namespaces)
        self.external = ExternalIdentifiers(self.namespaces)
    

class Namespace:
    def __init__(self):
        self.sbol = rdflib.URIRef('http://sbols.org/v2#')
        identifiers = rdflib.URIRef('http://identifiers.org/')
        self.sequence_ontology = rdflib.URIRef(identifiers + 'so/SO:')
        self.sbo_biomodels = rdflib.URIRef(identifiers + 'biomodels.sbo/SBO:') 
        self.identifier_edam = rdflib.URIRef(identifiers + 'edam/')

        self.biopax = rdflib.URIRef('http://www.biopax.org/release/biopax-level3.owl#')
        self.dc = rdflib.URIRef('http://purl.org/dc/terms/')
        self.edam = rdflib.URIRef('http://edamontology.org/format')
        self.owl = rdflib.URIRef('http://www.w3.org/2002/07/owl#')
        self.prov = rdflib.URIRef('https://www.w3.org/ns/prov#')
        self.synbiohub = rdflib.URIRef('http://wiki.synbiohub.org/wiki/Terms/synbiohub#')

class Objects:
    def __init__(self, namespaces):
        self.namespaces = namespaces
        self.component_definition = rdflib.term.URIRef(self.namespaces.sbol + 'ComponentDefinition')
        self.component = rdflib.term.URIRef(self.namespaces.sbol + 'Component')
        self.module_definition = rdflib.term.URIRef(self.namespaces.sbol + 'ModuleDefinition')
        self.range = rdflib.term.URIRef(self.namespaces.sbol + 'Range')
        self.cut = rdflib.term.URIRef(self.namespaces.sbol + 'Cut')
        self.sequence = rdflib.term.URIRef(self.namespaces.sbol + "Sequence")
        self.combinatorial_derivation = rdflib.term.URIRef(self.namespaces.sbol + "CombinatorialDerivation")
        self.experiment = rdflib.term.URIRef(self.namespaces.sbol + "Experiment")
        self.experimental_data = rdflib.term.URIRef(self.namespaces.sbol + "ExperimentalData")
        self.functional_component = rdflib.term.URIRef(self.namespaces.sbol + "FunctionalComponent")
        self.implementation = rdflib.term.URIRef(self.namespaces.sbol + "Implementation")
        self.interaction = rdflib.term.URIRef(self.namespaces.sbol + "Interaction")
        self.generic_location = rdflib.term.URIRef(self.namespaces.sbol + "GenericLocation")
        self.mapsTo = rdflib.term.URIRef(self.namespaces.sbol + "MapsTo")
        self.module = rdflib.term.URIRef(self.namespaces.sbol + "Module")
        self.model = rdflib.term.URIRef(self.namespaces.sbol + "Model")
        self.attachment = rdflib.term.URIRef(self.namespaces.sbol + "Attachment")
        self.collection = rdflib.term.URIRef(self.namespaces.sbol + "Collection")
        self.sequence_annotation = rdflib.term.URIRef(self.namespaces.sbol + "SequenceAnnotation")
        self.sequence_constraint = rdflib.term.URIRef(self.namespaces.sbol + "SequenceConstraint")
        self.participation = rdflib.term.URIRef(self.namespaces.sbol + "Participation")

        self.top_levels = {rdflib.URIRef(self.namespaces.sbol + name) for name in
                            ['Sequence',
                            'ComponentDefinition',
                            'ModuleDefinition',
                            'Model',
                            'Collection',
                            'GenericTopLevel',
                            'Attachment',
                            'Activity',
                            'Agent',
                            'Plan',
                            'Implementation',
                            'CombinatorialDerivation',
                            'Experiment',
                            'ExperimentalData']}

class Predicates:
    def __init__(self, namespaces):
        self.namespaces = namespaces
        self.rdf_type = rdflib.URIRef(rdflib.RDF.type)

        self.display_id = rdflib.term.URIRef(self.namespaces.sbol + 'displayId')
        self.persistent_identity = rdflib.term.URIRef(self.namespaces.sbol + 'persistentIdentity')
        self.version = rdflib.term.URIRef(self.namespaces.sbol + 'version')
        self.title = rdflib.term.URIRef(self.namespaces.dc + 'title')
        self.description = rdflib.term.URIRef(self.namespaces.dc + 'description')


        self.component = rdflib.term.URIRef(self.namespaces.sbol + 'component')
        self.functional_component = rdflib.term.URIRef(self.namespaces.sbol + 'functionalComponent')
        self.sequence_annotation = rdflib.term.URIRef(self.namespaces.sbol + 'sequenceAnnotation')
        self.sequence_constraint = rdflib.term.URIRef(self.namespaces.sbol + 'sequenceConstraint')
        self.location = rdflib.term.URIRef(self.namespaces.sbol + 'location')
        self.sequence = rdflib.term.URIRef(self.namespaces.sbol + 'sequence')
        self.cut = rdflib.term.URIRef(self.namespaces.sbol + 'cut')
        self.at = rdflib.term.URIRef(self.namespaces.sbol + 'at')

        self.definition = rdflib.term.URIRef(self.namespaces.sbol + 'definition')
        self.sequence_constraint_restriction = rdflib.term.URIRef(self.namespaces.sbol + 'restriction')
        self.sequence_constraint_subject = rdflib.term.URIRef(self.namespaces.sbol + 'subject')
        self.sequence_constraint_object = rdflib.term.URIRef(self.namespaces.sbol + 'object')
        self.type = rdflib.term.URIRef(self.namespaces.sbol + 'type')
        self.role = rdflib.term.URIRef(self.namespaces.sbol + 'role')
        self.start = rdflib.term.URIRef(self.namespaces.sbol + 'start')
        self.end = rdflib.term.URIRef(self.namespaces.sbol + 'end')

        self.interaction = rdflib.term.URIRef(self.namespaces.sbol + 'interaction')
        self.participation = rdflib.term.URIRef(self.namespaces.sbol + 'participation')
        self.elements = rdflib.term.URIRef(self.namespaces.sbol + 'elements')
        self.participant = rdflib.term.URIRef(self.namespaces.sbol + 'participant')
        self.encoding = rdflib.term.URIRef(self.namespaces.sbol + 'encoding')
        self.direction = rdflib.term.URIRef(self.namespaces.sbol + 'direction')
        self.access = rdflib.term.URIRef(self.namespaces.sbol + 'access')
        self.orientation = rdflib.term.URIRef(self.namespaces.sbol + 'orientation')

        self.framework = rdflib.term.URIRef(self.namespaces.sbol + 'framework')
        self.language = rdflib.term.URIRef(self.namespaces.sbol + 'language')
        self.source = rdflib.term.URIRef(self.namespaces.sbol + 'source')

        self.local = rdflib.term.URIRef(self.namespaces.sbol + 'local')
        self.remote = rdflib.term.URIRef(self.namespaces.sbol + 'remote')
        self.module = rdflib.term.URIRef(self.namespaces.sbol + 'module')
        self.maps_to = rdflib.term.URIRef(self.namespaces.sbol + 'mapsTo')
        self.variable_component = rdflib.term.URIRef(self.namespaces.sbol + 'variableComponent')


        self.mutable_notes = rdflib.term.URIRef(self.namespaces.synbiohub + 'mutableNotes')
        self.mutable_description = rdflib.term.URIRef(self.namespaces.synbiohub + 'mutableDescription')
        self.mutable_provenance = rdflib.term.URIRef(self.namespaces.synbiohub + 'mutableProvenance')

        self.ownership_predicates = [
            self.module,
            self.maps_to,
            self.interaction,
            self.participation,
            self.functional_component,
            self.sequence_constraint,
            self.location,
            self.sequence_annotation,
            self.variable_component
        ] 

class ExternalIdentifiers:
    def __init__(self, namespaces):
        self.namespaces = namespaces

        self.component_definition_DNA = rdflib.URIRef(self.namespaces.biopax + "Dna")
        self.component_definition_DNARegion = rdflib.URIRef(self.namespaces.biopax + "DnaRegion")
        self.component_definition_RNA = rdflib.URIRef(self.namespaces.biopax + "Rna")
        self.component_definition_RNARegion = rdflib.URIRef(self.namespaces.biopax + "RnaRegion")
        self.component_definition_protein = rdflib.URIRef(self.namespaces.biopax + "Protein")
        self.component_definition_smallMolecule = rdflib.URIRef(self.namespaces.biopax + "SmallMolecule")
        self.component_definition_complex = rdflib.URIRef(self.namespaces.biopax + "Complex")
        self.component_definition_all = rdflib.URIRef("www.placeholder.com/all_type")

        self.component_definition_promoter       = rdflib.URIRef(self.namespaces.sequence_ontology + "0000167")
        self.component_definition_rbs            = rdflib.URIRef(self.namespaces.sequence_ontology + "0000139")
        self.component_definition_cds            = rdflib.URIRef(self.namespaces.sequence_ontology + "0000316")
        self.component_definition_terminator     = rdflib.URIRef(self.namespaces.sequence_ontology + "0000141")
        self.component_definition_gene           = rdflib.URIRef(self.namespaces.sequence_ontology + "0000704")
        self.component_definition_operator       = rdflib.URIRef(self.namespaces.sequence_ontology + "0000057")
        self.component_definition_engineeredGene = rdflib.URIRef(self.namespaces.sequence_ontology + "0000280")
        self.component_definition_mRNA           = rdflib.URIRef(self.namespaces.sequence_ontology + "0000234")
        self.component_definition_engineeredRegion = rdflib.URIRef(self.namespaces.sequence_ontology + "0000804")
        self.component_definition_nonCovBindingSite = rdflib.URIRef(self.namespaces.sequence_ontology + "0001091")
        self.component_definition_effector       = rdflib.URIRef("http://identifiers.org/chebi/CHEBI:35224") 
        self.component_definition_startCodon     = rdflib.URIRef(self.namespaces.sequence_ontology + "0000318")
        self.component_definition_tag            = rdflib.URIRef(self.namespaces.sequence_ontology + "0000324")
        self.component_definition_engineeredTag  = rdflib.URIRef(self.namespaces.sequence_ontology + "0000807")
        self.component_definition_sgRNA          = rdflib.URIRef(self.namespaces.sequence_ontology + "0001998")
        self.component_definition_transcriptionFactor = rdflib.URIRef("http://identifiers.org/go/GO:0003700")

        self.interaction_inhibition = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000169")
        self.interaction_stimulation = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000170")
        self.interaction_biochemical_reaction = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000176")
        self.interaction_noncovalent_bonding = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000177")
        self.interaction_degradation = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000179")
        self.interaction_genetic_production = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000589")
        self.interaction_control = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000168")

        self.participant_inhibitor = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000020")
        self.participant_inhibited = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000642")
        self.participant_stimulator =  rdflib.URIRef(self.namespaces.sbo_biomodels + "0000459")
        self.participant_stimulated = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000643")
        self.participant_modifier = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000019")
        self.participant_modified = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000644")
        self.participant_product = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000011")
        self.participant_reactant = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000010")
        self.participant_participation_promoter = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000598") 
        self.participant_template = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000645")

        self.location_orientation_inline = rdflib.URIRef(self.namespaces.sbol + "inline")
        self.location_orientation_reverseComplement = rdflib.URIRef(self.namespaces.sbol + "reverseComplement")

        self.functional_component_direction_in = rdflib.URIRef(self.namespaces.sbol + "in")
        self.functional_component_direction_out = rdflib.URIRef(self.namespaces.sbol + "out")
        self.functional_component_direction_inout = rdflib.URIRef(self.namespaces.sbol + "inout") 
        self.functional_component_direction_none = rdflib.URIRef(self.namespaces.sbol + "none")

        self.component_instance_acess_public = rdflib.URIRef(self.namespaces.sbol + "public")
        self.component_instance_acess_private = rdflib.URIRef(self.namespaces.sbol + "private")

        self.sequence_encoding_iupacDNA = rdflib.URIRef("http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html")
        self.sequence_encoding_iupacRNA = rdflib.URIRef("http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html")
        self.sequence_encoding_iupacProtein = rdflib.URIRef("http://www.chem.qmul.ac.uk/iupac/AminoAcid/")
        self.sequence_encoding_opensmilesSMILES = rdflib.URIRef("http://www.opensmiles.org/opensmiles.html")

        self.sequence_constraint_restriction_precedes = rdflib.URIRef(self.namespaces.sbol + "precedes")
        self.sequence_constraint_restriction_sameOrientationAs = rdflib.URIRef(self.namespaces.sbol + "sameOrientationAs")
        self.sequence_constraint_restriction_oppositeOrientationAs = rdflib.URIRef(self.namespaces.sbol + "oppositeOrientationAs")
        self.sequence_constraint_restriction_differentFrom = rdflib.URIRef(self.namespaces.sbol + "differentFrom")

        self.model_language_SBML = rdflib.URIRef(self.namespaces.identifier_edam + "format_2585")
        self.model_language_CellML = rdflib.URIRef(self.namespaces.identifier_edam + "format_3240")
        self.model_language_BioPAX = rdflib.URIRef(self.namespaces.identifier_edam + "format_3156")

        self.model_framework_continuous =  rdflib.URIRef(self.namespaces.sbo_biomodels + "0000062")
        self.model_framework_discrete = rdflib.URIRef(self.namespaces.sbo_biomodels + "0000063")

        self.mapsTo_refinement_useRemote = rdflib.URIRef(self.namespaces.sbol + "useRemote")
        self.mapsTo_refinement_useLocal = rdflib.URIRef(self.namespaces.sbol + "useLocal") 
        self.mapsTo_refinement_verifyIdentical  = rdflib.URIRef(self.namespaces.sbol + "verifyIdentical")
        self.mapsTo_refinement_merge = rdflib.URIRef(self.namespaces.sbol + "merge") 

        self.variable_component_cardinality_zeroOrOne = rdflib.URIRef(self.namespaces.sbol + "zeroOrOne") 
        self.variable_component_cardinality_one = rdflib.URIRef(self.namespaces.sbol + "one")
        self.variable_component_cardinality_zeroOrMore = rdflib.URIRef(self.namespaces.sbol + "zeroOrMore")
        self.variable_component_cardinality_oneOrMore = rdflib.URIRef(self.namespaces.sbol + "oneOrMore")

        self.cd_types = [self.component_definition_DNA,
                        self.component_definition_DNARegion,
                        self.component_definition_RNA,
                        self.component_definition_RNARegion,
                        self.component_definition_protein,
                        self.component_definition_smallMolecule,
                        self.component_definition_complex]
        
        self.cd_roles = [self.component_definition_promoter,
                        self.component_definition_rbs,
                        self.component_definition_cds,
                        self.component_definition_terminator,
                        self.component_definition_engineeredRegion,
                        self.component_definition_engineeredGene,
                        self.component_definition_operator,
                        self.component_definition_gene,
                        self.component_definition_mRNA,
                        self.component_definition_sgRNA,              
                        self.component_definition_transcriptionFactor,
                        self.component_definition_effector,
                        self.component_definition_engineeredTag,
                        self.component_definition_tag,
                        self.component_definition_startCodon,
                        self.component_definition_nonCovBindingSite]

        self.participant_roles = [
            self.participant_inhibitor,
            self.participant_inhibited, 
            self.participant_participation_promoter,
            self.participant_stimulator,
            self.participant_stimulated ,
            self.participant_reactant,
            self.participant_product,
            self.participant_modifier,
            self.participant_modified,
            self.participant_template,
        ]

        self.cd_type_names = {
            self.component_definition_DNA : "DNA",
            self.component_definition_DNARegion : "DNA",
            self.component_definition_RNA : "RNA",
            self.component_definition_RNARegion : "RNA",
            self.component_definition_protein : "Protein",
            self.component_definition_smallMolecule : "Small Molecule",
            self.component_definition_complex: "Complex"}

        self.dna_roles = {self.component_definition_promoter : "Promoter",
                        self.component_definition_rbs : "RBS",
                        self.component_definition_cds : "CDS",
                        self.component_definition_terminator : "Terminator",
                        self.component_definition_engineeredRegion : "Engineered Region",
                        self.component_definition_engineeredGene : "Engineered Gene",
                        self.component_definition_operator : "Operator",
                        self.component_definition_gene : "Gene"}

        self.rna_roles = {self.component_definition_mRNA : "mRNA",
                         self.component_definition_sgRNA : "sgRNA",
                         self.component_definition_cds : "CDS-RNA"}                         
        self.protein_roles = {self.component_definition_transcriptionFactor : "Transcriptional Factor"}
        self.small_molecule_roles = {self.component_definition_effector : "Effector"}
        self.complex_roles = {}
        self.undefined_roles = {self.component_definition_sgRNA : "sgRNA",
                                self.component_definition_engineeredTag : "Engineered Tag",
                                self.component_definition_tag : "Tag",
                                self.component_definition_startCodon: "Start Codon",
                                self.component_definition_nonCovBindingSite: "Non-Covalent Binding Site"}
        
        self.cd_role_dict = DefaultKeyDict(self.component_definition_all,{self.component_definition_DNA : self.dna_roles,
                                                                        self.component_definition_DNARegion : self.dna_roles,
                                                                        self.component_definition_RNA: self.rna_roles,
                                                                        self.component_definition_RNARegion: self.rna_roles,
                                                                        self.component_definition_protein: self.protein_roles,
                                                                        self.component_definition_smallMolecule: self.small_molecule_roles,
                                                                        self.component_definition_complex : self.small_molecule_roles,
                                                                        self.component_definition_all : self.undefined_roles})

        self.interaction_type_names = {
            self.interaction_inhibition: "Inhibition",
            self.interaction_stimulation:"Stimulation",
            self.interaction_biochemical_reaction:"Biochemical reaction",
            self.interaction_noncovalent_bonding:"Noncovalent bonding",
            self.interaction_degradation:"Degradation",
            self.interaction_genetic_production:"Genetic production",
            self.interaction_control:"Control"
        }
        self.inhibition_participants = {self.participant_inhibitor : "Inhibitor",
                                        self.participant_inhibited : "Inhibited", 
                                        self.participant_participation_promoter : "Promoter"}
                                        
        self.stimulation_participants = {self.participant_stimulator : "Stimulator",
                                         self.participant_stimulated : "Stimulated", 
                                         self.participant_participation_promoter : "Promoter"}

        self.biochemical_reaction_participants = {self.participant_reactant : "Reactant",
                                                    self.participant_product : "Product",
                                                    self.participant_modifier : "Modifier",
                                                    self.participant_modified : "Modified"} 

        self.noncovalent_bonding_participants = {self.participant_reactant : "Reactant",
                                                 self.participant_product : "Product"}

        self.degradation_participants = {self.participant_reactant : "Reactant"}
        self.genetic_production_participants = {self.participant_participation_promoter : "Promoter",
                                                self.participant_template : "Participant",
                                                self.participant_product : "Product"} 
        self.control_participants = {self.participant_modifier : "Modifier",
                                     self.participant_modified : "Modified"}

        self.interaction_participant_dict = {self.interaction_inhibition : self.inhibition_participants,
                                            self.interaction_stimulation : self.stimulation_participants,
                                            self.interaction_biochemical_reaction : self.biochemical_reaction_participants,
                                            self.interaction_noncovalent_bonding : self.noncovalent_bonding_participants,
                                            self.interaction_degradation : self.degradation_participants,
                                            self.interaction_genetic_production : self.genetic_production_participants,
                                            self.interaction_control : self.control_participants}
        


        self.encoding_map = {self.component_definition_DNA : self.sequence_encoding_iupacDNA,
                            self.component_definition_DNARegion : self.sequence_encoding_iupacDNA,
                            self.component_definition_RNA : self.sequence_encoding_iupacRNA,
                            self.component_definition_RNARegion : self.sequence_encoding_iupacRNA,
                            self.component_definition_protein : self.sequence_encoding_iupacProtein,
                            self.component_definition_smallMolecule : self.sequence_encoding_opensmilesSMILES,
                            self.component_definition_complex : ""}

    def get_component_definition_identifier_name(self,cd_type,role = None):
        '''
        Reverse method that when you know the URI's return a descriptive name for said ComponentDefinition
        '''
        cd_type_name = None
        cd_role_name = None
        try:
            return self.undefined_roles[role]
        except KeyError:
            pass
        try:
            cd_type_name = self.cd_type_names[cd_type]
        except KeyError:
            return "Unknown"
        try:
            cd_role_name = self.cd_role_dict[cd_type][role]
        except KeyError:
            return cd_type_name
        return cd_role_name

    def get_type_from_role(self,role):
        if role in self.dna_roles:
            return self.component_definition_DNA
        if role in self.rna_roles:
            return self.component_definition_RNA
        if role in self.protein_roles:
            return self.component_definition_protein
        if role in self.small_molecule_roles:
            return self.component_definition_smallMolecule
        if role in self.complex_roles or role in self.undefined_roles:
            return self.component_definition_complex

    def get_participant_role_name(self,role):
        try:
            self.interaction_type_names[role]
        except KeyError:
            return "Unknown"

    def get_interaction_type_name(self,int_type):
        if int_type == self.interaction_inhibition:
            return "Inhibition"
        if int_type == self.interaction_stimulation:
            return "Stimulation"
        if int_type == self.interaction_biochemical_reaction:
            return "Biochemical reaction"
        if int_type == self.interaction_noncovalent_bonding:
            return "Noncovalent bonding"
        if int_type == self.interaction_degradation:
            return "Degradation"
        if int_type == self.interaction_genetic_production:
            return "Genetic production"
        if int_type == self.interaction_control:
            return "Control"
        return "Unknown"
    
    def get_location_orientation_name(self,orientation):
        if orientation == self.location_orientation_inline:
            return "Inline"
        if orientation == self.location_orientation_reverseComplement:
            return "Reverse Complement"

    def get_model_framework_name(self,framework):
        if framework == self.model_framework_continuous:
            return "Continuous"
        if framework == self.model_framework_discrete:
            return "Discrete"
        return "Unknown Framework"

    def get_model_language_name(self,language):
        if language == self.model_language_SBML:
            return "SBML"
        if language == self.model_language_CellML:
            return "CellML"
        if language == self.model_language_BioPAX:
            return "BioPAX"
        return "Unknown Language"

    def are_equivalent(self,type1,type2):
        potential_dicts = [self.cd_role_dict,self.interaction_participant_dict]
        for p_dict in potential_dicts:
            try:
                if p_dict[type1] == p_dict[type2]:
                    return True
            except KeyError:
                continue
        return False


class DefaultKeyDict(dict):
    def __init__(self, default_key, *args, **kwargs):
        self.default_key = default_key
        super(DefaultKeyDict, self).__init__(*args, **kwargs)

    def __missing__ (self, key):
        if self.default_key not in self:  # default key not defined
            raise KeyError(key)
        return self[self.default_key]

    def __repr__(self):
        return ('{}({!r}, {})'.format(self.__class__.__name__,
                                      self.default_key,
                                      super(DefaultKeyDict, self).__repr__()))

    def __reduce__(self):  # optional, for pickle support
        args = (self.default_key if self.default_key in self else None,)
        return self.__class__, args, None, None, self.iteritems()

identifiers = SBOLIdentifiers()