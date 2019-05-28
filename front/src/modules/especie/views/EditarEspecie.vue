<template>
    <v-form
        v-model="valid"
    >
        <v-flex v-if="dadosEspecie.id === 'undefined'">
            <carregando
                :text="'Carregando dados da edição'"
            />
        </v-flex>
        <v-flex
            v-else
            xs10
            offset-xs1
        >
            <h3>Edição de espécie</h3>
            <v-card
                class="pa-3"
            >
                <v-text-field
                    v-model="dadosEspecie.familia"
                    @change="atualizarCampo('familia', $event) "
                    label="Família"
                />
                <v-text-field
                    v-model="dadosEspecie.nome_cientifico"
                    @change="atualizarCampo('nome_cientifico', $event) "
                    label="Nome científico"
                />
                <v-text-field
                    v-model="dadosEspecie.nomes_populares"
                    @change="atualizarCampo('nomes_populares', $event) "
                    label="Nomes populares"
                />
            </v-card>
            <v-card
                class="pa-3"
            >
                <v-text-field
                    v-model="dadosEspecie.inicio_colheita"
                    @change="atualizarCampo('inicio_colheita', $event) "
                    label="Início da colheita"
                />
                <v-select
                    v-model="dadosEspecie.porte"
                    :items="getEspecieMetadata.porte"
                    item-text="descricao"
                    item-value="valor"
                    @change="atualizarCampo('porte', $event) "
                    label="Porte"
                />
                <v-select
                    v-model="dadosEspecie.estrato"
                    :items="getEspecieMetadata.estrato"
                    item-text="descricao"
                    item-value="valor"
                    @change="atualizarCampo('estrato', $event) "
                    label="Estrato"
                />
                <v-select
                    v-model="dadosEspecie.sucessao"
                    :items="getEspecieMetadata.sucessao"
                    item-text="descricao"
                    item-value="valor"
                    @change="atualizarCampo('sucessao', $event) "
                    label="Sucessão"
                />
                <v-select
                    v-model="dadosEspecie.umidade"
                    :items="getEspecieMetadata.umidade"
                    @change="atualizarCampo('umidade', $event) "
                    label="Umidade"
                />
                <v-select
                    v-model="dadosEspecie.tolerancia_poda"
                    :items="getEspecieMetadata.tolerancia_poda"
                    @change="atualizarCampo('tolerancia_poda', $event) "
                    label="Tolerância a poda"
                />
            </v-card>
            <v-card
                class="pa-3"
            >
                <v-text-field
                    v-model="dadosEspecie.temperatura_min"
                    xs4
                    @change="atualizarCampo('temperatura_min', $event) "
                    label="Temperatura mínima"
                />
                <v-text-field
                    v-model="dadosEspecie.temperatura_max"
                    xs4
                    @change="atualizarCampo('temperatura_max', $event) "
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
import Carregando from '@/components/CarregandoVuetify';
import Tools from '@/mixins/tools';
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'EditarEspecie',
    components: {
        Carregando,
    },
    mixins: [
        Tools,
    ],
    data() {
        return {
            valid: true,
            dadosEditados: {
                id: '',
                nomes_populares: '',
                nome_cientifico: '',
                familia: '',
                exigencia_solo: '',
                temperatura_min: '',
                temperatura_max: '',
                inicio_colheita: '',
                tempo_vida: '',
                sucessao: '',
                porte: '',
                umidade: '',
                tolerancia_poda: '',
            },
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
    watch: {
        dadosEspecie() {
            this.inicializarDadosEspecie();
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
        inicializarDadosEspecie() {
            this.dadosEditados = {
                id: this.dadosEspecie.id,
                nomes_populares: this.dadosEspecie.nomes_populares,
                nome_cientifico: this.dadosEspecie.nome_cientifico,
                familia: this.dadosEspecie.familia,
                exigencia_solo: this.dadosEspecie.exigencia_solo,
                temperatura_min: this.dadosEspecie.temperatura_min,
                temperatura_max: this.dadosEspecie.temperatura_max,
                inicio_colheita: this.dadosEspecie.inicio_colheita,
                tempo_vida: this.dadosEspecie.tempo_vida,
                sucessao: this.dadosEspecie.sucessao,
                porte: this.dadosEspecie.porte,
            };
        },
        atualizarCampo(key, value) {
            if (Object.keys(this.dadosEditados).includes(key)) {
                this.dadosEditados[key] = value;
            }
        },
        salvar() {
            this.updateEspecie(this.dadosEditados);
        },
    },
};
</script>
