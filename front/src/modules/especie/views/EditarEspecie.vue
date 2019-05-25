<template>
    <v-form
        v-model="valid"
    >
        <v-flex
            xs10
            offset-xs1
        >
            <h3>Edição de espécie</h3>
            <v-card
                class="pa-3"
            >
                <v-text-field
                    v-model="dadosEspecie.familia"
                    label="Família"
                />
                <v-text-field
                    v-model="dadosEspecie.nome_cientifico"
                    label="Nome científico"
                />
                <v-text-field
                    v-model="dadosEspecie.nomes_populares"
                    label="Nomes populares"
                />
            </v-card>
            <v-card
                class="pa-3"
            >
                <v-text-field
                    v-model="dadosEspecie.inicio_colheita"
                    label="Início da colheita"
                />
                <v-select
                    v-model="dadosEspecie.porte"
                    :items="getEspecieMetadata.porte"
                    label="Porte"
                />
                <v-select
                    v-model="dadosEspecie.estrato"
                    :items="getEspecieMetadata.estrato"
                    label="Estrato"
                />
                <v-select
                    v-model="dadosEspecie.sucessao"
                    :items="getEspecieMetadata.sucessao"
                    label="Sucessão"
                />
                <v-select
                    v-model="dadosEspecie.umidade"
                    :items="getEspecieMetadata.umidade"
                    label="Umidade"
                />
                <v-select
                    v-model="dadosEspecie.tolerancia_poda"
                    :items="getEspecieMetadata.tolerancia_poda"
                    label="Tolerância a poda"
                />
            </v-card>
            <v-card
                class="pa-3"
            >
                <v-text-field
                    v-model="dadosEspecie.temperatura_min"
                    xs4
                    label="Temperatura mínima"
                />
                <v-text-field
                    v-model="dadosEspecie.temperatura_max"
                    xs4
                    label="Temperatura máxima"
                />
            </v-card>
            <v-btn
                color="info"
                @click="salvar()"
            >
                <v-icon
                    class="pr-3"
                >save</v-icon>
                salvar
            </v-btn>
            <v-btn
                color="error"
                @click="voltar()"
            >
                <v-icon
                    class="pr-3"
                >cancel</v-icon>
                cancelar
            </v-btn>
        </v-flex>
    </v-form>
</template>
<script>
import Tools from '@/mixins/tools';
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'EditarEspecie',
    mixins: [
        Tools,
    ],
    data() {
        return {
            valid: true,
        };
    },
    computed: {
        ...mapGetters({
            dadosEspecie: 'especie/especie',
            getEspecieMetadata: 'especie/getEspecieMetadata',
        }),
        id() {
            return this.$route.params.id;
        },
    },
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscarEspecie(this.$route.params.id);
            this.buscarEspecieMetadata();
        }
    },
    methods: {
        ...mapActions({
            buscarEspecie: 'especie/buscarEspecie',
            buscarEspecieMetadata: 'especie/buscarEspecieMetadata',
            updateEspecie: 'especie/updateEspecie',
        }),
        salvar() {
            this.updateEspecie(
                {
                    id: this.dadosEspecie.id,
                    nomes_populares: this.dadosEspecie.nomes_populares,
                },
            );
        },
    },
};
</script>
