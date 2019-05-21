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
                    :items="porte_items"
                    label="Porte"
                />
                <v-select
                    v-model="dadosEspecie.estrato"
                    :items="estrato_items"
                    label="Estrato"
                />
                <v-select
                    v-model="dadosEspecie.sucessao"
                    :items="sucessao_items"
                    label="Sucessão"
                />
                <v-select
                    v-model="dadosEspecie.umidade"
                    :items="umidade_items"
                    label="Umidade"
                />
                <v-select
                    v-model="dadosEspecie.tolerancia_poda"
                    :items="tolerancia_poda_items"
                    label="Tolerância a poda"
                />
            </v-card>
            <v-card
                class="pa-3"
            >
                <v-text-field
                    xs4
                    v-model="dadosEspecie.temperatura_min"
                    label="Temperatura mínima"
                />
                <v-text-field
                    xs4
                    v-model="dadosEspecie.temperatura_max"
                    label="Temperatura máxima"
                />
            </v-card>
            <v-btn
                color="info"
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
            porte_items: [],
            estrato_items: [],
            sucessao_items: [],
            umidade_items: [],
            tolerancia_poda_items: [],
        };
    },
    computed: {
        ...mapGetters({
            dadosEspecie: 'especie/especie',
        }),
        id() {
            return this.$route.params.id;
        },
    },
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscarEspecie(this.$route.params.id);
        }
    },
    methods: {
        ...mapActions({
            buscarEspecie: 'especie/buscarEspecie',
        }),
    },
};
</script>
