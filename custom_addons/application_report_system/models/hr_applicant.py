# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrApplicant(models.Model):
    _inherit = "hr.applicant"

    technical_score = fields.Integer("Score Technique")
    soft_skill_score = fields.Integer("Score Soft Skills")

    strengths = fields.Text("Forces")
    weaknesses = fields.Text("Faiblesses")

    recommendation = fields.Selection([
        ('strong_yes', 'Fortement recommander'),
        ('yes', 'Recommander'),
        ('neutral', 'Neutre'),
        ('no', 'Mauvais profil'),
    ], string="Recommandation")

    executive_summary = fields.Text(string="Synthèse Executive")
    evaluation_table = fields.Text(string="Evaluation des compétences")
    motivation = fields.Text(string="Motivation & Projection")
    vigilance_points = fields.Text(string="Points de vigilance")
    availability = fields.Char(string="Disponibilité")
    expected_salary = fields.Char(string="Rémunération souhaitée")
    firm_opinion = fields.Text(string="Avis du cabinet")
    next_steps = fields.Text(string="Suite du processus")

    # ===== INFOS SUPPLÉMENTAIRES =====
    last_degree = fields.Char("Dernier diplôme")
    candidate_location = fields.Char("Localisation du candidat")
    job_location = fields.Char("Localisation du poste")
    mobility = fields.Char("Mobilité")

    interview_mode = fields.Selection([
        ('physique', 'Présentiel'),
        ('visio', 'Visioconférence'),
        ('telephone', 'Téléphonique')
    ], string="Mode de réalisation de l'entretien")

    consultant_signature = fields.Binary("Signature consultant")

    job_id = fields.Many2one('hr.job', string="Poste")

    # Lien vers les lignes d'évaluation
    evaluation_line_ids = fields.One2many(
        "applicant.evaluation.line",
        "applicant_id",
        string="Evaluations"
    )

    def generate_evaluation_lines(self):
        """Crée les lignes d'évaluation pour le candidat à partir des critères du poste"""
        for applicant in self:
            if applicant.job_id:
                criteria_list = self.env['job.evaluation.criteria'].search([('job_id', '=', applicant.job_id.id)])
                for crit in criteria_list:
                    # Ne créer que si la ligne n'existe pas déjà
                    if not applicant.evaluation_line_ids.filtered(lambda l: l.criteria_id == crit):
                        self.env['applicant.evaluation.line'].create({
                            'applicant_id': applicant.id,
                            'criteria_id': crit.id,
                        })

    @api.model
    def create(self, vals):
        record = super().create(vals)
        record.generate_evaluation_lines()
        return record
    
    @api.onchange('job_id')
    def _onchange_job_id_generate_lines(self):
        for applicant in self:
            if applicant.job_id:
                # Supprimer anciennes lignes
                applicant.evaluation_line_ids = [(5, 0, 0)]

                criteria_list = self.env['job.evaluation.criteria'].search([
                    ('job_id', '=', applicant.job_id.id)
                ])

                lines = []
                for crit in criteria_list:
                    lines.append((0, 0, {
                        'criteria_id': crit.id,
                        'sequence': crit.sequence if hasattr(crit, 'sequence') else 10
                    }))

                applicant.evaluation_line_ids = lines
    
class ApplicantEvaluationLine(models.Model):
    _name = "applicant.evaluation.line"
    _description = "Applicant Evaluation Line"
    _order = "sequence"

    applicant_id = fields.Many2one(
        "hr.applicant",
        string="Candidature",
        ondelete="cascade",
        required=True
    )

    sequence = fields.Integer(default=10)

    criteria_id = fields.Many2one(
        "job.evaluation.criteria",
        string="Critère",
        required=True
    )

    summary = fields.Char(string="Synthèse")
    description = fields.Html(string="Description détaillée")

    # Poste lié automatiquement au candidat
    job_id = fields.Many2one(
        "hr.job",
        string="Poste",
        compute="_compute_job_id",
        store=True
    )

    @api.depends('applicant_id')
    def _compute_job_id(self):
        for line in self:
            line.job_id = line.applicant_id.job_id

    # filtrage dynamique des critères
    @api.onchange('applicant_id')
    def _onchange_applicant_id(self):
        if self.applicant_id and self.applicant_id.job_id:
            return {
                'domain': {
                    'criteria_id': [
                        ('job_id', '=', self.applicant_id.job_id.id)
                    ]
                }
            }

    # Sécurité supplémentaire à la création
    @api.model
    def create(self, vals):
        if vals.get('applicant_id') and not vals.get('job_id'):
            applicant = self.env['hr.applicant'].browse(vals['applicant_id'])
            vals['job_id'] = applicant.job_id.id
        return super().create(vals)


class JobEvaluationCriteria(models.Model):
    _name = "job.evaluation.criteria"
    _description = "Critères d'évaluation par poste"

    name = fields.Char("Critère", required=True)
    job_id = fields.Many2one("hr.job", string="Poste", required=True)

    _sql_constraints = [
        (
            'unique_criteria_per_job',
            'unique(name, job_id)',
            'Ce critère existe déjà pour ce poste.'
        )
    ]



